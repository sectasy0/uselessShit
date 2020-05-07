$iPID = WinGetProcess(WinGetTitle(GUICtrlRead($pidlist)))
$hMem = _MemoryOpen($iPID)
$baseAddr = _MemoryModuleGetBaseAddress($iPID, "ots.exe") + 0x004D2190
Local $aOffset[2]
$aOffset[0] = 0
$aOffset[1] = 0x330
Global $CurrentHp1 = _MemoryPointerRead($baseAddr, $hMem, $aOffset, "double")
_MemoryClose($hMem)