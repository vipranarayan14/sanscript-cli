import sys
from os import path

import typer


def get_input_data(input_file: typer.FileText, input_string: str) -> str:
    if input_file is not None:
        if input_string is not None:
            typer.echo(
                "Warning: The input string is ignored since input file is specified.",
                err=True,
            )
        return input_file.read()

    if input_string is not None:
        return input_string

    typer.echo(
        "Error: Either a string or a file is required as input. See help with "
        "'--help'.",
        err=True,
    )
    raise typer.Exit(code=1)


def write_output(output_file: typer.FileTextWrite, output_data: str):
    if output_file is None:
        return typer.echo(output_data)

    output_file.write(output_data)

    if output_file is sys.stdout:
        return

    typer.echo(f"Output written to: {path.realpath(output_file.name)}")
