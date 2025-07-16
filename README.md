
<div style="display:flex; align-items: center; gap: 1rem;">
  <img src="icon.ico"/>
  <span style="font-size: 40px; font-weight: bold;">RO - Tools</span>
</div>

## 📦 Download

Você pode baixar a versão mais recente do RO Tools clicando no botão abaixo:

[![Download](https://img.shields.io/badge/⬇️%20Download-RO__Tools__v1.6.1-blue?style=for-the-badge)](https://github.com/uniaodk/ro-tools/releases/download/v1.6.1/RO_Tools_1.6.1.zip)

### ⚠️ Atenção

Para que este programa funcione corretamente, é **necessário executá-lo como administrador**.

Sem privilégios administrativos, algumas funcionalidades podem não funcionar corretamente, como:

- Leitura de memória de outros processos  
- Simulação de teclas ou comandos no sistema  
- Acesso a janelas de outros aplicativos

> 💡 Clique com o botão direito no executável e selecione **"Executar como administrador"**.

## 🎮 Visão Geral

[Demonstrativo da Ferramenta](https://youtu.be/INusWjFhUrw)

Ferramenta de automação para jogadores de **Ragnarok Online** focada em buffs, uso de itens automáticos, execução de macros e habilidades.

O RO-Tools foi criado para facilitar a jogabilidade em servidores de Ragnarok Online (pré-renovação). Ele automatiza ações como uso de poções, buffs, macros e alternância de equipamentos com base em condições personalizadas.

### Componentes da Interface

#### 🔌 Processo

- Selecione o processo do jogo para ativar os eventos. O botão 🔁 (refresh) atualiza a lista de processos abertos.

#### 🔧 Abas

- **Início**: Painel de controle principal com eventos ativos.
- **Debug**: Tela para verificar se informações são consistentes
- **Links**: Acesso rápido a páginas úteis.
- **Configurações**: Ajustes da aplicação.

#### 🧪 Features

- **Potions**  
  Usa poções configuradas com base em percentual de HP e SP.

- **YGG**  
  Usa automaticamente sementes ou frutas de Yggdrasil ao atingir limiares críticos de HP/SP.

- **Itens de Buff**  
  Aplica consumíveis que fornecem efeitos de buff (ex: Poção de Concentração, Poção de Despertar).
  Pode ser configurado por tecla e tempo de recarga.

- **Itens para Curar Debuff**  
  Usa itens que removem efeitos negativos automaticamente (ex: Panaceia, Poção Verde).
  Pode ser configurado para remover tipos específicos de status (Silêncio, Cegueira, etc).

- **Asa de Mosca**  
  Configura uma tecla dedicada para o uso da Asa de Mosca, evitando conflito com o sistema de Auto Pot.
  Necessário devido à limitação do jogo de usar apenas um item por vez.

- **Skill Spawmmer**  
  Repetição de habilidades ofensivas.

- **Skill Buff**  
  Ativação periódica de buffs.

- **Equip. Buff**  
  Troca de equipamento para ativar efeitos.

- **Hotkey**  
  Execução de comandos por atalho.

- **Macro**  
  Sequência de ações automatizadas.

- **Auto-Teleport por ID de monstros**  
  Tele para encontrar os mobs automaticamente. Configure os IDs dos monstros e o sistema usará automaticamente a Asa de Mosca para encontrar algum deles.

- **Auto-Abracadabra**  
  Use a habilidade Abracadabra automaticamente com controle de tempo e cancelamento seguro. Ideal para invocação de MvP e domesticação de pets continua.

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

- **Skill Timer**  
  Configure o tempo que cada skill/item vai ser utilizado

- **Auto Commands**  
  Insere automaticamente comandos ou mensagens a ser exibida no chat

- **Avisos Sonoros**  
   Algumas features estão providas de avisos sonoros para identificar sua ativação

- **Utilizar Buffs e Items ao Atacar**  
   Evita se buffar quando não estiver atacando, voltando a se buffar quando utilizar uma Skill Spawmmer
---

## ⚙️ Configuração do servers.json

[Vídeo de configuração para um server](https://youtu.be/uHH97eWDVRE)

Funcionalidade de cada offset, caso queira não utilizar alguma feature conforme o offset, atribui o valor `0x0`

- [1] Dados que recupera do jogo  
- [2] O que irá funcionar no RO Tools

**hp_offset**:  
- [1] HP atual/max, SP atual/max e lista de Buffs (Ícones do lado direito)  
- [2] Auto Pot HP/SP/YGG, Stuffs, Debuff, Skill Buff e Equip Buff

**x_pos_offset**:
- [1] Posição do jogador no eixo X e Y  
- [2] Rédeas (Auto buffar quando andar X células)  e Auto Element (Com a posição do jogador fica fácil saber qual o monstro que está mais próximo do jogador)

**map_offset**:  
- [1] Nome do mapa atual  
- [2] Bloquear item em cidades e o Utilizar itens somente nos mapas definido (Identificar se o mapa condiz com os critérios)

**job_offset**:
- [1] Identificador da sprite da classe do jogador  
- [2] Auto sincroniza a classe no RO Tools para as configurações da classe (Único trabalho seria toda vez que trocar de classe, ter que trocar manualmente)

**chat_offset**:  
- [1] Identificar se o chat está aberto ou fechado  
- [2] Opções de esperar o chat fechar para continuar buffando ou forçar o fechamento via memória do jogo

**entity_list_offset**:
- [1] Listar todos monstros que aparecem na tela do jogador  
- [2] Auto Tele e Auto Element (Para funcionar corretamente precisa saber quais IDs do monstro aparecem nessa lista)

**abracadabra_address**:
- [1] Identificar o ID da última habilidade utilizada pelo abracadabra  
- [2] Auto Abracadabra (Sem essa informação a ferramenta não sabe quando ???? é do MVP,  utilizando infinitamente)


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
- PyQt5
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
