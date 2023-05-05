from console_creator import *

def hel_wrld():
    print("Hello World")

def echo(text, times=1):
    for p in range(int(times)):
        print(text)


console = Console(exit_aliases=("exit",), lowercase_commands=True, end_message=None)

console.add_command(Command("hello_world", hel_wrld, description="prints hello world"))

ECHO_DESCRIPTION = "prints text"
ECHO_TEXT_DESCRIPTION = "text to be printed"
ECHO_TIMES_DESCRIPTION = "times text to be printed"
ECHO_TEXT_REQ_ARGUMENT1 = Argument("text", description=ECHO_TEXT_DESCRIPTION)
ECHO_TIMES_OPT_ARGUMENT1 = Argument("times", description=ECHO_TIMES_DESCRIPTION, optional=True)
console.add_command(Command("echo", echo, description=ECHO_DESCRIPTION,
                            required_arguments=(ECHO_TEXT_REQ_ARGUMENT1, ),
                            optional_arguments=(ECHO_TIMES_OPT_ARGUMENT1, )))

console.launch()
