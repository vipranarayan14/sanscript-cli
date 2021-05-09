from typing import Optional

import typer
from indic_transliteration.sanscript import transliterate, SCHEMES, SchemeMap

import help_text
from utils import get_input_data, write_output

app = typer.Typer()

scheme_names = list(SCHEMES.keys())

scheme_help = "Choose from: {}.".format(", ".join(scheme_names))


def check_scheme(scheme_name: str):
    if scheme_name in scheme_names:
        return scheme_name

    error_msg = f"Invalid scheme name. \n\n{scheme_help}"
    raise typer.BadParameter(error_msg)


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
