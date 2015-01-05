Set WshShell = CreateObject("WScript.Shell")
cmds=WshShell.RUN("Interface.exe", 0, True)
Set WshShell = Nothing