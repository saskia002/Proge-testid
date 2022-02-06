#SingleInstance Force
#Persistent
#NoEnv
SetBatchLines, -1
Gosub, TrayMenu

TrayMenu:
	Menu, Tray, MainWindow
	Menu, Tray, NoStandard 
	Menu, Tray, DeleteAll 
	Menu, Tray, Add, Enable, Kohvi
	Menu, Tray, Add, Disable, Külm_kohvi
	Menu, Tray, Add
	Menu, Tray, Add, Exit, GuiClose
Return

Kohvi:
	kohvi_soe := 1
	Loop{
		Send, {F22}
		Sleep, 500 000
	}Until (kohvi_soe = 0)
return

Külm_kohvi:
	kohvi_soe := 0
return

^F12::
	kohvi_soe := 0
return

GuiClose: 
	ExitApp