# WiFi Tool

## Overview
The **WiFi Tool** is a Python-based utility for managing WiFi networks on Windows and Linux. It provides functionalities such as viewing available networks, connecting to networks, retrieving saved passwords. The tool offers a user-friendly interface with colorful output and keyboard navigation for enhanced usability.

---

## Features
1. **View Available Networks**
   - Scans and displays all nearby WiFi networks in a tabular format with essential details like SSID, BSSID, signal strength, etc.

2. **Connect to a Network**
   - Lists available networks for selection.
   - Automatically checks if the selected network's password is saved. If not, it prompts the user to enter a password.

3. **Retrieve Saved Networks**
   - Displays a list of all saved WiFi networks along with their SSID, BSSID, and password.


## Installation
### Prerequisites
- Python 3.7+
- Pip (Python Package Manager)
- Administrative privileges

### Required Modules
The tool requires the following Python libraries:
- `colorama`: For colorful terminal messages.
- `tabulate`: For formatted table output.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Sheikh-Muhammad-Mujtaba/wifi-tool
   cd wifi-tool
   ```

2. Run the tool:
   ```bash
   python run.py
   ```

---

## Usage
### Running the Tool
To launch the program, run the `run.py` script:
```bash
python run.py
```

### Menu Options
1. **View Available Networks**
   - Displays all nearby WiFi networks in a formatted table.

2. **Connect to a WiFi Network**
   - Prompts for available networks and connects automatically if the password is saved.

3. **Get Saved WiFi Networks**
   - Lists saved networks along with their passwords (Windows-only).

0. **Exit**
   - Exits the program.

---

## Future Plans

1. **Add Deauthentication Attack Functionality**  
   - Enhance the menu by integrating the deauthentication attack option for both Linux and Windows (where feasible).  
   - Allow users to select target networks interactively.  

2. **Enable Monitor Mode Functionality**  
   - Include a dedicated option to enable monitor mode on selected interfaces, streamlining wireless network analysis.  

3. **Disable Monitor Mode Functionality**  
   - Add the ability to stop monitor mode and restore interfaces to their default state.  

4. **Capture Handshake Data**  
   - Implement functionality to capture handshake packets for WPA/WPA2 networks.  
   - Provide user-friendly options to save captured data for further analysis.  

5. **Crack Handshake Data**  
   - Introduce a feature to crack captured handshake data using wordlists or brute force.  
   - Support integration with popular tools like `aircrack-ng` for efficient processing.  

These additions aim to expand the tool's capabilities, making it a comprehensive solution for WiFi network management and penetration testing.
   
---

## Support
For issues, please open an issue on the [GitHub repository](https://github.com/Sheikh-Muhammad-Mujtaba/wifi-tool) or contact the developer.

---

## Collaboration Steps

1. Fork the Repository

2. Create a fork of this project on GitHub to start working on your own copy and Make Changes

3. Create a new branch for your feature or bug fix.

4. Submit Pull Request

After testing your changes, submit a pull request to the main repository with a detailed description of your work.
Join Discussions

Share ideas, improvements, or feature suggestions through issues or discussion boards.

## Acknowledgments
We value every contribution, big or small. Let’s work together to make this tool a robust and indispensable resource for WiFi network management and security testing.

Happy coding! 🎉


---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

