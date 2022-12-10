# Specify the command to execute
$command = "iwr -useb https://christitus.com/win | iex"

# Execute the command
Invoke-Expression $command
