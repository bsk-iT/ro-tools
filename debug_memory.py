import pymem
import win32gui
import win32process
import psutil
from service.servers_file import SERVERS_FILE, HP_OFFSET, X_POS_OFFSET, MAP_OFFSET, JOB_OFFSET

def find_ragnarok_process():
    """Encontra o processo do Ragnarok"""
    processes = []
    
    # Procurar por processos que podem ser do Ragnarok
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            proc_info = proc.info
            proc_name = proc_info['name'].lower()
            
            # Procurar por nomes conhecidos do Ragnarok
            ragnarok_names = ['rtales.bin', 'ragexe.exe', 'client.exe', 'ragnarok.exe']
            
            if any(name in proc_name for name in ragnarok_names):
                processes.append({
                    'pid': proc_info['pid'],
                    'name': proc_info['name'],
                    'title': f"{proc_info['name']} (PID: {proc_info['pid']})"
                })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    return processes

def debug_memory_addresses():
    """Debug dos endereços de memória"""
    print("=== DEBUG DE ENDEREÇOS DE MEMÓRIA ===\n")
    
    # Encontrar processo do Ragnarok
    processes = find_ragnarok_process()
    if not processes:
        print("❌ Nenhum processo do Ragnarok encontrado!")
        print("Certifique-se de que o jogo esteja rodando.")
        print("\nProcessos procurados: rtales.bin, ragexe.exe, client.exe, ragnarok.exe")
        return
    
    print("Processos encontrados:")
    for i, proc in enumerate(processes):
        print(f"{i}: {proc['title']}")
    
    if len(processes) > 1:
        choice = input(f"\nEscolha o processo (0-{len(processes)-1}): ")
        try:
            selected = processes[int(choice)]
        except:
            selected = processes[0]
    else:
        selected = processes[0]
    
    print(f"\nUsando processo: {selected['title']}")
    
    try:
        # Conectar ao processo
        pm = pymem.Pymem()
        pm.open_process_from_id(selected['pid'])
        
        # Obter módulo base (assumindo rtales.bin)
        try:
            modules = pymem.process.enum_process_modules(pm.process_handle)
            base_address = modules[0].lpBaseOfDll  # Primeiro módulo é geralmente o principal
            module_name = modules[0].szModule
            print(f"✅ Módulo principal: {module_name} (Base: 0x{base_address:08X})")
        except Exception as e:
            print(f"❌ Erro ao obter módulos: {e}")
            return
        
        # Ler configurações do servers.json
        hp_offset = SERVERS_FILE.get_value(HP_OFFSET)
        x_pos_offset = SERVERS_FILE.get_value(X_POS_OFFSET)
        map_offset = SERVERS_FILE.get_value(MAP_OFFSET)
        job_offset = SERVERS_FILE.get_value(JOB_OFFSET)
        
        print(f"\n=== OFFSETS CONFIGURADOS ===")
        print(f"HP Offset: {hp_offset}")
        print(f"X Pos Offset: {x_pos_offset}")
        print(f"Map Offset: {map_offset}")
        print(f"Job Offset: {job_offset}")
        
        # Testar cada endereço
        print(f"\n=== TESTANDO ENDEREÇOS ===")
        
        offsets_to_test = [
            ("HP", hp_offset),
            ("X Position", x_pos_offset),
            ("Map", map_offset),
            ("Job", job_offset)
        ]
        
        for name, offset_str in offsets_to_test:
            if offset_str and offset_str != "0x0":
                try:
                    offset = int(offset_str, 16)
                    
                    # Método 1: Offset direto do base address
                    direct_address = base_address + offset
                    print(f"\n{name}:")
                    print(f"  Offset: {offset_str}")
                    print(f"  Endereço direto: 0x{direct_address:08X}")
                    
                    try:
                        direct_value = pm.read_uint(direct_address)
                        print(f"  Valor direto: {direct_value}")
                    except Exception as e:
                        print(f"  ❌ Erro ao ler endereço direto: {e}")
                    
                    # Método 2: Ponteiro (como o código faz)
                    try:
                        pointer_address = pm.read_uint(base_address + offset)
                        print(f"  Endereço do ponteiro: 0x{pointer_address:08X}")
                        if pointer_address:
                            pointer_value = pm.read_uint(pointer_address)
                            print(f"  Valor do ponteiro: {pointer_value}")
                    except Exception as e:
                        print(f"  ❌ Erro ao ler ponteiro: {e}")
                        
                except ValueError:
                    print(f"❌ Offset inválido para {name}: {offset_str}")
        
        pm.close_process()
        
    except Exception as e:
        print(f"❌ Erro ao acessar processo: {e}")

if __name__ == "__main__":
    debug_memory_addresses()