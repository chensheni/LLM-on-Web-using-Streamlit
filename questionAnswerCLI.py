#!/usr/bin/env python3

"""
An cohere api key is required to use this script.
"""

import click
from oalib.solutions import submit_question


@click.command()
@click.argument("text")
def main(text):
    """This is the main function that you ask the Cohere API a question to get an answer

    example: ./questionAnswerCLI.py "Who won the 2020 Summer Olympics?"

    """
    print(submit_question(text))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
