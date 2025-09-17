"""
Script para testar se os novos endereços estão funcionando corretamente
"""
import pymem
import psutil
import time
from service.servers_file import SERVERS_FILE, HP_OFFSET, X_POS_OFFSET, MAP_OFFSET, JOB_OFFSET

def find_rtales_process():
    """Encontra o processo rtales.bin"""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'rtales.bin' in proc.info['name'].lower():
                return proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None

def test_memory_addresses():
    """Testa se os endereços estão funcionando"""
    print("🧪 TESTE DOS NOVOS ENDEREÇOS DE MEMÓRIA\n")
    
    # Encontrar processo
    pid = find_rtales_process()
    if not pid:
        print("❌ Processo rtales.bin não encontrado!")
        print("Certifique-se de que o RagnaTales esteja rodando.")
        return False
    
    print(f"✅ Processo rtales.bin encontrado (PID: {pid})")
    
    try:
        # Conectar ao processo
        pm = pymem.Pymem()
        pm.open_process_from_id(pid)
        
        # Obter base address usando método compatível
        try:
            # Tentar método mais novo
            modules = pymem.process.enum_process_modules(pm.process_handle)
            base_address = modules[0].lpBaseOfDll
            module_name = modules[0].szModule
        except AttributeError:
            # Fallback para método alternativo
            import ctypes
            from ctypes import wintypes
            
            # Usar GetModuleHandleEx para obter o base address
            kernel32 = ctypes.windll.kernel32
            base_address = kernel32.GetModuleHandleW(None)
            if not base_address:
                # Se falhar, usar base address padrão comum
                base_address = 0x00400000
            module_name = "rtales.bin"
        
        print(f"✅ Módulo: {module_name}")
        print(f"✅ Base Address: 0x{base_address:08X}")
        
        # Carregar offsets do arquivo
        hp_offset = int(SERVERS_FILE.get_value(HP_OFFSET), 16)
        x_pos_offset = int(SERVERS_FILE.get_value(X_POS_OFFSET), 16) 
        map_offset = int(SERVERS_FILE.get_value(MAP_OFFSET), 16)
        job_offset = int(SERVERS_FILE.get_value(JOB_OFFSET), 16)
        
        print(f"\n=== OFFSETS CARREGADOS ===")
        print(f"HP Offset: 0x{hp_offset:08X}")
        print(f"X Pos Offset: 0x{x_pos_offset:08X}")
        print(f"Map Offset: 0x{map_offset:08X}")
        print(f"Job Offset: 0x{job_offset:08X}")
        
        # Testar cada endereço
        print(f"\n=== TESTANDO LEITURA DOS VALORES ===")
        
        tests_passed = 0
        total_tests = 0
        
        # Teste HP
        try:
            hp_address = base_address + hp_offset
            hp_value = pm.read_uint(hp_address)
            print(f"✅ HP: {hp_value} (endereço: 0x{hp_address:08X})")
            if 1 <= hp_value <= 999999:  # HP razoável
                tests_passed += 1
            else:
                print(f"   ⚠️ Valor de HP suspeito: {hp_value}")
            total_tests += 1
        except Exception as e:
            print(f"❌ Erro ao ler HP: {e}")
            total_tests += 1
        
        # Teste Posição X
        try:
            x_pos_address = base_address + x_pos_offset
            x_pos_value = pm.read_uint(x_pos_address)
            print(f"✅ Posição X: {x_pos_value} (endereço: 0x{x_pos_address:08X})")
            if 0 <= x_pos_value <= 1000:  # Posição razoável
                tests_passed += 1
            else:
                print(f"   ⚠️ Valor de posição X suspeito: {x_pos_value}")
            total_tests += 1
        except Exception as e:
            print(f"❌ Erro ao ler Posição X: {e}")
            total_tests += 1
        
        # Teste Job
        try:
            job_address = base_address + job_offset
            job_value = pm.read_uint(job_address)
            print(f"✅ Job ID: {job_value} (endereço: 0x{job_address:08X})")
            if 0 <= job_value <= 4218:  # Job ID razoável
                tests_passed += 1
            else:
                print(f"   ⚠️ Valor de Job ID suspeito: {job_value}")
            total_tests += 1
        except Exception as e:
            print(f"❌ Erro ao ler Job ID: {e}")
            total_tests += 1
        
        # Teste Mapa (string)
        try:
            map_address = base_address + map_offset
            # Ler como string (até 20 caracteres)
            map_bytes = pm.read_bytes(map_address, 20)
            map_name = map_bytes.split(b'\x00')[0].decode('ascii', errors='ignore')
            print(f"✅ Mapa: '{map_name}' (endereço: 0x{map_address:08X})")
            if len(map_name) > 0 and map_name.isalpha():
                tests_passed += 1
            else:
                print(f"   ⚠️ Nome do mapa suspeito: '{map_name}'")
            total_tests += 1
        except Exception as e:
            print(f"❌ Erro ao ler Mapa: {e}")
            total_tests += 1
        
        # Resultado final
        print(f"\n" + "="*50)
        print(f"📊 RESULTADO DO TESTE: {tests_passed}/{total_tests} endereços válidos")
        
        if tests_passed == total_tests:
            print(f"🎉 SUCESSO! Todos os endereços estão funcionando!")
            print(f"✅ O RO Tools agora deve conseguir ler os valores corretamente.")
        elif tests_passed >= total_tests // 2:
            print(f"⚠️ PARCIALMENTE FUNCIONAL: {tests_passed} de {total_tests} endereços válidos")
            print(f"📝 Alguns endereços podem precisar de ajustes.")
        else:
            print(f"❌ FALHA: Apenas {tests_passed} de {total_tests} endereços válidos")
            print(f"🔧 Os endereços podem estar incorretos ou o processo mudou.")
        
        pm.close_process()
        return tests_passed == total_tests
        
    except Exception as e:
        print(f"❌ Erro ao acessar memória: {e}")
        return False

def continuous_monitoring():
    """Monitora os valores continuamente para verificar se estão atualizando"""
    print(f"\n🔄 MONITORAMENTO CONTÍNUO (pressione Ctrl+C para parar)\n")
    
    pid = find_rtales_process()
    if not pid:
        print("❌ Processo não encontrado!")
        return
    
    try:
        pm = pymem.Pymem()
        pm.open_process_from_id(pid)
        
        # Obter base address usando método compatível
        try:
            # Usar base address padrão para executáveis Windows
            base_address = 0x00400000
            module_name = "rtales.bin"
        except Exception:
            base_address = 0x00400000
            module_name = "rtales.bin"
        
        hp_offset = int(SERVERS_FILE.get_value(HP_OFFSET), 16)
        x_pos_offset = int(SERVERS_FILE.get_value(X_POS_OFFSET), 16)
        
        print("Monitorando HP e Posição X (valores devem mudar quando você se mover no jogo):")
        
        while True:
            try:
                hp = pm.read_uint(base_address + hp_offset)
                x_pos = pm.read_uint(base_address + x_pos_offset)
                print(f"\rHP: {hp:>6} | Pos X: {x_pos:>3}", end="", flush=True)
                time.sleep(0.5)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"\n❌ Erro: {e}")
                break
        
        print(f"\n\n✅ Monitoramento finalizado.")
        pm.close_process()
        
    except Exception as e:
        print(f"❌ Erro: {e}")

def main():
    print("🧪 TESTE DOS ENDEREÇOS DE MEMÓRIA ATUALIZADOS\n")
    
    print("="*60)
    print("OPÇÕES:")
    print("1 - Testar endereços uma vez")
    print("2 - Monitoramento contínuo")
    print("3 - Sair")
    print("="*60)
    
    choice = input("\nEscolha uma opção (1-3): ")
    
    if choice == "1":
        success = test_memory_addresses()
        if success:
            print(f"\n🎯 PRÓXIMOS PASSOS:")
            print(f"1. Inicie o RO Tools")
            print(f"2. Conecte ao processo rtales.bin")
            print(f"3. Ative o monitoramento")
            print(f"4. Teste as funcionalidades (auto pot, etc.)")
    elif choice == "2":
        continuous_monitoring()
    elif choice == "3":
        print("👋 Saindo...")
    else:
        print("❌ Opção inválida!")

if __name__ == "__main__":
    main()