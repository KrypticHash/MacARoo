# MacARoo - The Mac Address Changer 🕶️
           
Welcome to MacARoo! 🎉
       
Tired of being tracked? Looking for a way to spice up your digital life? MacARoo is here to help you rock the cyber world incognito-style! 🕵️‍♂️ Change your MAC address with flair using our delightful tool. Whether you're a privacy-conscious ninja or just a curious soul, MacARoo has got your back.
  
## What's MacARoo All About? 🤔

MacARoo is a simple yet powerful command-line tool that lets you change your device's MAC address effortlessly. A MAC address is like your device's fingerprint in the digital realm. By changing it, you can dodge those pesky network trackers and roam the online universe like a shadow. 🌌

## Features 🌟

- **Random Mode**: Feeling lucky? Let MacARoo pick a random MAC address for you! 🎲
- **Custom Mode**: Craft your own MAC address masterpiece. Express yourself! 💃
- **Stealth Mode**: Blend into the digital crowd. Change your MAC address at intervals. 🕶️
- **Backup & Restore**: Don't lose your original MAC address. We've got your back! 🛡️
- **Emoji Magic**: Add a touch of whimsy to your MAC address. Who said tech can't be fun? 🦄✨

## Usage 🛠️

Follow the steps below to use the MacARoo:

1. Clone the repository:

   ```bash
   git clone https://github.com/KrypticHash/MacARoo.git
   cd MacARoo
   ```

2. Run the script using Python:

   ```bash
   python MacARoo.py -i <interface> -m <new_mac>
   ```

   Replace `<interface>` with the name of the network interface whose MAC address you want to change, and `<new_mac>` with the desired MAC address. Make sure to use the following format for the MAC address: `XX:XX:XX:XX:XX:XX`.

   For example:

   ```bash
   python MacARoo.py -i eth0 -m 00:11:22:33:44:55
   ```

3. The script will disable the specified interface, change its MAC address, and then re-enable the interface. You will see output similar to the following:
   ```
   [+] Changing MAC address for eth0 to 00:11:22:33:44:55
   ```

## Options

The MAC Address Changer Script provides the following command-line options:

- `-i`, `--interface`: Specify the name of the network interface for which you want to change the MAC address.
- `-m`, `--mac`: Specify the new MAC address you want to set for the interface.

If you do not provide both the interface and the new MAC address using the options above, the script will display an error message and provide guidance on using the `--help` option for more information.

## Example

Here's an example of how to use the script to change the MAC address of the `eth0` interface to `00:11:22:33:44:55`:

```bash
python MacARoo.py -i eth0 -m 00:11:22:33:44:55
```

## Disclaimer

This script is provided as-is and should be used responsibly and in accordance with applicable laws and regulations. Changing MAC addresses may have unintended consequences on network connectivity and security. The author(s) of this script are not responsible for any misuse, damage, or legal issues caused by its use.

Remember, with great power comes great responsibility! Use MacARoo wisely. 🦸‍♂️
