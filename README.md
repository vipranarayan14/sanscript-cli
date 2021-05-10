# sanscript-cli

A CLI for indic script transliteration based on "indic-transliteration" python library.

See [the library's homepage](https://github.com/sanskrit-coders/indic_transliteration) for supported scripts/schemes.

## Usage

```sh
sanscript-cli [OPTIONS] [INPUT_STRING]
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

For more info: https://github.com/sanskrit-coders/indic_transliteration
