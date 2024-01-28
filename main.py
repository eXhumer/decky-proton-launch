from asyncio import sleep
from subprocess import Popen
from typing import Type

from decky_plugin import DECKY_PLUGIN_DIR


class Plugin:
    BACKEND_PROC: Popen[bytes] | None = None

    @staticmethod
    async def _main(cls: Type["Plugin"]):
        cls.BACKEND_PROC = Popen([f"{DECKY_PLUGIN_DIR}/bin/backend"])

        while True:
            await sleep(1)

    @staticmethod
    async def _unload(cls: Type["Plugin"]):
        if cls.BACKEND_PROC is not None:
            cls.BACKEND_PROC.kill()
            cls.BACKEND_PROC = None

    @staticmethod
    async def reload_backend(cls: Type["Plugin"]):
        await cls._unload()
        cls.BACKEND_PROC = Popen([f"{DECKY_PLUGIN_DIR}/bin/backend"])
