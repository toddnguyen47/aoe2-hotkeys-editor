# aoe2_hotkeys_editor
A fork of crimsoncantab's [AoC Hotkey Editor](https://github.com/crimsoncantab/aok-hotkeys) with some of my personal edits. All credits go to [crimsoncantab](https://github.com/crimsoncantab/)'s wonderful code. He wrote everything in the `modules` folder.

# Requirements
You will need to download and install [Python 3+](https://www.python.org/downloads/).

# How to Run
First, go into the `non-webframework` folder.

NOTE: If at any time you are lost, type into a command line
```
python main.py --help
```
And a help message will display.

## Read in a HKI file
To read in a HKI file, type the following into a terminal:
```
python main.py textFileToSaveInputsTo -i input_hki_file
```
**NOTE:** Make sure the input_hki_file ends with .hki! i.e. it has a HKI file extension.

## Export to a HKI file
To export a HKI file, type the following into a terminal:
```
python main.py textFileWithNewInputs -o output_hki_file
```
**NOTE:** Make sure the output_hki_file ends with .hki! i.e. it has a HKI file extension.


# How to Place into your Steam Directory
1. Go into where you installed Steam and Age of Empires 2. Usually, it is located at `C:\Program Files (x86)\Steam\steamapps\common\Age2HD\profiles`
2. **IMPORTANT:** Make a backup of your `profile0.hki` file in case anything goes wrong! One way to make a backup is to copy `profile0.hki` file into another directory elsewhere.
3. After you made a backup of `profile0.hki`, place your newly exported hki file in this directory. Rename this new file `profile0.hki`, effectively replacing the old hki file.
4. Boot up Age of Empires 2. You should be good to go!
