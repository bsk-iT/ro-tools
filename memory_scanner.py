import pymem
import win32gui
import win32process
import json
import time
from typing import Dict, List, Optional

class MemoryScanner:
    def __init__(self):
        self.pm = None
        self.base_address = None
        self.module_name = None

    def find_ragnarok_process(self) -> List[Dict]:
        """Encontra processos do Ragnarok"""
        processes = []
        
        def enum_windows_callback(hwnd, _):
            try:
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                if win32gui.IsWindowVisible(hwnd):
                    window_title = win32gui.GetWindowText(hwnd)
                    # Procurar por janelas que possam ser do Ragnarok
                    keywords = ["ragnarok", "ro", "rtales", "gravity"]
                    if any(keyword in window_title.lower() for keyword in keywords) or not window_title:
                        processes.append({
                            'pid': pid,
                            'title': window_title or f"PID {pid}",
                            'hwnd': hwnd
                        })
            except:
                pass
        
        win32gui.EnumWindows(enum_windows_callback, None)
        return processes

    def connect_to_process(self, pid: int) -> bool:
        """Conecta ao processo especificado"""
        try:
            self.pm = pymem.Pymem()
            self.pm.open_process_from_id(pid)
            
            # Tentar encontrar o módulo principal
            modules = pymem.process.list_modules(self.pm.process_handle)
            
            # Procurar por módulos conhecidos do Ragnarok
            known_modules = ["rtales.bin", "client.exe", "ragexe.exe", "ragnarok.exe"]
            
            for module in modules:
                if any(known in module.name.lower() for known in known_modules):
                    self.module_name = module.name
                    self.base_address = module.lpBaseOfDll
                    print(f"✅ Módulo encontrado: {self.module_name} (Base: 0x{self.base_address:08X})")
                    return True
            
            # Se não encontrou um módulo conhecido, usar o primeiro
            if modules:
                self.module_name = modules[0].name
                self.base_address = modules[0].lpBaseOfDll
                print(f"⚠️ Usando módulo padrão: {self.module_name} (Base: 0x{self.base_address:08X})")
                return True
                
            return False
            
        except Exception as e:
            print(f"❌ Erro ao conectar ao processo: {e}")
            return False

    def scan_for_patterns(self) -> Dict[str, str]:
        """Escaneia a memória procurando por padrões conhecidos"""
        if not self.pm or not self.base_address:
            return {}
        
        results = {}
        
        print("\n🔍 Escaneando memória por padrões...")
        
        # Padrões para buscar (valores típicos que podem indicar HP, SP, etc.)
        patterns_to_scan = [
            {
                'name': 'hp_offset',
                'description': 'HP atual (procure valores entre 1-999999)',
                'scan_type': 'user_input'
            },
            {
                'name': 'x_pos_offset', 
                'description': 'Posição X (procure valores entre 0-1000)',
                'scan_type': 'user_input'
            },
            {
                'name': 'map_offset',
                'description': 'Nome do mapa (string)',
                'scan_type': 'user_input'
            },
            {
                'name': 'job_offset',
                'description': 'Job ID (valores entre 0-4218)',
                'scan_type': 'user_input'
            }
        ]
        
        for pattern in patterns_to_scan:
            print(f"\n--- {pattern['description']} ---")
            print("No Cheat Engine, encontre o endereço para este valor.")
            address_input = input(f"Cole o endereço encontrado (ex: 0x12345678) ou 'skip': ")
            
            if address_input.lower() == 'skip':
                continue
                
            try:
                # Converter endereço absoluto para offset relativo
                absolute_addr = int(address_input, 16)
                relative_offset = absolute_addr - self.base_address
                
                # Verificar se o offset é válido (dentro do módulo)
                if 0 <= relative_offset <= 0x10000000:  # 256MB limite razoável
                    results[pattern['name']] = f"0x{relative_offset:08X}"
                    print(f"✅ Offset calculado: 0x{relative_offset:08X}")
                    
                    # Tentar ler o valor para validar
                    try:
                        value = self.pm.read_uint(absolute_addr)
                        print(f"   Valor atual: {value}")
                    except:
                        print("   ⚠️ Não foi possível ler o valor")
                else:
                    print(f"❌ Offset muito grande: 0x{relative_offset:08X}")
                    
            except ValueError:
                print("❌ Endereço inválido")
            except Exception as e:
                print(f"❌ Erro: {e}")
        
        return results

    def update_servers_json(self, new_offsets: Dict[str, str]):
        """Atualiza o arquivo servers.json com os novos offsets"""
        try:
            with open("servers.json", "r", encoding="utf-8") as f:
                servers_data = json.load(f)
            
            # Atualizar offsets para rtales.bin
            if "rtales.bin" in servers_data:
                for key, value in new_offsets.items():
                    if value:  # Só atualizar se o valor não estiver vazio
                        servers_data["rtales.bin"][key] = value
                        print(f"✅ Atualizado {key}: {value}")
                
                # Fazer backup do arquivo original
                with open("servers_backup.json", "w", encoding="utf-8") as f:
                    json.dump(servers_data, f, indent=2, ensure_ascii=False)
                
                # Salvar arquivo atualizado
                with open("servers.json", "w", encoding="utf-8") as f:
                    json.dump(servers_data, f, indent=2, ensure_ascii=False)
                
                print("✅ Arquivo servers.json atualizado com sucesso!")
                print("💾 Backup salvo como servers_backup.json")
            else:
                print("❌ Entrada 'rtales.bin' não encontrada no servers.json")
                
        except Exception as e:
            print(f"❌ Erro ao atualizar servers.json: {e}")

def main():
    print("=== ESCANEADOR DE MEMÓRIA PARA RAGNAROK ===\n")
    
    scanner = MemoryScanner()
    
    # Encontrar processos
    processes = scanner.find_ragnarok_process()
    if not processes:
        print("❌ Nenhum processo encontrado!")
        print("\nDica: Certifique-se de que o Ragnarok esteja rodando.")
        return
    
    print("Processos encontrados:")
    for i, proc in enumerate(processes):
        print(f"{i}: PID {proc['pid']} - {proc['title']}")
    
    # Selecionar processo
    if len(processes) > 1:
        choice = input(f"\nEscolha o processo (0-{len(processes)-1}): ")
        try:
            selected = processes[int(choice)]
        except:
            selected = processes[0]
    else:
        selected = processes[0]
    
    print(f"\nConectando ao processo: PID {selected['pid']}")
    
    if not scanner.connect_to_process(selected['pid']):
        print("❌ Falha ao conectar ao processo")
        return
    
    print("\n📋 INSTRUÇÕES:")
    print("1. Abra o Cheat Engine")
    print("2. Conecte ao mesmo processo do Ragnarok")
    print("3. Para cada valor solicitado:")
    print("   - Procure o endereço no Cheat Engine")
    print("   - Copie o endereço completo (ex: 0x12345678)")
    print("   - Cole aqui quando solicitado")
    print("\n⚠️ IMPORTANTE: Use os endereços EXATOS do Cheat Engine!")
    
    input("\nPressione Enter quando estiver pronto...")
    
    # Escanear por padrões
    new_offsets = scanner.scan_for_patterns()
    
    if new_offsets:
        print("\n=== NOVOS OFFSETS ENCONTRADOS ===")
        for key, value in new_offsets.items():
            print(f"{key}: {value}")
        
        update = input("\nDeseja atualizar o servers.json? (s/n): ")
        if update.lower() in ['s', 'sim', 'y', 'yes']:
            scanner.update_servers_json(new_offsets)
    else:
        print("\n❌ Nenhum offset foi configurado.")

if __name__ == "__main__":
    main()