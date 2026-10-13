# Equatorial Guinea (GQ) — legislación en Markdown

Part of [LawCodex](https://github.com/LawCodex): the legislation of every country as plain Markdown in git.

**Minimal repository: the Fundamental Law (Constitution) of the Republic of Equatorial Guinea**, in Spanish.

Retrieved 2026-10-13.

<!-- COUNTS -->
| Directory | Files |
|---|---|
| `constitucion/` | 1 |
| **Total** | **1** |
<!-- /COUNTS -->

## Contents

```
constitucion/ley-fundamental-2012.md   Ley Fundamental de Guinea Ecuatorial — new text of the Constitution with the
                                       reform approved by referendum on 13 November 2011, promulgated 16 February 2012
```

## Source

| Document | URL |
|---|---|
| Ley Fundamental — Oficina de Información y Prensa de Guinea Ecuatorial (Government press office) | https://www.guineaecuatorialpress.com/pdf/Ley_Fundamental_Guinea_Ecuatorial.pdf |
| Internet Archive capture used (31 October 2020) | https://web.archive.org/web/20201031130303id_/https://www.guineaecuatorialpress.com/pdf/Ley_Fundamental_Guinea_Ecuatorial.pdf |

The live file on the official site currently returns an empty (0-page) PDF, so the Internet Archive capture of the
same official URL is used (identical to the 2012 publication `imgdb/2012/LEYFUNDAMENTALREFORMADA.pdf` on the same
site). The first sentence of the preamble, scattered by the PDF's justified layout, was reassembled; all other text
is as extracted.

## Not covered / known gaps

* **No ordinary legislation.** No official online collection of Equato-Guinean laws (Boletín Oficial del Estado)
  could be found: the domains of the Presidency, Parliament (Cámara de los Diputados, Senado), Constitutional
  Court and Ministry of Justice did not answer; gob.gq redirects to the press office site, which only publishes
  occasional decrees and news (mostly scans). Internet Archive copies of that site contain no further laws as text.
* Later constitutional amendments, if any, are not included; the text is the 2012 consolidated version published
  by the Government.
* Only Spanish (French and Portuguese are also official languages; no versions found).

## Copyright

Official text of the Republic of Equatorial Guinea published by the Government press office without stated reuse
restrictions; official legislative texts are generally not subject to copyright. The Markdown conversion is
provided as is.

## Regenerating

```sh
python3 scripts/gq_fetch.py    # downloads the archived PDF to ../_raw/gq/ and writes the Markdown
python3 scripts/gq_readme.py   # updates the counts table
```
