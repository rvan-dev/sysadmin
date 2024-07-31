# Transfer custom roles between vSphere Server
How to export the Roles on a vSphere 7.0 Server and import them on another vSphere 
Software Required: PowerCLI

1. Export the Role you want from the original Server (export it to a file)  
`(Get-VIRole -name “Role Name”).ExtensionData.Privilege`

2. Import the Role onto the new System  
```
$Role = New-VIRole -Name "New Role Name"  
$privilege = Get-content C:\Scripts\Logs\ExtractedRole.txt  
$privilege | foreach {Set-VIRole -role $role -AddPrivilege (get-viprivilege -id $_) }
```
