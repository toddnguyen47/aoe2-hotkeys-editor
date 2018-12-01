import os

cur_dir = os.getcwd()

# Keycode file
WINDOWS_KEYCODES_FILE = os.path.join(cur_dir, "utils/WindowsKeyboardKeycodes.csv")

# Input hki file
HKI_INPUT_FILE = os.path.join(cur_dir, "hki_files/player0.hki")

# Output hki file
HKI_OUTPUT_FILE = os.path.join(cur_dir, "hki_files/player000.hki")

# The extracted hotkey list file
HOTKEY_LIST_FILE = os.path.join(cur_dir, "hki_files/hotkey_list.txt")

# Changed text file to export to HKI
HOTKEY_TEXT_TO_EXPORT_HKI = os.path.join(cur_dir, "hki_files/hotkey_list1.txt")
