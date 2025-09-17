"""
Script para converter endereços absolutos do Cheat Engine para offsets relativos
"""
import json
import os

def convert_cheat_engine_addresses():
    """Converte os endereços do Cheat Engine para offsets"""
    print("🔧 CONVERSOR DE ENDEREÇOS DO CHEAT ENGINE\n")
    
    # Endereços que você encontrou no Cheat Engine
    cheat_engine_addresses = {
        "hp_offset": "0x00E8E434",        # HP: 755
        "x_pos_offset": "0x00E77288",     # Posição: 156  
        "map_offset": "0x00E89BD4",       # Mapa: "prontera"
        "job_offset": "0x00E8AA50",       # Job: 5
        "chat_offset": "0x00CE5B48",      # Chat: 0
        "entity_list_offset": "0x007F1FAC"  # Mantendo o valor atual
    }
    
    print("Endereços encontrados no Cheat Engine:")
    for key, address in cheat_engine_addresses.items():
        print(f"  {key}: {address}")
    
    # Base address típico para executáveis Windows
    # Vamos tentar alguns valores comuns
    possible_base_addresses = [
        0x00400000,  # Base address padrão mais comum
        0x00010000,  # Alternativa comum
        0x00000000,  # Se os endereços já são offsets
    ]
    
    print(f"\n=== TESTANDO DIFERENTES BASE ADDRESSES ===")
    
    for base_addr in possible_base_addresses:
        print(f"\nTestando Base Address: 0x{base_addr:08X}")
        
        converted_offsets = {}
        all_valid = True
        
        for key, addr_str in cheat_engine_addresses.items():
            addr = int(addr_str, 16)
            offset = addr - base_addr
            
            # Verificar se o offset é razoável (positivo e não muito grande)
            if 0 <= offset <= 0x10000000:  # 256MB limite
                converted_offsets[key] = f"0x{offset:08X}"
                print(f"  ✅ {key}: 0x{offset:08X}")
            else:
                print(f"  ❌ {key}: 0x{offset:08X} (inválido)")
                all_valid = False
                break
        
        if all_valid:
            print(f"\n🎯 BASE ADDRESS VÁLIDO ENCONTRADO: 0x{base_addr:08X}")
            
            # Mostrar comparação com valores atuais
            print(f"\n=== COMPARAÇÃO COM CONFIGURAÇÃO ATUAL ===")
            try:
                with open("servers.json", "r", encoding="utf-8") as f:
                    current_config = json.load(f)["rtales.bin"]
                
                for key, new_value in converted_offsets.items():
                    current_value = current_config.get(key, "NÃO DEFINIDO")
                    status = "✅ IGUAL" if current_value == new_value else "🔄 DIFERENTE"
                    print(f"  {key}:")
                    print(f"    Atual:  {current_value}")
                    print(f"    Novo:   {new_value} {status}")
                
            except:
                print("❌ Erro ao ler configuração atual")
            
            # Perguntar se quer atualizar
            print(f"\n" + "="*60)
            update = input("Deseja atualizar o servers.json com estes novos offsets? (s/n): ")
            
            if update.lower() in ['s', 'sim', 'y', 'yes']:
                update_servers_json(converted_offsets, base_addr)
            
            return converted_offsets
    
    print("\n❌ Nenhum base address válido encontrado automaticamente.")
    print("Você pode tentar inserir o base address manualmente.")
    
    manual_base = input("\nDigite o base address manualmente (ex: 0x00400000) ou Enter para sair: ")
    if manual_base.strip():
        try:
            base_addr = int(manual_base, 16)
            print(f"\nUsando base address manual: 0x{base_addr:08X}")
            
            converted_offsets = {}
            for key, addr_str in cheat_engine_addresses.items():
                addr = int(addr_str, 16)
                offset = addr - base_addr
                converted_offsets[key] = f"0x{offset:08X}"
                print(f"  {key}: 0x{offset:08X}")
            
            update = input("\nDeseja salvar estes offsets? (s/n): ")
            if update.lower() in ['s', 'sim', 'y', 'yes']:
                update_servers_json(converted_offsets, base_addr)
                
            return converted_offsets
            
        except ValueError:
            print("❌ Base address inválido!")
    
    return None

def update_servers_json(new_offsets, base_address):
    """Atualiza o servers.json com os novos offsets"""
    try:
        # Fazer backup
        if os.path.exists("servers.json"):
            with open("servers.json", "r", encoding="utf-8") as f:
                backup_data = f.read()
            backup_name = "servers_backup.json"
            with open(backup_name, "w", encoding="utf-8") as f:
                f.write(backup_data)
            print(f"💾 Backup criado: {backup_name}")
        
        # Carregar e atualizar configuração
        with open("servers.json", "r", encoding="utf-8") as f:
            servers_data = json.load(f)
        
        if "rtales.bin" not in servers_data:
            servers_data["rtales.bin"] = {}
        
        # Atualizar offsets
        for key, value in new_offsets.items():
            old_value = servers_data["rtales.bin"].get(key, "NÃO DEFINIDO")
            servers_data["rtales.bin"][key] = value
            print(f"✅ Atualizado {key}: {old_value} → {value}")
        
        # Salvar arquivo atualizado
        with open("servers.json", "w", encoding="utf-8") as f:
            json.dump(servers_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n🎉 SUCESSO!")
        print(f"📁 Arquivo servers.json atualizado!")
        print(f"🏠 Base Address usado: 0x{base_address:08X}")
        print(f"💾 Backup salvo em: servers_backup.json")
        
        print(f"\n📋 PRÓXIMOS PASSOS:")
        print(f"1. Reinicie o RO Tools")
        print(f"2. Conecte ao processo rtales.bin")
        print(f"3. Teste se os valores estão sendo lidos corretamente")
        
    except Exception as e:
        print(f"❌ Erro ao atualizar servers.json: {e}")

def show_current_vs_cheat_engine():
    """Mostra comparação entre config atual e endereços do Cheat Engine"""
    print("=== COMPARAÇÃO: CONFIGURAÇÃO ATUAL vs CHEAT ENGINE ===\n")
    
    # Endereços do Cheat Engine
    ce_addresses = {
        "hp_offset": "0x00E8E434",
        "x_pos_offset": "0x00E77288", 
        "map_offset": "0x00E89BD4",
        "job_offset": "0x00E8AA50",
        "chat_offset": "0x00CE5B48"
    }
    
    try:
        with open("servers.json", "r", encoding="utf-8") as f:
            current_config = json.load(f)["rtales.bin"]
        
        print("Endereços do Cheat Engine (absolutos):")
        for key, addr in ce_addresses.items():
            current = current_config.get(key, "NÃO DEFINIDO")
            print(f"  {key}:")
            print(f"    Cheat Engine: {addr}")
            print(f"    Config Atual: {current}")
            print()
            
    except Exception as e:
        print(f"❌ Erro ao ler configuração: {e}")

def main():
    print("🎯 CONVERSOR DE ENDEREÇOS DO CHEAT ENGINE PARA RO TOOLS\n")
    
    print("📊 Endereços identificados na sua imagem do Cheat Engine:")
    print("  HP (00E8E434): 755 ✅")
    print("  Posição (00E77288): 156 ✅") 
    print("  Mapa (00E89BD4): 'prontera' ✅")
    print("  Job (00E8AA50): 5 ✅")
    print("  Chat (00CE5B48): 0 ✅")
    
    print("\n" + "="*60)
    print("OPÇÕES:")
    print("1 - Converter endereços automaticamente")
    print("2 - Mostrar comparação com configuração atual")
    print("3 - Sair")
    print("="*60)
    
    choice = input("\nEscolha uma opção (1-3): ")
    
    if choice == "1":
        convert_cheat_engine_addresses()
    elif choice == "2":
        show_current_vs_cheat_engine()
    elif choice == "3":
        print("👋 Saindo...")
    else:
        print("❌ Opção inválida!")

if __name__ == "__main__":
    main()