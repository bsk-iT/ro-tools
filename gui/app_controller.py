from events.game import GAME
from game.jobs import NOVICE, Job
from service.config_file import CONFIG_FILE
from service.memory import MEMORY
from PyQt6.QtGui import QIcon
from config.icon import ICON_OFF, ICON_ON


class AppController:

    def __init__(self):
        self.process_name = None
        self.cbox_job = None
        self.sync_data(NOVICE)

    def sync_data(self, job):
        self.job: Job = job
        self.spawn_skills = CONFIG_FILE.get_spawn_skills(self.job)

    def on_change_process(self, cbox, index, process_options) -> None:
        if not process_options:
            MEMORY.process.close_process()
            return
        process = process_options[index]
        self.process_name = process["name"]
        MEMORY.update_process(self.process_name, process["pid"])
        cbox.focusNextChild()

    def on_change_job(self, cbox, index):
        job = cbox.model.item(index, 0).data()
        self.sync_data(job)
        cbox.updated_job.emit(job)

    def on_togle_monitoring(self, status_toggle, value=None):
        if not MEMORY.is_valid():
            return
        if value is None:
            status_toggle.toggle()
            return
        GAME.start() if status_toggle.isChecked() else GAME.stop()
        status_toggle.setIcon(QIcon(ICON_ON if value else ICON_OFF))


APP_CONTROLLER = AppController()
