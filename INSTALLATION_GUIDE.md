# 🕵️ Cyber Investigator Toolkit - Installation & Usage Guide

A powerful, user-friendly GUI toolkit for cyber forensics and OSINT tasks with Matrix-style interface.

## 📋 Table of Contents
- [System Requirements](#system-requirements)
- [Quick Installation](#quick-installation)
- [Manual Installation](#manual-installation)
- [Tool Installation Guide](#tool-installation-guide)
- [Usage Guide](#usage-guide)
- [Troubleshooting](#troubleshooting)
- [Features](#features)

## 🖥️ System Requirements

- **OS:** Windows 10/11 (Primary), Linux (Experimental)
- **Python:** 3.7 or higher
- **RAM:** 4GB minimum, 8GB recommended
- **Storage:** 2GB free space
- **Permissions:** Administrator access (for tool installation)

## ⚡ Quick Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/cyber-investigator-toolkit.git
cd cyber-investigator-toolkit
```

### Step 2: Run Auto-Installer (Windows)
```bash
# Right-click on install_all.bat and "Run as Administrator"
# OR run in Command Prompt as Administrator:
install_all.bat
```

### Step 3: Launch the Tool
```bash
python investigetorGUI.py
```

## 🔧 Manual Installation

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
pip install holehe maigret
```

### Step 2: Install External Tools

#### 1. WHOIS Tool
- Download from: [Sysinternals Whois](https://docs.microsoft.com/en-us/sysinternals/downloads/whois)
- Extract `whois.exe`
- Copy to: `C:\Windows\System32\` (requires admin rights)

#### 2. PhoneInfoga
- Download from: [PhoneInfoga Releases](https://github.com/sundowndev/phoneinfoga/releases)
- Get the Windows binary (`phoneinfoga-windows-amd64.exe`)
- Rename to `phoneinfoga.exe`
- Copy to: `C:\Windows\System32\`

#### 3. Volatility
- Download from: [Volatility Releases](https://github.com/volatilityfoundation/volatility/releases)
- Extract the standalone EXE
- Copy to: `C:\Windows\System32\`

#### 4. Wireshark (for tshark)
- Download from: [Wireshark](https://www.wireshark.org/download.html)
- Install with default settings
- Ensure "tshark" is selected during installation

#### 5. Metasploit
- Download from: [Metasploit](https://docs.metasploit.com/docs/using-metasploit/getting-started.html)
- Follow the installation guide
- Add to system PATH

## 🛠️ Tool Installation Guide

### Python-Based Tools
```bash
# Install via pip
pip install dnsrecon
pip install holehe
pip install maigret
```

### Windows-Specific Setup
```bash
# Add tools to PATH (if not using System32 method)
# Create a folder: C:\Tools
# Add C:\Tools to your system PATH
# Copy all .exe files to C:\Tools
```

### Verification
```bash
# Test if tools are in PATH
whois --version
phoneinfoga --help
volatility --help
tshark --version
msfconsole --version
```

## 🚀 Usage Guide

### 1. Launching the Tool
```bash
python investigetorGUI.py
```

### 2. Interface Overview
- **Matrix Background:** Animated falling code effect
- **Input Fields:** Enter target information (domain, phone, email, etc.)
- **Tool Categories:** OSINT, Forensics, Network Monitoring, Exploit Testing
- **Result Dialogs:** Separate windows for each tool output

### 3. Using OSINT Tools

#### WHOIS Lookup
1. Enter domain in "Enter Domain" field
2. Click "Run WHOIS Lookup"
3. Results appear in popup window
4. Use Copy/Save buttons to export results

#### DNS Reconnaissance
1. Enter target domain
2. Click "Run DNS Recon"
3. View DNS records, subdomains, and more

#### Phone Number OSINT
1. Enter phone number with country code
2. Click "Phone Number OSINT (PhoneInfoga)"
3. Get carrier info, location, and more

#### Email Intelligence
1. Enter email address
2. Click "Email Intelligence (Holehe)"
3. Check email existence across platforms

#### Username Search
1. Enter username
2. Click "Username Search (Maigret)"
3. Find username across social media platforms

### 4. Using Forensics Tools

#### USB History
1. Click "USB History"
2. View connected USB devices (Windows only)
3. Get device IDs and descriptions

#### Volatility RAM Analysis
1. Ensure you have a memory dump file (`memdump.raw`)
2. Click "Run Volatility - RAM Analysis"
3. Analyze running processes and memory artifacts

### 5. Network Monitoring

#### Tshark Capture
1. Click "Run Tshark Capture"
2. Capture network traffic for 10 seconds
3. Analyze packet data

### 6. Exploit Testing

#### PDF Exploit Generation
1. Enter LHOST (your IP address)
2. Enter LPORT (port number)
3. Click "Generate Malicious PDF (Metasploit)"
4. Generate test PDF with embedded payload

### 7. Result Management
Each tool result opens in a separate dialog with:
- **Copy:** Copy results to clipboard
- **Save:** Save results to text file
- **Clear:** Clear the result area
- **Font Size:** Adjust text size (10-24)
- **Theme:** Choose dark/light/matrix theme

## 🔍 Features

### 🎨 User Interface
- Matrix-style animated background
- Dark theme with green accents
- Responsive design
- Separate result dialogs

### 🛡️ Security Tools
- **OSINT:** WHOIS, DNS recon, phone/email/username intelligence
- **Forensics:** USB history, memory analysis
- **Network:** Packet capture and analysis
- **Exploit:** PDF payload generation

### 📊 Result Management
- Copy to clipboard
- Save to file
- Multiple themes
- Adjustable font sizes
- Clear functionality

## 🚨 Troubleshooting

### Common Issues

#### "Command not found" Error
```bash
# Check if tool is in PATH
where toolname

# Add to PATH manually
set PATH=%PATH%;C:\path\to\tool
```

#### Python Module Errors
```bash
# Reinstall Python packages
pip uninstall package_name
pip install package_name
```

#### Permission Errors
- Run Command Prompt as Administrator
- Ensure tools are in System32 or PATH
- Check file permissions

#### GUI Not Starting
```bash
# Check PyQt5 installation
pip install PyQt5

# Check Python version
python --version
```

### Tool-Specific Issues

#### WHOIS Not Working
- Download from Sysinternals
- Ensure whois.exe is in System32
- Run as Administrator

#### PhoneInfoga Issues
- Download correct Windows binary
- Check if executable is blocked
- Run from Command Prompt

#### Volatility Problems
- Download correct version for your OS
- Ensure memory dump file exists
- Check profile compatibility

#### Metasploit Issues
- Follow official installation guide
- Ensure Ruby dependencies are installed
- Check PATH configuration

## 📝 Notes

### Security Considerations
- This tool is for educational and authorized testing only
- Always obtain proper permissions before testing
- Some tools may trigger antivirus software
- Use in isolated testing environment

### Performance Tips
- Close unnecessary applications
- Ensure sufficient RAM (8GB+ recommended)
- Use SSD for better performance
- Close result dialogs when not needed

### File Locations
- **Memory Dumps:** Place `memdump.raw` in tool directory
- **Saved Results:** Choose location when saving
- **Logs:** Check Command Prompt for error messages

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Users are responsible for ensuring they have proper authorization before using these tools. The authors are not responsible for any misuse.

---

**Happy Hacking! 🕵️‍♂️💻** 