"""
Script para testar e corrigir endereços de memória do RO Tools
"""
import json
import os

def check_current_config():
    """Verifica a configuração atual"""
    print("=== VERIFICAÇÃO DA CONFIGURAÇÃO ATUAL ===\n")
    
    try:
        with open("servers.json", "r", encoding="utf-8") as f:
            servers_data = json.load(f)
        
        if "rtales.bin" in servers_data:
            config = servers_data["rtales.bin"]
            print("Configuração atual para rtales.bin:")
            print(f"  HP Offset: {config.get('hp_offset', 'NÃO DEFINIDO')}")
            print(f"  X Position Offset: {config.get('x_pos_offset', 'NÃO DEFINIDO')}")
            print(f"  Map Offset: {config.get('map_offset', 'NÃO DEFINIDO')}")
            print(f"  Job Offset: {config.get('job_offset', 'NÃO DEFINIDO')}")
            print(f"  Chat Offset: {config.get('chat_offset', 'NÃO DEFINIDO')}")
            print(f"  Entity List Offset: {config.get('entity_list_offset', 'NÃO DEFINIDO')}")
            print(f"  Abracadabra Address: {config.get('abracadabra_address', 'NÃO DEFINIDO')}")
            
            return config
        else:
            print("❌ Configuração para 'rtales.bin' não encontrada!")
            return None
            
    except FileNotFoundError:
        print("❌ Arquivo servers.json não encontrado!")
        return None
    except json.JSONDecodeError:
        print("❌ Erro ao ler servers.json - arquivo corrompido!")
        return None

def convert_cheat_engine_addresses():
    """Ajuda a converter endereços do Cheat Engine para offsets relativos"""
    print("\n=== CONVERSÃO DE ENDEREÇOS DO CHEAT ENGINE ===\n")
    
    print("📋 INSTRUÇÕES:")
    print("1. Abra o Cheat Engine")
    print("2. Conecte ao processo rtales.bin")
    print("3. No Cheat Engine, clique com o botão direito no processo")
    print("4. Selecione 'Memory View' ou 'Visualizar Memória'")
    print("5. Anote o endereço base do módulo principal (geralmente o primeiro)")
    print("6. Para cada valor que você encontrou, calcule: Endereço_Encontrado - Base_Address")
    
    print("\nExemplo:")
    print("  Base Address: 0x00400000")
    print("  Endereço do HP: 0x00E8E434")
    print("  Offset = 0x00E8E434 - 0x00400000 = 0x00A8E434")
    
    base_address_input = input("\nDigite o Base Address do módulo (ex: 0x00400000): ")
    
    if not base_address_input:
        print("❌ Base address não fornecido.")
        return
    
    try:
        base_address = int(base_address_input, 16)
        print(f"✅ Base Address: 0x{base_address:08X}")
        
        addresses_to_convert = [
            ("HP", "hp_offset"),
            ("Posição X", "x_pos_offset"), 
            ("Mapa", "map_offset"),
            ("Job", "job_offset"),
            ("Chat", "chat_offset"),
            ("Lista de Entidades", "entity_list_offset")
        ]
        
        new_config = {}
        
        for name, key in addresses_to_convert:
            address_input = input(f"\nEndereço do {name} no Cheat Engine (ou 'skip'): ")
            
            if address_input.lower() == 'skip':
                continue
                
            try:
                absolute_address = int(address_input, 16)
                offset = absolute_address - base_address
                
                if offset >= 0:
                    new_config[key] = f"0x{offset:08X}"
                    print(f"✅ Offset calculado: 0x{offset:08X}")
                else:
                    print(f"❌ Offset negativo: 0x{offset:08X} - verifique o base address")
                    
            except ValueError:
                print(f"❌ Endereço inválido: {address_input}")
        
        if new_config:
            print("\n=== NOVOS OFFSETS CALCULADOS ===")
            for key, value in new_config.items():
                print(f"{key}: {value}")
            
            update = input("\nDeseja atualizar o servers.json? (s/n): ")
            if update.lower() in ['s', 'sim', 'y', 'yes']:
                update_servers_config(new_config)
        
    except ValueError:
        print(f"❌ Base address inválido: {base_address_input}")

def update_servers_config(new_offsets):
    """Atualiza a configuração no servers.json"""
    try:
        # Fazer backup
        if os.path.exists("servers.json"):
            with open("servers.json", "r", encoding="utf-8") as f:
                backup_data = f.read()
            with open("servers_backup.json", "w", encoding="utf-8") as f:
                f.write(backup_data)
            print("💾 Backup criado: servers_backup.json")
        
        # Carregar configuração atual
        with open("servers.json", "r", encoding="utf-8") as f:
            servers_data = json.load(f)
        
        # Atualizar offsets
        if "rtales.bin" not in servers_data:
            servers_data["rtales.bin"] = {}
        
        for key, value in new_offsets.items():
            servers_data["rtales.bin"][key] = value
        
        # Salvar
        with open("servers.json", "w", encoding="utf-8") as f:
            json.dump(servers_data, f, indent=2, ensure_ascii=False)
        
        print("✅ Configuração atualizada com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro ao atualizar configuração: {e}")

def manual_offset_input():
    """Permite inserir offsets manualmente"""
    print("\n=== INSERÇÃO MANUAL DE OFFSETS ===\n")
    
    print("Digite os offsets que você calculou manualmente:")
    print("Formato: 0x00000000 (ou deixe vazio para pular)")
    
    offsets = [
        ("HP Offset", "hp_offset"),
        ("X Position Offset", "x_pos_offset"),
        ("Map Offset", "map_offset"), 
        ("Job Offset", "job_offset"),
        ("Chat Offset", "chat_offset"),
        ("Entity List Offset", "entity_list_offset"),
        ("Abracadabra Address", "abracadabra_address")
    ]
    
    new_config = {}
    
    for name, key in offsets:
        value = input(f"{name}: ")
        if value.strip():
            # Validar formato hexadecimal
            try:
                int(value, 16)  # Teste se é hex válido
                new_config[key] = value
            except ValueError:
                print(f"❌ Valor inválido para {name}: {value}")
    
    if new_config:
        print("\n=== OFFSETS INSERIDOS ===")
        for key, value in new_config.items():
            print(f"{key}: {value}")
        
        update = input("\nDeseja salvar estes offsets? (s/n): ")
        if update.lower() in ['s', 'sim', 'y', 'yes']:
            update_servers_config(new_config)

def main():
    print("🔧 RO TOOLS - CONFIGURADOR DE ENDEREÇOS DE MEMÓRIA\n")
    
    # Verificar configuração atual
    current_config = check_current_config()
    
    if not current_config:
        print("\n❌ Não foi possível carregar a configuração atual.")
        return
    
    print("\n" + "="*50)
    print("OPÇÕES:")
    print("1 - Converter endereços do Cheat Engine")
    print("2 - Inserir offsets manualmente")
    print("3 - Sair")
    print("="*50)
    
    choice = input("\nEscolha uma opção (1-3): ")
    
    if choice == "1":
        convert_cheat_engine_addresses()
    elif choice == "2":
        manual_offset_input()
    elif choice == "3":
        print("👋 Saindo...")
    else:
        print("❌ Opção inválida!")

if __name__ == "__main__":
    main()