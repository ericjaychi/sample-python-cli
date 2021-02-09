# Import the click module that was just downloaded.
import click


# Makes the function main a designated group for commands. Allowing multiple functions to be tied to main.
@click.group()
# Function that represents a group since there is no command decorator.
def main():
	# Creating an empty function since we need to have this exist so we can use it as a group.
	pass


# Uses the "main" group to indicate that this function is a command of that group.
@main.command()
@click.option(
	# Aliases that can be used to indicate the flag in the terminal.
	"--number",
	"-n",
	# Uses this value if nothing was inputted in the terminal.
	default=1,
	# Help message that appends right into the terminal.
	help="The number of iterations that you want printed"
)
# Function that represents a command. The function name is the command name.
def hello(number):
	"""
	Prints the value "Hello" to the terminal.
	"""

	# Simple print statement to the terminal.
	for i in range(number):
		click.echo("Hello")


# Uses the "main" group to indicate that this function is a command of that group.
@main.command()
# Function that represents a command. The function name is the command name.
def world():
	"""
	Prints the value "World!" to the terminal.
	"""
	# Simple print statement to the terminal.
	click.echo("World!")


if __name__ == "__main__":
	main()
