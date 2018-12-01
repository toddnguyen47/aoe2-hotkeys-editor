import modules.hotkeys as hotkeys
import params
import sys
import os


def export_hki():
    """
    Export from a text input file (for now) to a .hki file.
    
    # FILES
    Hki input file      -> params.HKI_INPUT_FILE
    Text input file     -> params.HOTKEY_TEXT_TO_EXPORT_HKI
    Output file         -> params.HKI_OUTPUT_FILE
    """
    if os.path.isfile(params.HKI_OUTPUT_FILE):
        filename_only = os.path.basename(params.HKI_OUTPUT_FILE)
        overwrite = input("File {} exists. Would you like to overwrite it? (Y/N):\n>>> ".format(filename_only))
        if overwrite.lower() != "y":
            print("Exiting...")
            exit(0)

    with open(params.HKI_INPUT_FILE, "rb") as file:
        bytes_read = file.read()
        hotkey_obj = hotkeys.HotkeyFile(bytes_read)
    # hotkeyassign_obj = hotkeys.HotkeyAssign(hotkey_obj)

    # binary_output = hotkey_obj.serialize()
    # with open(params.HKI_OUTPUT_FILE, "wb") as file:
        # file.write(binary_output)
    
    # Get a dictionary of newly obtained keys
    parsed_dict = export_hki_parser()
    
    
    # For each sequential memory element in the hki file
    for memory_obj in hotkey_obj:
        hotkey_name = memory_obj[0]
        new_key_inputs = parsed_dict[hotkey_name]
        
        temp_dict = memory_obj
        memory_obj[1].update(new_key_inputs)

    # Export to hki file
    binary_output = hotkey_obj.serialize()
    with open(params.HKI_OUTPUT_FILE, "wb") as file:
        file.write(binary_output)
    
    print("Finished outputting to {}".format(params.HKI_OUTPUT_FILE.replace("\\", "/")))


def export_hki_parser():
    """
    Parse the text input file and return a dictionary.
    Dict[hk_id] = {Keys being used, ctrl, alt, shift,}
    
    # FILES
    Input text file     -> params.HOTKEY_TEXT_TO_EXPORT_HKI
    """
    key_dict = {}
    code_dict = get_keycodes(keycode_as_dictkey=False)

    # Parse the input file first
    with open(params.HOTKEY_TEXT_TO_EXPORT_HKI, "r") as file:
        data = file.read()
    
    data = data.split("\n")
    for line in data:
        # Only if line is not empty
        if line:
            line_split = line.split(":")
            hotkeyassign_key = line_split[0].strip()
            new_key_inputs = line_split[1].strip()

            # Only check if the hotkey assign key is not empty
            # AND the hotkeys exists in the hotkeys.hk_ids
            if hotkeyassign_key and hotkeyassign_key in hotkeys.hk_ids:
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
                
                # If the key is not empty
                if actual_key:
                    actual_key_code = code_dict[actual_key]

                # Update our dictionary
                # cur_hotkey_dict.update({'code': actual_key_code, 'ctrl': ctrl_used, 'alt': alt_used, 'shift': shift_used})
                
                key_dict[hotkeyassign_key] = {'code': actual_key_code, 'ctrl': ctrl_used, 'alt': alt_used, 'shift': shift_used}

    return key_dict


def read_in_hki_file():
    """
    Read in a HKI file and export it to params.HOTKEY_LIST_FILE
    """
    if os.path.isfile(params.HOTKEY_LIST_FILE):
        filename_only = os.path.basename(params.HOTKEY_LIST_FILE)
        overwrite = input("File {} exists. Would you like to overwrite it? (Y/N):\n>>> ".format(filename_only))
        if overwrite.lower() != "y":
            print("Exiting...")
            exit(0)

    # Open the binary hki file and uncompress it
    hotkey_obj = hotkeys.HotkeyFile(open(params.HKI_INPUT_FILE, "rb").read())
    # Get all the Windows keycodes
    keypress_dict = get_keycodes(keycode_as_dictkey=True)

    hotkey_keys_dict = {}
    # Get all hotkey controls from the hki file
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

        hotkey_keys_dict[hotkey_name] = key_used_str

    # Export to file
    with open(params.HOTKEY_LIST_FILE, "w") as output_file:
        # For each "group" in hk_groups
        for group in hotkeys.hk_groups:
            group_name = group[0]
            key_groups = group[1]
            output_file.write("".join((group_name, ":\n")))
            for key in key_groups:
                # If no keys
                controls = ""
                # If there is a key
                if key in hotkey_keys_dict:
                    controls = hotkey_keys_dict[key]
                output_file.write("".join((key, ": ", controls, "\n")))
            output_file.write("\n")

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
    print("Valid command line arguments are:")
    print(">>> read")
    print(">>> write")


if __name__ == "__main__":
    # Use only with Python 2.7
    if sys.version_info[0] < 3:
        raise Exception("Please run this file with Python 3")
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
