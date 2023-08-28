registered_vehicles = {}
number_of_commands = int(input())
for x in range(number_of_commands):
    command = input().split()
    username = command[1]
    if "register" in command:
        license_plate_number = command[2]
        if username in registered_vehicles.keys():
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            registered_vehicles[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    else:
        if username not in registered_vehicles.keys():
            print(f"ERROR: user {username} not found")
        else:
            del registered_vehicles[username]
            print(f"{username} unregistered successfully")

for username, license_plate_number in registered_vehicles.items():
    print(f"{username} => {license_plate_number}")

