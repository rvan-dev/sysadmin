# Get a list of all services
$services = Get-WmiObject Win32_Service

# Initialize an empty hash table to store service account usage
$serviceAccounts = @{}

# Loop through each service
foreach ($service in $services) {
    $account = $service.StartName

    # Check if the account is already in the hash table
    if ($serviceAccounts.ContainsKey($account)) {
        # Add the service name to the existing list for this account
        $serviceAccounts[$account] += ", " + $service.Name
    } else {
        # Create a new entry in the hash table for this account
        $serviceAccounts[$account] = $service.Name
    }
}

# Display the results
foreach ($account in $serviceAccounts.Keys) {
    Write-Host "Account: $account"
    Write-Host "Services: $($serviceAccounts[$account])"
    Write-Host ""
}
