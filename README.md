# sanscript-cli

A CLI for indic script transliteration based on [indic-transliteration](https://github.com/sanskrit-coders/indic_transliteration) python library.

See the library's homepage for supported scripts/schemes and other information.

## Installation

Download the wheel file from the [releases](https://github.com/vipranarayan14/sanscript-cli/releases) page and use [`pip` to install](https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels).

```sh
$ pip install -U sanscript_cli-xxx.whl
```

## Usage

```sh
sanscript [OPTIONS] [INPUT_STRING]
```

Input can be:

- from command's argument

  Example:

  ```sh
  $ sanscript --from hk --to iast "rAmAyaNa"
  ```

  Output: `rāmāyaṇa`

- from file passed to '--input-file / -i' option

  Example:

  ```sh
  $ sanscript --from hk --to iast -i ramayana.txt
  ```

  Output: `rāmāyaṇa`

- from Standard Input using '-'

  Example:

  ```sh
  $ cat ramayana.txt | sanscript --from hk --to iast -i -
  ```

  OR:

  ```sh
  $ sanscript --from hk --to iast -i - < ramayana.txt
  ```

  Output: `rāmāyaṇa`

Output can be:

- to Standard Output

  Example:

  ```sh
  $ sanscript --from hk --to iast "rAmAyaNa"
  ```

  OR:

  ```sh
  $ sanscript --from hk --to iast "rAmAyaNa" -o -
  ```

  Output: `rāmāyaṇa`

- to file passed '--ouput-file / -o' option

  Example:

  ```sh
  $ sanscript --from hk --to iast "rAmAyaNa" -o output.txt
  ```

  Output:

  ```
  Output written to: /home/user/output.txt
  ```

## License

MIT
