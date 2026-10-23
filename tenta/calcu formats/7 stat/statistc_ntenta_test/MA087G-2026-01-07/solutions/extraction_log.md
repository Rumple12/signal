# Extraction log: MA087G-2026-01-07

Generated: 2026-04-30

## Folder inspected

Target folder:

`MA087G-2026-01-07`

## PDFs found

| File | Role | Pages | Embedded text | Readability |
|---|---:|---:|---:|---|
| `2026-01 tenta.pdf` | Official exam paper | 3 | No extractable text | Readable after rendering to images |
| `5ILRSBDM0000_Grade-D.pdf` | Student attempt, Grade D | 12 | No extractable text | Readable after rendering to images |

## Extraction method

- `pypdf` could open both PDFs and count pages.
- `pypdf` extracted 0 text characters from every page, so both PDFs are image-only/scanned PDFs.
- `PyMuPDF` was installed and used to render pages to PNG images.
- Rendered page images were saved in:

`MA087G-2026-01-07/solutions/_extracted_pages/`

## Official exam questions recovered

All official questions were readable from the rendered images:

- Uppgift 1: events, independence, conditional probability
- Uppgift 2: continuous density/CDF/moments
- Uppgift 3: minimum of two independent exponential variables
- Uppgift 4: discrete distribution and normal linear combination
- Uppgift 5: maximum likelihood for geometric-type distribution
- Uppgift 6: confidence interval and hypothesis test for mean

## Source uncertainties and caveats

1. Uppgift 2 contains an internal inconsistency:
   - The main displayed density is `f(x)=a x^2(2-x)` for `0 <= x <= 2`.
   - The printed fallback comment says to use `f(x)=5x^3(2-x)/8`, which corresponds to a different density.
   - The solution guide solves the main displayed density and also reports the fallback answers.

2. Uppgift 4b does not explicitly state that `X` and `Y` are independent.
   - Independence is required to compute the variance of the taxi cost from the given information.
   - The solution guide uses the standard exam assumption of independence and flags this assumption.

## Cross-exam pattern memory status

No existing `solutions/` folders or `pattern_tracker.md` files were found in the older exam folders at the time of processing. Therefore this exam seeds the first pattern tracker for later folders.
