#!/usr/bin/env python3

import os
import subprocess

def run_command(command):
    print(f"Running: {command}")
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error: {e}")

def check_and_fix_common_issues():
    # Check if the network is up
    if os.system("ping -c 1 8.8.8.8") != 0:
        print("Network seems down, trying to restart the network manager")
        run_command("sudo systemctl restart NetworkManager")

    # Check if the package lists are up to date
    if os.system("apt-cache policy | grep http | wc -l") == 0:
        print("Package lists seem outdated, updating")
        run_command("sudo apt-get update")

    # Check if the Metasploit service is running
    if os.system("systemctl is-active --quiet postgresql") != 0:
        print("Metasploit database seems down, trying to start it")
        run_command("sudo systemctl start postgresql")

    # Check if the Tor service is running
    if os.system("systemctl is-active --quiet tor") != 0:
        print("Tor service seems down, trying to start it")
        run_command("sudo systemctl start tor")

def main():
    while True:
        print("\n1. Update system")
        print("2. Install tools")
        print("3. Setup Metasploit database")
        print("4. Setup Tor service")
        print("5. Clone GitHub repository")
        print("6. Setup Wi-Fi")
        print("7. Check and fix common issues")
        print("8. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            run_command("sudo apt-get update -y")
            run_command("sudo apt-get upgrade -y")
        elif choice == "2":
            tools = ["git", "nmap", "wireshark", "metasploit-framework", "tor", "torbrowser-launcher"]
            for tool in tools:
                run_command(f"sudo apt-get install {tool} -y")
        elif choice == "3":
            run_command("sudo msfdb init")
        elif choice == "4":
            run_command("sudo systemctl start tor")
            run_command("sudo systemctl enable tor")
        elif choice == "5":
            run_command("git clone https://github.com/tukru")
        elif choice == "6":
            run_command("sudo ifconfig wlan0 up")
        elif choice == "7":
            check_and_fix_common_issues()
        elif choice == "8":
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
