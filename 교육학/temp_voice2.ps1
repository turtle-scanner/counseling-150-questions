
 = 'HKLM:\SOFTWARE\Microsoft\Speech\Voices\Tokens'
if (Test-Path ) {
    Get-ChildItem  | ForEach-Object { .PSChildName }
}
 = 'HKLM:\SOFTWARE\Microsoft\Speech_OneCore\Voices\Tokens'
if (Test-Path ) {
    Get-ChildItem  | ForEach-Object { .PSChildName }
}
