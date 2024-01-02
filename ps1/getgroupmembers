# Import the Active Directory module
Import-Module ActiveDirectory

# Define the list of AD group names
$groupNames = @("GROUPNAME", "GROUPNAME2") # Add your group names here

# Function to get and display members of a group
function Get-AndDisplayGroupMembers($groupName) {
    Write-Host "Members of group $groupName:"
    $groupMembers = Get-ADGroupMember -Identity $groupName
    foreach ($member in $groupMembers) {
        Write-Host "`t$member"
    }
}

# Process each group
foreach ($groupName in $groupNames) {
    Get-AndDisplayGroupMembers -groupName $groupName
    Write-Host ""
}
