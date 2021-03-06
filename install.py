import os

RCFILES = [".shrc", ".zshrc", ".vimrc", ".quip.shrc", ".quip.vimrc", ".slate"]


def main():
    home = os.getenv("HOME")
    src_dir = os.path.dirname(os.path.abspath(__file__))

    for filename in RCFILES:
        path = os.path.join(home, filename)
        src_path = os.path.join(src_dir, filename)

        assert os.path.exists(src_path), "%s doesn't exist" % src_path

        if os.path.exists(path):
            if raw_input("%s already exists. Replace? [y/N]: " % path) != "y":
                continue
            os.remove(path)

        print "%s -> %s" % (path, src_path)
        os.symlink(src_path, path)


if __name__ == "__main__":
    main()
