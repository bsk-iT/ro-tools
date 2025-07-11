
<h1 style="display:flex; align-items: center; gap: 1rem;">
  <img src="icon.ico"/>
  <span>RO - Tools</span>
</h1>

---

## 📦 Download

Você pode baixar a versão mais recente do RO Tools clicando no botão abaixo:

[![Download](https://img.shields.io/badge/⬇️%20Download-RO__Tools__v1.3.1-blue?style=for-the-badge)](https://github.com/uniaodk/ro-tools/releases/download/v1.3.1/RO_Tools_1.3.1.zip)

### ⚠️ Atenção

Para que este programa funcione corretamente, é **necessário executá-lo como administrador**.

Sem privilégios administrativos, algumas funcionalidades podem não funcionar corretamente, como:

- Leitura de memória de outros processos  
- Simulação de teclas ou comandos no sistema  
- Acesso a janelas de outros aplicativos

> 💡 Clique com o botão direito no executável e selecione **"Executar como administrador"**.

## 🎮 Visão Geral

Ferramenta de automação para jogadores de **Ragnarok Online** focada em buffs, uso de itens automáticos, execução de macros e habilidades.

O RO-Tools foi criado para facilitar a jogabilidade em servidores de Ragnarok Online (pré-renovação). Ele automatiza ações como uso de poções, buffs, macros e alternância de equipamentos com base em condições personalizadas.

## 📸 Vídeos

- [Demonstrativo da Ferramenta](https://youtu.be/INusWjFhUrw)
- [Configuração do arquivo servers.json](https://youtu.be/uHH97eWDVRE)

### Componentes da Interface

#### 🔌 Processo

- Selecione o processo do jogo para ativar os eventos. O botão 🔁 (refresh) atualiza a lista de processos abertos.

#### 🔧 Abas

- **Início**: Painel de controle principal com eventos ativos.
- **Links**: Acesso rápido a páginas úteis.
- **Configurações**: Ajustes da aplicação.

#### 🧪 Auto Item

Automatiza o uso de itens com base em condições personalizadas. Pode ser usado para restaurar HP/SP, aplicar efeitos de buff ou remover debuffs automaticamente. Inclui também configurações para itens especiais como Yggdrasil e Asa de Mosca.

- 💉 **Potions**
  - Usa poções configuradas com base em percentual de HP e SP.
  - Suporte a múltiplas teclas configuráveis.

- 🌿 **YGG**
  - Usa automaticamente sementes ou frutas de Yggdrasil ao atingir limiares críticos de HP/SP.

- 🧪 **Itens de Buff**
  - Aplica consumíveis que fornecem efeitos de buff (ex: Poção de Concentração, Poção de Despertar).
  - Pode ser configurado por tecla e tempo de recarga.

- 💀 **Itens para Curar Debuff**
  - Usa itens que removem efeitos negativos automaticamente (ex: Panaceia, Poção Verde).
  - Pode ser configurado para remover tipos específicos de status (Silêncio, Cegueira, etc).

- 🦋 **Asa de Mosca**
  - Configura uma tecla dedicada para o uso da Asa de Mosca, evitando conflito com o sistema de Auto Pot.
  - Necessário devido à limitação do jogo de usar apenas um item por vez.

#### 🧰 Job Tools

Ferramentas específicas por profissão.

- **Skill Spawmmer**: Repetição de habilidades ofensivas.
- **Skill Buff**: Ativação periódica de buffs.
- **Equip. Buff**: Troca de equipamento para ativar efeitos.
- **Hotkey**: Execução de comandos por atalho.
- **Macro**: Sequência de ações automatizadas.

---

#### ✨ Novas funcionalidades

- **Auto-Teleport por ID de monstros**  
  Tele para encontrar os mobs automaticamente. Configure os IDs dos monstros e o sistema usará automaticamente a Asa de Mosca para encontrar algum deles.

- **Auto-Abracadabra**  
  Use a habilidade Abracadabra automaticamente com controle de tempo e cancelamento seguro. Ideal para invocação contínua.

- **Links úteis personalizados por servidor**  
  Acesse ferramentas específicas do seu servidor (como sites de rankings, market, wiki, etc.) diretamente pelo app, com links configuráveis.
  
- **Auto Switch para Elemento**  
  Configure os IDs do monstros para que altere automaticamente os melhores equipes conforme a situação.

- **Suporte com driver Intereception**  
  Alguns jogos impede a simulação do clique dentro do jogo, o que requer algo mais robusto para funcionar.

- **Auto Rédea**  
  Utiliza rédea automaticamente quando andar X células.

- **Block Pantano dos Mortos**  
  Evita utilizar certas skill quando estiver na área do Pantano dos Mortos

---

## ⚙️ Eventos Disponíveis

Abaixo a lista de eventos definidos no sistema:

| Evento              | Descrição |
|---------------------|-----------|
| `auto_item_buff`    | Aplica itens que fornecem efeitos de buff automaticamente. |
| `auto_item_debuff`  | Usa itens que removem debuffs automaticamente. |
| `auto_pot_hp`       | Usa potions com base em percentual de HP. |
| `auto_pot_sp`       | Usa potions com base em percentual de SP. |
| `auto_ygg`          | Usa sementes ou frutas de Yggdrasil conforme necessário. |
| `hotkey_event`      | Executa ações com base em teclas de atalho personalizadas. |
| `macro_event`       | Executa sequências personalizadas de ações (macros). |
| `skill_buff`        | Aplica automaticamente habilidades de buff conforme a lista de buffs do personagem. |
| `skill_equip`       | Troca de equipamento com base na ativação de skills. |
| `skill_spawmmer`    | Automatiza o uso de habilidades ofensivas. |
| `base_event`        | Classe base que define estrutura comum a todos os eventos. |
| `game_event`        | Controla execução e sincronização dos eventos com o jogo. |

---

## 📁 Estrutura de Pastas

```
ro-tools/
├── assets/ # Ícones e imagens de habilidades
├── config/ # Arquivos de configuração e ícones
├── events/ # Eventos principais que controlam ações automatizadas
├── game/ # Estruturas e lógica de jogo (jobs, buffs, etc)
├── gui/ # Interface gráfica (Qt)
├── service/ # Serviços como teclado, mouse, memória
├── tests/ # Testes automatizados
└── util/ # Utilitários diversos
```

## 🧩 Requisitos para o modo de simulação `"driver"` (Interception)

Para que o modo `"driver"` funcione corretamente — utilizado para simular teclas e cliques de forma compatível com jogos que bloqueiam eventos simulados comuns (ex: `SendInput`, `keybd_event`) — é necessário instalar o driver **Interception** e sua respectiva biblioteca Python.

### 📦 Instalação do driver Interception

1. Baixe o driver a partir do repositório oficial:
   [https://github.com/oblitum/Interception](https://github.com/oblitum/Interception)

2. Extraia o conteúdo do arquivo `.zip`.

3. Execute o instalador via terminal com permissão de administrador:

  ```bash
   install-interception.exe /install
  ```
4. Reinicie o computador após a instalação (recomendado).

⚠️ Este driver atua em nível de kernel. É necessário permissão de administrador para funcionar corretamente.

## 🛠 Requisitos

- Python 3.12+
- PyQt6
- pywin32
- keyboard
- pymem
- psutil
- interception-python

Instale as dependências com:

```bash
pip install -r requirements.txt
```

## 🚀 Execução

Para iniciar a aplicação, execute o seguinte comando:

```bash
python main.py
```

---

## 🙏 Agradecimentos e Projeto Base

Este projeto foi desenvolvido com base no excelente trabalho realizado pelo [4RTools](https://github.com/4RTools/4RTools).

Muitos dos conceitos, estruturas e ideias iniciais foram inspirados ou adaptados a partir desse projeto.  
Agradecemos à comunidade do 4RTools por tornar seu código aberto e servir como referência para a evolução de ferramentas voltadas ao Ragnarok Online.

> Este repositório visa expandir e adaptar funcionalidades específicas para o cenário **pré-renovação**, com foco em automações personalizadas e extensibilidade do sistema de eventos.

## ⚠️ Aviso Legal

Esta ferramenta foi desenvolvida para fins educacionais e uso pessoal.

O uso deste software em servidores oficiais de Ragnarok Online pode violar os termos de serviço do jogo.  
**Utilize por sua conta e risco.**
