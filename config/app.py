from config.icon import resource_path


APP_NAME = "RO - Tools"
APP_ICON = resource_path("assets/icon/icon.png")
APP_DELAY = 0.01
APP_MONITORING_DELAY = 0.2
APP_CBOX_WIDTH = 300
APP_WIDTH = 800
APP_HEIGHT = 600
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
"""
