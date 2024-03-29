from asyncio import sleep
from subprocess import Popen
from sys import version_info as python_version
from typing import Type, Union

from decky_plugin import DECKY_PLUGIN_DIR, logger


class Plugin:
    """
    This is a Decky plugin that starts a backend process and keeps it running.
    """

    BACKEND_PATH = f"{DECKY_PLUGIN_DIR}/bin/backend"
    BACKEND_PROC: Union[Popen[bytes], None] = None

    @staticmethod
    async def _main(cls: Type["Plugin"]):
        """
        Plugin entry hook.
        """

        logger.debug("Backend Python Version: " +
                     f"{python_version.major}.{python_version.minor}")

        logger.info("Starting backend process...")

        cls.BACKEND_PROC = Popen([cls.BACKEND_PATH])

        while True:
            await sleep(1)

    @staticmethod
    async def _unload(cls: Type["Plugin"]):
        """
        Plugin unload hook.
        """

        if cls.BACKEND_PROC is not None:
            cls.BACKEND_PROC.kill()
            cls.BACKEND_PROC = None
