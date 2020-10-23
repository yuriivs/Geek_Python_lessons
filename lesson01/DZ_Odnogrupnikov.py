from time import sleep as pause

def out_red(text):
    print("\033[31m {}" .format(text), pause(2), "\033[37m {}" .format(text))

def out_yellow(text):
    print("\033[33m {}" .format(text))

def out_green(text):
    print("\033[32m {}" .format(text))

out_red("red")
pause(2)
out_yellow("yellow")
pause(2)
out_green("green")


