#!/usr/bin/python3
from typing import Callable, NoReturn
from pathlib import Path

class Commands(object):
    def __init__(self):
        from os import system
        self.cmd_extr: Callable[[str,], int] = system

    def fileExists(self, path: str) -> bool:
        pth = Path(path)
        return pth.exists()

    def createFile(self, path: str, mode=0o664) -> None:
        pth = Path(path)
        pth.touch(mode=mode)

    def chmod(self, mode: str, filename: str) -> None:
        self.cmd_extr("chmod {mode} {filename}".format(mode=mode, filename=filename))

    def makeFileExecutable(self, filename: str) -> None:
        self.chmod("+x", filename)

    def execFileNoArgs(self, filename: str) -> None:
        self.cmd_extr("./{filename}".format(filename=filename))

    def execFile(self, filename: str, *args, **kwargs) -> NoReturn:
        raise NotImplementedError

    def execRawCommamd(self, rawdata: str) -> None:
        self.cmd_extr(rawdata)

class SetupContainerMixin(object):
    def __init__(self):
        self.cmd_proxy = Commands()

    def installDeps(self) -> None:
        self.cmd_proxy.execFileNoArgs("install_deps.sh")

    def buildContainer(self) -> None:
        self.cmd_proxy.execFileNoArgs("buildcont.sh")

    def setupContainer(self):
        self.installDeps()
        self.buildContainer()
        self.cmd_proxy.createFile(".shd")

class dockerContainer(SetupContainerMixin):
    def __init__(self, name: str = "nameless") -> None:
        super().__init__()
        self.name = name
    def run(self) -> None:
        if not(self.cmd_proxy.fileExists(".shd")):
            self.setupContainer()
        self.cmd_proxy.execFileNoArgs("rundocker.sh")

def main():
    container = dockerContainer("bot")
    container.run()
    print("\x1b[42mFor attach container try `docker attach $id` with this id ↑\x1b[49m\n") 
    print("\x1b[42mFor detach use the escape sequence Ctrl+P followed by Ctrl+Q.\x1b[49m")


if __name__ == "__main__": main()
