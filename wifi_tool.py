import subprocess
import threading
import os
import platform
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(Fore.RED + f"Error: {result.stderr.strip()}")
            return None
    except Exception as e:
        print(Fore.RED + f"Exception: {str(e)}")
        return None


# function to show avalable networks
def show_available_networks():
    print(Fore.CYAN + "Scanning for available WiFi networks...")
    output = run_command("netsh wlan show networks mode=bssid")
    if output:
        networks = []
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("SSID"):
                ssid = line.split(":")[1].strip()
                networks.append({"SSID": ssid})
            elif line.startswith("BSSID"):
                networks[-1]["BSSID"] = line.split(":")[1].strip()
            elif line.startswith("Signal"):
                networks[-1]["Signal"] = line.split(":")[1].strip()
            elif line.startswith("Network type"):
                networks[-1]["Type"] = line.split(":")[1].strip()

        if networks:
            print(Fore.GREEN + tabulate(networks, headers="keys", tablefmt="pretty"))
        else:
            print(Fore.RED + "No networks found.")
        return networks
    return []

# function to connect to network
def connect_to_network():
    networks = show_available_networks()
    if not networks:
        print(Fore.RED + "No networks available to connect.")
        return

    print(Fore.CYAN + "Select a network to connect:")
    for i, network in enumerate(networks):
        print(f"{i + 1}. {network['SSID']}")

    choice = input(Fore.YELLOW + "Enter the number of the network: ")
    try:
        choice = int(choice) - 1
        if 0 <= choice < len(networks):
            ssid = networks[choice]["SSID"]
            print(Fore.CYAN + f"Checking if password is saved for {ssid}...")
            profiles = run_command(f"netsh wlan show profile name=\"{ssid}\" key=clear")
            if profiles and "Key Content" in profiles:
                password = profiles.split("Key Content")[1].split(":")[1].strip()
                print(Fore.GREEN + f"Password found: {password}. Connecting...")
                run_command(f"netsh wlan connect name=\"{ssid}\"")
            else:
                print(Fore.RED + f"No saved password found for {ssid}.")
                password = input(Fore.YELLOW + "Enter WiFi password: ")
                run_command(f"netsh wlan connect name=\"{ssid}\" key=\"{password}\"")
        else:
            print(Fore.RED + "Invalid choice.")
    except ValueError:
        print(Fore.RED + "Invalid input. Please enter a number.")

# function to get saved wifi passwords
def get_saved_wifi_passwords():
    print(Fore.CYAN + "Retrieving saved WiFi profiles...")
    output = run_command("netsh wlan show profiles")
    if output:
        profiles = []
        for line in output.splitlines():
            if "All User Profile" in line:
                ssid = line.split(":")[1].strip()
                details = run_command(f"netsh wlan show profile name=\"{ssid}\" key=clear")
                if details and "Key Content" in details:
                    password = details.split("Key Content")[1].split(":")[1].strip()
                    bssid = details.split("BSSID")[1].split(":")[1].strip() if "BSSID" in details else "N/A"
                    profiles.append({"SSID": ssid, "BSSID": bssid, "Password": password})

        if profiles:
            print(Fore.GREEN + tabulate(profiles, headers="keys", tablefmt="pretty"))
        else:
            print(Fore.RED + "No saved profiles found.")

# Main menu
def main():
    while True:
        try:
            print(Fore.MAGENTA + "\nWiFi Tool")
            print(Fore.BLUE + "1. View available WiFi networks")
            print(Fore.BLUE + "2. Connect to a WiFi network")
            print(Fore.BLUE + "3. Get saved WiFi passwords")
            print(Fore.RED + "0. Exit")

            choice = input(Fore.YELLOW + "Enter your choice: ")
            if choice == "1":
                show_available_networks()
            elif choice == "2":
                connect_to_network()
            elif choice == "3":
                get_saved_wifi_passwords()
            elif choice == "0":
                print(Fore.GREEN + "Exiting...")
                break
            else:
                print(Fore.RED + "Invalid choice.")
        except KeyboardInterrupt:
            print(Fore.RED + "\nProgram interrupted. Exiting...")
            break

if __name__ == "__main__":
    main()
