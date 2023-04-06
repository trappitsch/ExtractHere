import os
from fman import DirectoryPaneCommand, show_alert, YES, NO
from fman.url import as_human_readable, dirname
from fman.fs import is_dir, notify_file_added, mkdir


class ExtractHere(DirectoryPaneCommand):
    def __call__(self):
        # tar options dictionary
        tar_opts = {
            ".tar.gz": "-xzf",
            ".tar.bz2": "-xjf",
            ".tar.lz": "--lzip -xf",
            ".tar.lzma": "--lzma -xf",
            ".tar.xz": "--xz -xf",
            ".tar.zst": "--zstd -xf",
            ".tar.Z": "-xZf",
            ".tar": "-xf",
        }

        # get chosen files and loop through it to unpack
        chosen_files = self.get_chosen_files()
        for it in chosen_files:
            # determine qualifier:
            itlow = it.lower()
            if any(itlow.endswith(s) for s in (".tar.gz", ".tgz")) or it.endswith(
                ".taz"
            ):
                qual = ".tar.gz"
                len_qual = len(qual) if itlow.endswith(qual) else 4
            elif any(
                itlow.endswith(s) for s in (".tar.bz2", ".tb2", ".tbz", ".tbz2", ".tz2")
            ):
                qual = ".tar.bz2"
                if itlow.endswith(qual):
                    len_qual = 8
                elif itlow.endswith(".tbz2"):
                    len_qual = 5
                else:
                    len_qual = 4
            elif itlow.endswith(".tar.lz"):
                qual = ".tar.lz"
                len_qual = 7
            elif itlow.endswith(".tar.lzma"):
                qual = ".tar.lzma"
                len_qual = 9
            elif itlow.endswith(".tar.lz"):
                qual = ".tar.lzo"
                len_qual = 8
            elif itlow.endswith(".tar.xz"):
                qual = ".tar.xz"
                len_qual = 7
            elif any(itlow.endswith(s) for s in (".tar.zst", ".tzst")):
                qual = ".tar.zst"
                len_qual = 8 if itlow.endswith(".tar.zst") else 5
            elif any(itlow.endswith(s) for s in (".tar.Z", ".tZ")) or it.endswith(
                ".taZ"
            ):
                qual = ".tar.Z"
                if itlow.endswith(".tar.Z"):
                    len_qual = 6
                elif itlow.endswith(".tZ"):
                    len_qual = 3
                else:
                    len_qual = 4
            elif itlow.endswith(".tar"):
                qual = ".tar"
                len_qual = 4
            elif itlow.endswith(".zip"):
                qual = ".zip"
                len_qual = 4
            else:
                continue  # no unpacking to be done
            # unpack
            ext_name = it[0:-len_qual]
            # check if exists
            try:
                if is_dir(ext_name):
                    choice = show_alert(
                        "The file already exists. Do you want to overwrite it?",
                        buttons=YES | NO,
                        default_button=NO,
                    )
                    if choice == NO:
                        continue
            except FileNotFoundError:  # no such folder
                pass

            # make the folder
            try:
                is_dir(ext_name)
            except FileNotFoundError:  # folder does not exist
                mkdir(ext_name)

            # human readable stuff
            file_hr = as_human_readable(it)
            parent_folder = as_human_readable(ext_name)

            # command from terminal
            if qual == ".zip":
                cmd = f"unzip '{file_hr}' -d '{parent_folder}'"
            # all other commands use tar
            else:
                opts = tar_opts[qual]
                cmd = f"tar {opts} '{file_hr}' -C '{parent_folder}'"
            os.system(cmd)
            notify_file_added(ext_name)
