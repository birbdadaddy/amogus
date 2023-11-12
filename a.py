import ctypes
import sys,os 

try:
    # Try to elevate privileges using pywin32
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, '"C:\\Users\\LotionMen\\Documents\\.Programming\\Python\\.My Virus\\.Installer\\Code Py\\a.py"', None, 1)
except Exception as e:
    print(f"Failed to request administrator privileges: {e}")
    sys.exit(1)

# Your main script logic goes here
print("Running with administrator privileges.")
os.system('start cmd')