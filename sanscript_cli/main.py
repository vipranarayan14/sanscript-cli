from typing import Optional

import typer
from indic_transliteration.sanscript import transliterate, SCHEMES, SchemeMap

from sanscript_cli.help_text import program as program_help
from sanscript_cli.typer_opts import (
    from_scheme,
    input_file,
    input_string,
    output_file,
    to_scheme,
)
from sanscript_cli.utils import get_input_data, write_output

app = typer.Typer()


@app.command(help=program_help)
def main(
    from_scheme: str = from_scheme,
    to_scheme: str = to_scheme,
    input_file: Optional[typer.FileText] = input_file,
    output_file: Optional[typer.FileTextWrite] = output_file,
    input_string: Optional[str] = input_string,
):
    scheme_map = SchemeMap(SCHEMES[from_scheme], SCHEMES[to_scheme])
    input_data = get_input_data(input_file, input_string)

    output_data = transliterate(input_data, scheme_map=scheme_map)
    write_output(output_file, output_data)


if __name__ == "__main__":
    app()
