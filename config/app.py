from config.icon import resource_path


APP_NAME = "RO - Tools"
APP_ICON = resource_path("assets/icon/icon.png")
APP_ACTION_DELAY = 10
APP_MONITORING_DELAY = 100
APP_WIDTH = 800
APP_HEIGHT = 600
APP_ICON_SIZE = 32
APP_MIN_DELAY = 10
APP_MAX_DELAY = 60000
APP_FONT = resource_path("assets/font/JetBrainsMono-Regular.ttf")
APP_FONT_SIZE = 10
APP_MAP_CRITERIA = ["BG", "WoE", "PvP"]
APP_STYLE = """
    #painel {
        border: 1px solid gray;
        padding: 16px;
        border-radius: 8px;
    }
"""