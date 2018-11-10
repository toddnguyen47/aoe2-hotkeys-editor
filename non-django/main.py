import modules.hotkeys as hotkeys
import params
import sys


def export_hki():
    code_dict = get_keycodes(keycode_as_dictkey=False)

    hotkey_obj = hotkeys.HotkeyFile(open(params.INPUT_FILE, "rb").read())
    # hotkeyassign_obj = hotkeys.HotkeyAssign(hotkey_obj)

    with open(params.HOTKEY_BACKUP_FILE, "r") as file:
        data = file.read()
    
    data = data.split("\n")
    for line in data:
        # Only if line is not empty
        if line:
            line_split = line.split(":")
            hotkeyassign_key = line_split[0].strip()
            new_key_inputs = line_split[1].strip()

            # Only check if the hotkey assign key is not empty
            if hotkeyassign_key:
                # Save current hotkey into a temporary dict
                cur_hotkey_dict = hotkey_obj[hotkeyassign_key]

                # If CTRL key was used
                ctrl_used = True if "CTRL" in new_key_inputs else False
                # If ALT key was used
                alt_used = True if "ALT" in new_key_inputs else False
                # If SHIFT key was used
                shift_used = True if "SHIFT" in new_key_inputs else False
                # Get the key used
                if "+" in new_key_inputs:
                    # Will be the last input after the + sign
                    actual_key = new_key_inputs.split("+")[-1].strip()
                else:
                    actual_key = new_key_inputs.strip()
                
                actual_key_code = code_dict[actual_key]
                # Update our dictionary
                cur_hotkey_dict.update({'code': actual_key_code, 'ctrl': ctrl_used, 'alt': alt_used, 'shift': shift_used})

    binary_output = hotkey_obj.serialize()
    with open(params.OUTPUT_FILE, "wb") as file:
        file.write(binary_output)
    
    print("Finished outputting to " + params.OUTPUT_FILE)


def read_in_hki_file():
    # Open the binary hki file and uncompress it
    hotkey_obj = hotkeys.HotkeyFile(open(params.INPUT_FILE, "rb").read())
    # Get all the Windows keycodes
    keypress_dict = get_keycodes(keycode_as_dictkey=True)

    # Export to file
    with open(params.HOTKEY_LIST_FILE, "w") as output_file:
        for element in hotkey_obj:
            controls_list = element[1]
            hotkey_name = element[0]
            # Code for key being used
            cur_key = keypress_dict[controls_list['code']]

            # See if any modifier keys were used
            ctrl_used = controls_list['ctrl']
            shift_used = controls_list['shift']
            alt_used = controls_list['alt']

            # Key used string example: CTRL + SHIFT + ALT + G
            key_used_str = cur_key
            if alt_used:
                key_used_str = " ".join(("ALT +", key_used_str))
            if shift_used:
                key_used_str = " ".join(("SHIFT +", key_used_str))
            if ctrl_used:
                key_used_str = " ".join(("CTRL +", key_used_str))

            # Write it to a file
            output_file.write("{}: {}\n".format(hotkey_name, key_used_str))
    
    print("Exported to {}".format(params.HOTKEY_LIST_FILE).replace("\\", "/"))


def get_keycodes(keycode_as_dictkey):
    """
    Reference:
    https://docs.microsoft.com/en-us/windows/desktop/inputdev/virtual-key-codes

    # Arguments
    keycode_as_dictkey  -> True if you want the keycode to be the dictionary's key, false otherwise
    """
    with open(params.WINDOWS_KEYCODES_FILE, "r") as file:
        data = file.read()
    
    data = data.split("\n")
    dict1 = {}
    for line in data:
        # If line is not empty
        if line.strip():
            # Split on first comma
            comma_split = line.split(",", 1)
            
            if keycode_as_dictkey:
                # Convert the key from hexadecimal to decimal code
                key = int(comma_split[0], 16)
                dict1[key] = comma_split[1].strip()
            else:
                value = int(comma_split[0], 16)
                dict1[comma_split[1].strip()] = value

    return dict1


def print_error():
    print("Valid arguments are:")
    print("[1] read")
    print("[2] write")


if __name__ == "__main__":
    # Use only with Python 2.7
    if sys.version_info[0] > 2:
        raise Exception("Please run this file with Python 2.7")
    if len(sys.argv) < 2:
        print("Please provide a command line arguments.")
        print_error()
    else:
        if (sys.argv[1] == "read"):
            read_in_hki_file()
        elif (sys.argv[1] == "write"):
            export_hki()
        else:
            print_error()
