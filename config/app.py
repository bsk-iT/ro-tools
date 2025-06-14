from config.icon import resource_path


APP_NAME = "RO - Tools"
APP_ICON = resource_path("assets/icon/icon.png")
APP_DELAY = 0.01
APP_MONITORING_DELAY = 0.2
APP_CBOX_WIDTH = 250
APP_WIDTH = 1200
APP_HEIGHT = 570
APP_ICON_SIZE = 32
APP_MIN_DELAY = 0.01
APP_MAX_DELAY = 60
APP_FONT = resource_path("assets/font/JetBrainsMono-Regular.ttf")
APP_FONT_SIZE = 10
APP_STYLE = """
    #painel {
        border: 1px solid gray;
        padding: 16px;
        border-radius: 8px;
    }
    
    #status-btn {
        border: none;
        background-color: transparent;
    }
    
    #skill_inputs {
        border-bottom: 1px solid gray;
    }
    
    #attack_1, #defense_1 {
        color: rgb(72, 133, 237);
    }
    
    #attack_2, #defense_2 {
        color: rgb(123, 104, 238);
    }
    
    #attack_3, #defense_3 {
        color: rgb(199, 80, 255);
    }
    
    #attack_4, #defense_4 {
        color: rgb(255, 99, 171);
    }
"""
