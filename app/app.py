from sys import argv
from server import *


if __name__ == "__main__":
    if len(argv) > 1:
        # Run function
        if argv[1] == "--get-currencies":
            get_currencies()
        elif argv[1] == "--get-rates":
            if len(argv) < 3:
                raise ValueError("No currency parameter!")
            get_rates(currencies=[argv[2]])
        else:
            raise ValueError("Unknown function")

    else:
        # Run server
        app.run(
            host="localhost",
            port=5000
        )
