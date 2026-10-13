#!/usr/bin/env python3
"""Equatorial Guinea: Ley Fundamental (Constitution) as reformed in 2011 and promulgated on 16 February 2012,
published by the Government's official press office (guineaecuatorialpress.com). The live PDF is currently broken
(0 pages), so the Internet Archive capture of the same official URL is used.
Usage: python3 gq_fetch.py [--no-download]"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gq_text as T  # noqa

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(os.path.dirname(REPO), "_raw", "gq")
RETRIEVED = os.environ.get("LC_RETRIEVED", "2026-10-13")
URL = "https://www.guineaecuatorialpress.com/pdf/Ley_Fundamental_Guinea_Ecuatorial.pdf"
ARCHIVED = "https://web.archive.org/web/20201031130303id_/" + URL


def main():
    pdf = os.path.join(RAW, "ley-fundamental.pdf")
    if "--no-download" not in sys.argv:
        T.fetch(ARCHIVED, pdf, delay=3, check_pdf=True)
    if not T.pdf_ok(pdf):
        raise SystemExit("bad pdf")
    pages, _ = T.pdf_text(pdf, "spa", tmpdir=RAW, ocr=False)
    lines = T.clean_pages(pages)
    st = next(i for i, x in enumerate(lines) if x == "PREÁMBULO")
    lines = [x for x in lines[st + 1:] if not re.match(r"^[‐\-–]\s*\d+\s*[‐\-–]$", x)]
    # the first sentence of the preamble is justified across a wide line: pdftotext scatters its words
    head = "Nosotros, Pueblo de Guinea Ecuatorial, conscientes de nuestra responsabilidad ante Dios y la Historia."
    i = lines.index("Nosotros, Pueblo de Guinea")
    seg = [x for x in lines[i:i + 12] if x]
    if seg[:6] == ["Nosotros, Pueblo de Guinea", "responsabilidad ante Dios y la Historia.", "Ecuatorial,", "conscientes", "de", "nuestra"]:
        j, k = i, 0
        while k < 6:
            if lines[j]:
                k += 1
            j += 1
        lines[i:j] = [head, ""]
    body = ["## Preámbulo", ""] + T.structure(lines, "es")
    meta = {"title": "Ley Fundamental de Guinea Ecuatorial", "identifier": "Ley Fundamental de Guinea Ecuatorial (texto reformado, promulgado el 16 de febrero de 2012)",
            "type": "constitution", "jurisdiction": "gq", "language": "es", "date": "2012-02-16", "status": "in_force",
            "source": URL, "archived_source": ARCHIVED, "retrieved": RETRIEVED,
            "note": "New text of the Constitution with the constitutional reform approved by referendum on 13 November 2011, as published by the Government press office"}
    T.write_md(os.path.join(REPO, "constitucion", "ley-fundamental-2012.md"), meta, meta["title"], body)
    print("OK", sum(1 for x in body if x.startswith("#") and "Artículo" in x), "articles")


if __name__ == "__main__":
    main()
