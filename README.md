# 🕵️ Cyber Investigator Toolkit

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)](https://pypi.org/project/PyQt5/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

A powerful, user-friendly GUI toolkit for cyber forensics and OSINT tasks with a stunning Matrix-style interface. This toolkit combines multiple security tools into one intuitive application.

## 🎯 Features

### 🔍 OSINT Tools
- **WHOIS Lookup** - Domain registration information
- **DNS Reconnaissance** - DNS records and subdomain enumeration
- **Phone Number OSINT** - Carrier and location information (PhoneInfoga)
- **Email Intelligence** - Email existence across platforms (Holehe)
- **Username Search** - Social media presence (Maigret)

### 📀 Forensics Tools
- **USB History** - Connected USB devices analysis
- **Volatility RAM Analysis** - Memory forensics and process analysis

### 📈 Network Monitoring
- **Tshark Capture** - Network packet analysis and capture

### 📁 Exploit Testing
- **PDF Exploit Generation** - Malicious PDF creation (Metasploit)

### 🎨 User Interface
- **Matrix-style animated background**
- **Dark theme with green accents**
- **Separate result dialogs for each tool**
- **Copy, Save, Clear functionality**
- **Customizable themes and font sizes**

## 🚀 Quick Start

### Prerequisites
- Windows 10/11
- Python 3.7+
- Administrator privileges

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/cyber-investigator-toolkit.git
cd cyber-investigator-toolkit

# Run auto-installer (as Administrator)
install_all.bat

# Launch the tool
python investigetorGUI.py
```

### Manual Installation
For detailed installation instructions, see [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main_interface.png)
*Matrix-style animated background with tool categories*

### Result Dialog
![Result Dialog](screenshots/result_dialog.png)
*Separate popup windows with copy/save functionality*

### Tool Categories
![Tool Categories](screenshots/tool_categories.png)
*OSINT, Forensics, Network, and Exploit tools*

## 🛠️ Tools Included

| Tool | Purpose | Installation |
|------|---------|--------------|
| **WHOIS** | Domain information lookup | Sysinternals |
| **dnsrecon** | DNS reconnaissance | `pip install dnsrecon` |
| **PhoneInfoga** | Phone number intelligence | GitHub releases |
| **Holehe** | Email intelligence | `pip install holehe` |
| **Maigret** | Username search | `pip install maigret` |
| **Volatility** | Memory forensics | GitHub releases |
| **Tshark** | Network analysis | Wireshark installer |
| **Metasploit** | Exploit framework | Official installer |

## 📁 Project Structure

```
cyber-investigator-toolkit/
├── investigetorGUI.py          # Main GUI application
├── install_all.bat             # Windows auto-installer
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── INSTALLATION_GUIDE.md       # Detailed installation guide
└── screenshots/                # Application screenshots
```

## 🎮 Usage

1. **Launch the application**
   ```bash
   python investigetorGUI.py
   ```

2. **Enter target information**
   - Domain name
   - Phone number (with country code)
   - Email address
   - Username
   - LHOST/LPORT (for exploits)

3. **Select and run tools**
   - Click any tool button
   - Results appear in separate dialog
   - Use Copy/Save buttons to export

4. **Customize results**
   - Change font size (10-24)
   - Switch themes (dark/light/matrix)
   - Clear or save results

## 🔧 Configuration

### Adding New Tools
The modular design makes it easy to add new tools:

1. Add input fields (if needed)
2. Create a new function (e.g., `run_newtool()`)
3. Add a button and connect it
4. Use `self.show_result()` for output

### Customizing Themes
Modify the style variables in the main class:
```python
label_style = "color: #00FF41; font-weight: bold; ..."
button_style = "QPushButton { background: #111; ... }"
```

## 🚨 Troubleshooting

### Common Issues
- **"Command not found"** - Check if tool is in PATH
- **Permission errors** - Run as Administrator
- **GUI not starting** - Check PyQt5 installation

### Getting Help
1. Check [INSTALLATION_GUIDE.md](INSTALLATION_GUIDE.md)
2. Verify all tools are installed correctly
3. Check Command Prompt for error messages
4. Open an issue on GitHub

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Development Setup
```bash
# Install development dependencies
pip install -r requirements.txt

# Run the application
python investigetorGUI.py

# Test new features
# Add unit tests if applicable
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

**This tool is for educational and authorized testing purposes only.**

- Always obtain proper permissions before testing
- Use only on systems you own or have explicit permission to test
- Some tools may trigger antivirus software
- The authors are not responsible for any misuse

## 🙏 Acknowledgments

- **PhoneInfoga** - Phone number intelligence
- **Holehe** - Email intelligence
- **Maigret** - Username search
- **Volatility** - Memory forensics
- **Metasploit** - Exploit framework
- **PyQt5** - GUI framework

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/cyber-investigator-toolkit/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/cyber-investigator-toolkit/discussions)
- **Wiki:** [Project Wiki](https://github.com/yourusername/cyber-investigator-toolkit/wiki)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=yourusername/cyber-investigator-toolkit&type=Date)](https://star-history.com/#yourusername/cyber-investigator-toolkit&Date)

---

**Made with ❤️ for the cybersecurity community**

**Happy Hacking! 🕵️‍♂️💻** 