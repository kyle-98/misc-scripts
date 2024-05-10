$key_name = "KEY_NAME_HERE"
$path_to_icon = "PATH_HERE"
$context_menu_name = "RIGHT_CLICK_NAME_HERE"
$payload = "`"EXE_PATH_HERE`"" + "`"%1`""

try {
    [Microsoft.Win32.Registry]::SetValue("HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\$key_name", "", $context_menu_name, 1)
    [Microsoft.Win32.Registry]::SetValue("HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\$key_name", "Icon", $path_to_icon, 1)
    [Microsoft.Win32.Registry]::SetValue("HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell\$key_name\command", "", $payload, 1)
    Write-Host "Successfully created $key_name" -ForegroundColor White -BackgroundColor Green
} catch {
    Write-Host "Failed to create $key_name" -ForegroundColor White -BackgroundColor Red
}
