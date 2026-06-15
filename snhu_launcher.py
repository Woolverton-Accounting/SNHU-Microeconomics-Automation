import webbrowser
import time

def open_snhu_workspace():
    print("Launching your SNHU Summer Term Workspace...")
    
    # 1. Open your main SNHU Brightspace Dashboard
    brightspace_url = "https://snhu.edu"
    webbrowser.open(brightspace_url)
    time.sleep(1) # Pauses for 1 second to let Windows open the tab cleanly
    
    # 2. Open the direct login page for SNHU Shapira Library / Textbook portal
    library_url = "https://snhu.edu"
    webbrowser.open(library_url)
    
    print("All portals launched successfully! Have a great study session.")

# Execute the automation function
open_snhu_workspace()
