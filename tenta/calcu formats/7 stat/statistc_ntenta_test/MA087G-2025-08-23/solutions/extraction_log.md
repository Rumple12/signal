# Extraction log: MA087G-2025-08-23

Generated: 2026-05-01

## Folder inspected

Target folder:

`MA087G-2025-08-23`

## PDFs found

| File | Role | Pages | Embedded text | Readability |
|---|---:|---:|---:|---|
| `2025-08 tenta.pdf` | Official exam paper | 3 | No extractable text | Readable after rendering to images |
| `9BW8JD9L0000_Grade-D.pdf` | Student attempt, Grade D | 7 | No extractable text | Readable after rendering to images |
| `E2EBCMR20000_Grade-E.pdf` | Student attempt, Grade E | 9 | No extractable text | Readable after rendering to images, but some handwriting is faint |
| `JMXGPJAG0000_Grade-C.pdf` | Student attempt, Grade C | 15 | No extractable text | Readable after rendering to images |
| `MCS7UC8W0000_Grade-D.pdf` | Student attempt, Grade D | 11 | No extractable text | Readable after rendering to images |

## Extraction method

- `pypdf` could open all PDFs and count pages.
- `pypdf` extracted 0 text characters from every page, so all PDFs are image-only/scanned PDFs.
- `PyMuPDF` was used to render pages to PNG images.
- Rendered page images were saved in:

`MA087G-2025-08-23/solutions/_extracted_pages/`

## Official exam questions recovered

All official questions were readable from the rendered official exam:

- Uppgift 1: conditional probability with complements
- Uppgift 2: continuous density, CDF, probability, expected value, standard deviation
- Uppgift 3: Poisson probabilities, maximum of independent variables, linear combination
- Uppgift 4: ML estimate for parameter in density `theta x^(theta-1)`
- Uppgift 5: point estimate and confidence interval for normal standard deviation
- Uppgift 6: one-sided hypothesis test for mean with known sigma, plus sample size/power

## Source uncertainties and caveats

1. Uppgift 3c is visually unclear in the official scan.
   - The sensible/intended reading appears to be `Y = X_2 - 2X_1`, also matching student attempts.
   - The solution guide solves `Y = X_2 - 2X_1`.
   - If read literally as `Y = X_2 - 2X_2 = -X_2`, then `E(Y)=-2` but `V(Y)=2`, not `10`.

2. No PDF was corrupt or unreadable.

## Style update

The requested master-prompt style change was applied to this solution guide:

- extremely beginner-friendly,
- full hand-holding,
- symbol explanations before formulas,
- baby-step calculations,
- expanded per-question structure.

No separate master prompt file was found in the workspace, so no prompt file was edited.

## Cross-exam pattern memory

The current pattern tracker was seeded from the already processed folder:

`MA087G-2026-01-07/solutions/pattern_tracker.md`

Repeated patterns were linked where appropriate, especially:

- 2025-08 Uppgift 1 with 2026-01 Uppgift 1
- 2025-08 Uppgift 2 with 2026-01 Uppgift 2
- 2025-08 Uppgift 4 with 2026-01 Uppgift 5
- 2025-08 Uppgift 6 with 2026-01 Uppgift 6
