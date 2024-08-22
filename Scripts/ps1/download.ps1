$url       = 'https://nicelinkicoulddownloadfileswithwgetbutiusewindows~.~'
$outputdir = 'C:\Users\BOBER\Documents\'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12, [Net.SecurityProtocolType]::Tls11
$WebResponse = Invoke-WebRequest -Uri $url

$WebResponse.Links | Select-Object -ExpandProperty href -Skip 1 | ForEach-Object {
    Write-Host "Downloading file '$_'"
    $filePath = Join-Path -Path $outputdir -ChildPath $_
    $fileUrl  = '{0}/{1}' -f $url.TrimEnd('/'), $_
    Invoke-WebRequest -Uri $fileUrl -OutFile $filePath
}
