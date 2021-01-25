# ExtractHere fman plugin

**Version 0.1.0**

Shortcut to extract archive files right where they are.
Linux, probably OSX support.
Unpacking takes place using terminal command.

A folder with the filename
minus the qualifier is created.
The file is then unpacked into there.
If the folder to be created already exists,
confirmation is asked from the user.

Multiple files can be extracted at once.
Files that are not supported are simply skipped.
No error message is displayed.

## Supported formats

| Format          | Terminal command |
| --------------- | ---------------- |
| tar             | `tar`            |
| tar.gz          | `tar`            |
| zip             | `unzip`          |



## Key Bindings
 * [Ctrl+E]:    Extract the archive here.

Feel free to adjust the KeyBindings to your liking!

## ToDo:
 * Use fman native extraction for `tar` and `zip`
 * More formats?

## Installation:
Use fmans built in plugin installation tools. This will install the release version that is currently created. 

For a testing version, please download the source code and install it into your fman/Plugins/User directory. On linux this would be:

    ~/.config/fman/Plugins/User

