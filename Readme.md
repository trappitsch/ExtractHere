# ExtractHere fman plugin

**Version 0.2.0**

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

| Format          | Other suffixes   | Terminal command |
| --------------- | ---------------- | ---------------- |
| tar             |                  | `tar`            |
| tar.gz          | taz, tgz         | `tar`            |
| tar.bz2         | tb2, tbz, tbz2, tz | `tar`          |
| tar.lz          |                  | `tar`            |
| tar.lzma        | tlz              | `tar`            |
| tar.lzo         |                  | `tar`            |
| tar.xz          |                  | `tar`            |
| tar.Z           | tZ, taZ          | `tar`            |
| tar.zst         | tzst             | `tar`            |
| zip             |                  | `unzip`          |

*Note*: Endings are generally not case sensitive,
except for `taZ` and `taz`.
In these cases,
only correct cases are identified as archives.


## Key Bindings
 * [Ctrl+E]:    Extract the archive here.

Feel free to adjust the KeyBindings to your liking!

## ToDo:
 * Use fman native extraction for `zip`

## Installation:
Use fmans built in plugin installation tools. This will install the release version that is currently created. 

For a testing version, please download the source code and install it into your fman/Plugins/User directory. On linux this would be:

    ~/.config/fman/Plugins/User

## Change log

### v0.2.0

Support all formats
that can be unpacked with `tar`.

### v0.1.0

Initial release.
Supports `.zip`, `.tar`, `.tar.gz`.
All extracting happens
using terminal commands.