$main_key_name = "KEY_NAME_HERE"
$registry_path = "Registry::HKEY_CURRENT_USER\SOFTWARE\Classes\*\shell"

if(Test-Path $registry_path){
    $registry_key = [Microsoft.Win32.Registry]::CurrentUser.OpenSubKey("SOFTWARE\Classes\*\shell\", $true)
    $sub_keys = $registry_key.GetSubKeyNames()
    if($sub_keys -contains $main_key_name){
        $registry_key.DeleteSubKeyTree($main_key_name)
        Write-Host "Registry key(s) deleted" -ForeGroundColor White -BackgroundColor Green
    }
} else {
    Write-Host "Registry key not found" -ForeGroundColor White -BackgroundColor Red
}