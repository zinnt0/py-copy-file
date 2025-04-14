# write your code here
def copy_file(command: str) -> None:
    try:
        cp = command.split(" ")[0]
        if cp != "cp":
            return
        src = command.split(" ")[1]
        dest = command.split(" ")[2]
    except IndexError:
        pass
    else:
        if src == dest:
            return
        try:
            with open(src, "r")as src_file:
                content = src_file.read()
                with open(dest, "a") as dest_file:
                    dest_file.write(content)
        except FileNotFoundError:
            pass
