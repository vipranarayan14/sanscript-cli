import typer

from enum import Enum
from indic_transliteration.sanscript import transliterate, SCHEMES

scheme_names = list(SCHEMES.keys())

scheme_help = "Choose from: {}.".format(", ".join(scheme_names))


def check_scheme(scheme_name: str):
    if not scheme_name in scheme_names:
        error_msg = f"Invalid scheme name. {scheme_help}"
        raise typer.BadParameter(error_msg)
    return scheme_name


typer_option_from_scheme = typer.Option(
    ...,
    "--from",
    help=f"Name of the scheme FROM which the input is to be transliterated."
    "\n\n"
    f"{scheme_help}",
    callback=check_scheme,
)

typer_option_to_scheme = typer.Option(
    ...,
    "--to",
    help=f"Name of the scheme TO which the input is to be transliterated."
    "\n\n"
    f"{scheme_help}",
    callback=check_scheme,
)


def main(
    input: str,
    from_scheme: str = typer_option_from_scheme,
    to_scheme: str = typer_option_to_scheme,
):
    pass
    output = transliterate(input, from_scheme, to_scheme)
    typer.echo(output)


if __name__ == "__main__":
    typer.run(main)
