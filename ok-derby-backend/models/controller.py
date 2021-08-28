import time
import logging
import threading
from typing import Optional, Callable

logger = logging.getLogger(__name__)


class missionController:
    FLAG = False
    okderby = None
    watch_thread = threading.Thread()
    auto_derby_thread = threading.Thread()

    @classmethod
    def init(cls, func: Callable):
        cls.okderby = func
        cls.watch_thread = threading.Thread(target=cls.watch).start()

    @classmethod
    def watch(cls):
        while True:
            logger.debug(f"auto_derby_thread: {cls.auto_derby_thread.is_alive()} FLAG: {cls.FLAG}")
            if not cls.auto_derby_thread.is_alive():
                cls.FLAG = False
            time.sleep(3)

    @classmethod
    def start_mission(cls,
                      job_name: str,
                      plugins: str,
                      adb_address: Optional[str] = None) -> None:
        cls.FLAG = True
        cls.auto_derby_thread = threading.Thread(target=cls.okderby, args=(job_name, plugins, adb_address))
        cls.auto_derby_thread.start()

    @classmethod
    def stop_mission(cls) -> None:
        cls.FLAG = False

    @classmethod
    def get_mission_status(cls):
        if cls.auto_derby_thread.is_alive():
            return "running"
        else:
            return "stopped"
