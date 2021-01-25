import os
from fman import DirectoryPaneCommand, show_alert, YES, NO
from fman.url import as_human_readable, dirname
from fman.fs import is_dir, notify_file_added, mkdir


class ExtractHere(DirectoryPaneCommand):
    def __call__(self):
        chosen_files = self.get_chosen_files()
        for it in chosen_files:
            # determine qualifier:
            if it.endswith(".tar.gz"):
                qual = ".tar.gz"
            elif it.endswith(".tar"):
                qual = ".tar"
            elif it.endswith(".zip"):
                qual = ".zip"
            else:
                continue  # no unpacking to be done
            # unpack
            ext_name = it[0 : -len(qual)]
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
            if qual == ".tar.gz":
                cmd = f"tar -xzf {file_hr} -C {parent_folder}"
            elif qual == ".tar":
                cmd = f"tar -xf {file_hr} -C {parent_folder}"
            elif qual == ".zip":
                cmd = f"unzip {file_hr} -d {parent_folder}"
            os.system(cmd)
            notify_file_added(ext_name)
