"""
Teste simples de endereços de memória - versão compatível
"""
import pymem
import psutil
import json

def find_rtales_process():
    """Encontra o processo rtales.bin"""
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if 'rtales.bin' in proc.info['name'].lower():
                return proc.info['pid']
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return None

def test_memory_simple():
    """Teste simples dos endereços"""
    print("🧪 TESTE SIMPLES DOS ENDEREÇOS DE MEMÓRIA\n")
    
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
        print("✅ Conectado ao processo com sucesso!")
        
        # Carregar configuração
        with open("servers.json", "r", encoding="utf-8") as f:
            config = json.load(f)["rtales.bin"]
        
        # Base address padrão (como calculamos)
        base_address = 0x00400000
        print(f"✅ Usando Base Address: 0x{base_address:08X}")
        
        # Carregar offsets
        offsets = {
            "HP": int(config["hp_offset"], 16),
            "Posição X": int(config["x_pos_offset"], 16),
            "Mapa": int(config["map_offset"], 16),
            "Job": int(config["job_offset"], 16),
            "Chat": int(config["chat_offset"], 16)
        }
        
        print(f"\n=== TESTANDO ENDEREÇOS ===")
        
        success_count = 0
        total_tests = 0
        
        for name, offset in offsets.items():
            try:
                address = base_address + offset
                print(f"\n{name}:")
                print(f"  Offset: 0x{offset:08X}")
                print(f"  Endereço final: 0x{address:08X}")
                
                if name == "Mapa":
                    # Ler como string
                    try:
                        map_bytes = pm.read_bytes(address, 16)
                        map_name = map_bytes.split(b'\x00')[0].decode('ascii', errors='ignore')
                        print(f"  Valor: '{map_name}'")
                        if len(map_name) > 0:
                            success_count += 1
                            print(f"  ✅ OK - String válida")
                        else:
                            print(f"  ❌ String vazia ou inválida")
                    except:
                        print(f"  ❌ Erro ao ler string")
                else:
                    # Ler como inteiro
                    try:
                        value = pm.read_uint(address)
                        print(f"  Valor: {value}")
                        
                        # Validar valores
                        if name == "HP" and 1 <= value <= 999999:
                            success_count += 1
                            print(f"  ✅ OK - HP válido")
                        elif name == "Posição X" and 0 <= value <= 1000:
                            success_count += 1
                            print(f"  ✅ OK - Posição válida")
                        elif name == "Job" and 0 <= value <= 4218:
                            success_count += 1
                            print(f"  ✅ OK - Job válido")
                        elif name == "Chat":
                            success_count += 1
                            print(f"  ✅ OK - Valor lido")
                        else:
                            print(f"  ⚠️ Valor fora do esperado")
                    except Exception as e:
                        print(f"  ❌ Erro ao ler: {e}")
                
                total_tests += 1
                
            except Exception as e:
                print(f"❌ Erro geral no {name}: {e}")
                total_tests += 1
        
        # Resultado
        print(f"\n" + "="*50)
        print(f"📊 RESULTADO: {success_count}/{total_tests} endereços válidos")
        
        if success_count >= 3:  # Pelo menos 3 valores válidos
            print(f"🎉 SUCESSO! Os endereços estão funcionando!")
            print(f"✅ O RO Tools deve conseguir ler os valores agora.")
            result = True
        elif success_count >= 1:
            print(f"⚠️ PARCIAL: Alguns endereços funcionando.")
            print(f"📝 Pode precisar de ajustes finos.")
            result = True
        else:
            print(f"❌ FALHA: Nenhum endereço válido encontrado.")
            print(f"🔧 Verifique se o jogo está rodando e os endereços estão corretos.")
            result = False
        
        pm.close_process()
        return result
        
    except Exception as e:
        print(f"❌ Erro ao conectar ao processo: {e}")
        print(f"💡 Tente executar como administrador.")
        return False

def test_specific_addresses():
    """Testa endereços específicos que você encontrou no Cheat Engine"""
    print("🎯 TESTE DOS ENDEREÇOS ABSOLUTOS DO CHEAT ENGINE\n")
    
    # Endereços que você encontrou funcionando no Cheat Engine
    ce_addresses = {
        "HP": 0x00E8E434,
        "Posição X": 0x00E77288,
        "Mapa": 0x00E89BD4, 
        "Job": 0x00E8AA50,
        "Chat": 0x00CE5B48
    }
    
    pid = find_rtales_process()
    if not pid:
        print("❌ Processo não encontrado!")
        return
    
    try:
        pm = pymem.Pymem()
        pm.open_process_from_id(pid)
        print(f"✅ Conectado ao processo (PID: {pid})")
        
        print(f"\n=== TESTANDO ENDEREÇOS ABSOLUTOS ===")
        print("(Estes são os endereços que funcionaram no Cheat Engine)")
        
        for name, address in ce_addresses.items():
            try:
                print(f"\n{name} (0x{address:08X}):")
                
                if name == "Mapa":
                    map_bytes = pm.read_bytes(address, 16)
                    map_name = map_bytes.split(b'\x00')[0].decode('ascii', errors='ignore')
                    print(f"  Valor: '{map_name}'")
                else:
                    value = pm.read_uint(address)
                    print(f"  Valor: {value}")
                    
            except Exception as e:
                print(f"  ❌ Erro: {e}")
        
        pm.close_process()
        
    except Exception as e:
        print(f"❌ Erro: {e}")

def main():
    print("🧪 TESTE DE ENDEREÇOS - VERSÃO COMPATÍVEL\n")
    
    print("="*60)
    print("OPÇÕES:")
    print("1 - Testar endereços convertidos (offsets relativos)")
    print("2 - Testar endereços absolutos do Cheat Engine")
    print("3 - Sair")
    print("="*60)
    
    choice = input("\nEscolha uma opção (1-3): ")
    
    if choice == "1":
        success = test_memory_simple()
        if success:
            print(f"\n🎯 PRÓXIMOS PASSOS:")
            print(f"1. Execute o RO Tools")
            print(f"2. Conecte ao processo rtales.bin")
            print(f"3. Teste as funcionalidades")
    elif choice == "2":
        test_specific_addresses()
    elif choice == "3":
        print("👋 Saindo...")
    else:
        print("❌ Opção inválida!")

if __name__ == "__main__":
    main()