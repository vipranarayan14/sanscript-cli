import sys
from os import path
from typing import Optional

import typer
from indic_transliteration.sanscript import transliterate, SCHEMES, SchemeMap

import help_text

app = typer.Typer()

scheme_names = list(SCHEMES.keys())

scheme_help = "Choose from: {}.".format(", ".join(scheme_names))


def get_input_data(input_file: typer.FileText, input_string: str) -> str:
    if input_file is not None:
        if input_string is not None:
            typer.echo(
                "Warning: The input string is ignored since input file is specified.",
                err=True,
            )
        return input_file.read()
    elif input_string is not None:
        return input_string
    else:
        typer.echo(
            "Error: Either a string or a file is required as input. See help with '--help'.",
            err=True,
        )
        raise typer.Exit(code=1)


def write_output(output_file: typer.FileTextWrite, output_data: str):
    if output_file is not None:
        output_file.write(output_data)
        if output_file is not sys.stdout:
            typer.echo(f"Output written to: {path.realpath(output_file.name)}")
    else:
        typer.echo(output_data)


def check_scheme(scheme_name: str):
    if scheme_name not in scheme_names:
        error_msg = f"Invalid scheme name. {scheme_help}"
        raise typer.BadParameter(error_msg)
    return scheme_name


typer_opt_from_scheme = typer.Option(
    ...,
    "--from",
    "-f",
    help=help_text.from_scheme,
    callback=check_scheme,
)

typer_opt_to_scheme = typer.Option(
    ...,
    "--to",
    "-t",
    help=help_text.to_scheme,
    callback=check_scheme,
)

typer_opt_input_file = typer.Option(
    None,
    "--input-file",
    "-i",
    help=help_text.input_file,
)

typer_opt_output_file = typer.Option(
    None, "--output-file", "-o", help=help_text.output_file
)

typer_arg_input_string = typer.Argument(
    None,
    help=help_text.input_string,
)


@app.command(help=help_text.program)
def main(
    from_scheme: str = typer_opt_from_scheme,
    to_scheme: str = typer_opt_to_scheme,
    input_file: Optional[typer.FileText] = typer_opt_input_file,
    output_file: Optional[typer.FileTextWrite] = typer_opt_output_file,
    input_string: Optional[str] = typer_arg_input_string,
):
    scheme_map = SchemeMap(SCHEMES[from_scheme], SCHEMES[to_scheme])
    input_data = get_input_data(input_file, input_string)

    output_data = transliterate(input_data, scheme_map=scheme_map)
    write_output(output_file, output_data)


if __name__ == "__main__":
    app()
