@echo off
:: Cyber Investigator Toolkit Auto-Installer

:: Check for admin rights
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo Please run this script as Administrator!
    pause
    exit /b
)

:: Install Python packages
pip install -r requirements.txt
pip install holehe maigret

:: Download whois.exe
powershell -Command "Invoke-WebRequest -Uri 'https://download.sysinternals.com/files/WhoIs.zip' -OutFile 'WhoIs.zip'"
powershell -Command "Expand-Archive -Path 'WhoIs.zip' -DestinationPath ."
copy /Y WhoIs\whois.exe C:\Windows\System32\whois.exe

:: Download PhoneInfoga (Windows binary)
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/sundowndev/phoneinfoga/releases/latest/download/phoneinfoga-windows-amd64.exe' -OutFile 'phoneinfoga.exe'"
copy /Y phoneinfoga.exe C:\Windows\System32\phoneinfoga.exe

:: Download Volatility (standalone EXE)
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/volatilityfoundation/volatility/releases/download/2.6.1/volatility_2.6_win64_standalone.exe' -OutFile 'volatility.exe'"
copy /Y volatility.exe C:\Windows\System32\volatility.exe

:: Cleanup
if exist WhoIs.zip del WhoIs.zip
if exist phoneinfoga.exe del phoneinfoga.exe
if exist volatility.exe del volatility.exe
if exist WhoIs rmdir /s /q WhoIs

:: Manual steps
echo.
echo Please manually install Wireshark (for tshark) from https://www.wireshark.org/download.html
echo Please manually install Metasploit from https://docs.metasploit.com/docs/using-metasploit/getting-started.html

:: Done
echo.
echo All possible tools installed! Please check above for any manual steps.
pause 