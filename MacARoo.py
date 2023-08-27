#!/usr/bin/env python

# Import required modules
import subprocess
import optparse

# Function to get command line arguments
def get_arguments():
    # Create an instance of OptionParser
    parser = optparse.OptionParser()

    # Add options to the parser
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    # Parse the command line arguments
    (options, arguments) = parser.parse_args()

    # Check if required options are provided
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    
    # Return the parsed options
    return options

# Function to change MAC address
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    # Disable the network interface
    subprocess.call(["ifconfig", interface, "down"])

    # Change the MAC address of the interface
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    # Enable the network interface
    subprocess.call(["ifconfig", interface, "up"])

# Get the command line arguments
options = get_arguments()

# Change the MAC address using the provided options
change_mac(options.interface, options.new_mac)
