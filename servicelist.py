import subprocess

def get_startup_services():
    startup_services = []

    # Execute the wmic command to retrieve the list of services
    command = 'wmic service where (StartMode="Auto" or StartMode="DelayedAuto") get Name'
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Process the output and extract the service names
    output_lines = result.stdout.split('\n')
    for line in output_lines[1:-2]:  # Exclude header and empty lines at the end
        service_name = line.strip()
        startup_services.append(service_name)
        
    return startup_services

# Get the list of startup services
startup_services = get_startup_services()

# Write the list of startup services to a notepad file
filename = 'startup_services.txt'
with open(filename, 'w') as file:
    for service in startup_services:
        file.write(service + '\n')

print(f"List of startup services saved to '{filename}'.")
