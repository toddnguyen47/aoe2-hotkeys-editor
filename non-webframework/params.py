import os

cur_dir = os.getcwd()

# Keycode file
WINDOWS_KEYCODES_FILE = os.path.join(cur_dir, "utils/WindowsKeyboardKeycodes.csv")

# Input hki file
INPUT_FILE = os.path.join(cur_dir, "hki_files/player0.hki")

# Output hki file
OUTPUT_FILE = os.path.join(cur_dir, "hki_files/player000.hki")

# The extracted hotkey list file
HOTKEY_LIST_FILE = os.path.join(cur_dir, "hki_files/hotkey_list.txt")

# Backup changed hotkey file
HOTKEY_BACKUP_FILE = os.path.join(cur_dir, "hki_files/hotkey_list1.txt")
