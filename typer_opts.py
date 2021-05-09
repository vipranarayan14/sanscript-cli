import typer
from indic_transliteration.sanscript import SCHEMES

import help_text

scheme_names = list(SCHEMES.keys())
scheme_help = "Choose from: {}.".format(", ".join(scheme_names))


def check_scheme(scheme_name: str):
    if scheme_name in scheme_names:
        return scheme_name

    error_msg = f"Invalid scheme name. \n\n{scheme_help}"
    raise typer.BadParameter(error_msg)


from_scheme = typer.Option(
    ...,
    "--from",
    "-f",
    help=help_text.from_scheme,
    callback=check_scheme,
)

to_scheme = typer.Option(
    ...,
    "--to",
    "-t",
    help=help_text.to_scheme,
    callback=check_scheme,
)

input_file = typer.Option(
    None,
    "--input-file",
    "-i",
    help=help_text.input_file,
)

output_file = typer.Option(None, "--output-file", "-o", help=help_text.output_file)

input_string = typer.Argument(
    None,
    help=help_text.input_string,
)
