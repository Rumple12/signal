# 2026-08-18, Uppgift 6: workflow-test report

**PASS: actual LaTeX-to-PNG export, using the typed solution images expressly approved by the user.**

Review date: 2026-10-25. This is an export/transcription test using approved typed sources. The original handwriting alone does not contain completed solutions for parts (a) or (b).

## Verified source mapping

| Exam ID | Question | Part | PDF source | Genuine handwriting | Approved solution source |
|---|---|---|---|---|---|
| 2026-08-18 | Uppgift 6 | a | [Original exam, PDF page 4 / printed page 3](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/2026-08 exam.pdf>) | [Dated unfinished common fragment](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/exaam/exaam/IMG_20261024_155408.jpg>); no complete (a) | [Typed 6 68a.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6/6 68a.jpg>) |
| 2026-08-18 | Uppgift 6 | b | Same verified exam and page | Same fragment; no complete (b) | [Typed 6 68b.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/signal calc/6/6 68b.jpg>) |

The user explicitly answered **Use the existing typed solutions**. Those files were inspected and matched to the original question by their actual wording, Bayer diagram, and subparts, rather than by filename alone.

The original photo collection contains 36 images. Its headings and date variants were checked. The matching handwritten fragment contains the dated Question 6 heading, a search reminder, and the statement that each pixel measures only one color. [6 68 f.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/6 68 f.png>) is a crop of that fragment. [6 68.jpg](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal tenta/2026-08/6 68.jpg>) concerns compression and was excluded. January 2026 and August 2025 content on the same raw page was excluded.

## Stage results

| Stage | Result | Evidence |
|---|---|---|
| Original exam found | PASS | Exact 2026-08-18 exam; Question 6 on PDF page 4. |
| Completed handwriting found | NEEDS REVIEW | No complete handwritten (a)/(b); only an unfinished common fragment. |
| Alternate sources approved | PASS | User approved the two existing typed solution images. |
| Original question transcribed | PASS | Complete wording, both subparts, hint, both (2p) allocations, original Bayer diagram and legend. |
| Solution transcription | PASS | Approved source method/order/examples/intermediate values/final answers retained. No independent replacement solution. |
| Authoritative dated source | PASS | One dated source; prior completed Question 2(b) migrated and preserved. Older entry points now delegate. |
| Automatic part discovery | PASS | One exam/question command discovers a and b, with no per-letter prompt. |
| Separate PNG generation | PASS | Two actual LaTeX-to-PNG exports completed, one per part. |
| Width and source-question placement | PASS | Both 384px; all original question paragraphs occur before each corresponding solution. |
| Math/figure clipping | PASS | No overfull boxes/missing glyphs; text/math/image bounds checked on all PDF pages; final PNGs inspected. |
| Actual-size readability | PASS | Both final 256-color PNGs viewed at native 384px width, including all content and page joins. |
| Repeat command | PASS | Repeated export produced byte-identical PNG checksums. |
| Missing-source behavior | PASS | In-memory Question 6 tests: missing b is listed incomplete; all missing returns exit 2 without exporting. |
| Original-input preservation | PASS | 41 original inputs match their existing Git blobs; export also checked before/after SHA-256 hashes. |
| Ready for additional questions | PASS, scoped | Reusable exporter is ready for new verified transcriptions/registrations. Only this exact Question 6 was export-tested. |

## Final images

| Part | Final PNG | Dimensions | Size |
|---|---|---|---|
| a | [2026-08-18_Q06_a_bayer.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/calcu formats/signal calcu/7 Cameras Bayer and demosaicing/2026-08-18_Q06_a_bayer.png>) | 384 x 1259 | 119110 bytes (116.3 KiB) |
| b | [2026-08-18_Q06_b_demosaicing.png](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/calcu formats/signal calcu/7 Cameras Bayer and demosaicing/2026-08-18_Q06_b_demosaicing.png>) | 384 x 1557 | 123871 bytes (121.0 KiB) |

Each final image begins with the entire original multipart Question 6, including its original Bayer figure. Each is assembled vertically from two 384pt x 900pt PDF pages with unused page margins removed; no mathematical expressions are cropped or sliced.

## Source, converter, and repeat command

- Authoritative TeX: [2026-08-18_compiled_notes.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/2026-08-18_compiled_notes.tex>)
- Conversion script: [export_notes.py](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/export_notes.py>)
- Shared layout: [signal_layout.tex](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/signal_layout.tex>)
- Reuse instructions: [README.md](<C:/Users/Jake_/OneDrive - Mittuniversitetet/1. EDU/1.1 GREEN/15. DT081A Signal and Image Processing/tenta/signal latex/README.md>)

Exact PowerShell command, usable from any directory:

```powershell
& 'C:\Users\Jake_\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -B 'C:\Users\Jake_\OneDrive - Mittuniversitetet\1. EDU\1.1 GREEN\15. DT081A Signal and Image Processing\tenta\signal latex\export_notes.py' --exam 2026-08-18 --question 6
```

Append `--list` to inspect the completed/incomplete subquestions without rendering. Intermediate PDFs, wrappers, logs, raster pages and the machine validation JSON are outside source/final directories, under `tmp/pdfs/signal-export/2026-08-18/Q06/`.

## Uncertainties and scope

- The crossed-out search keyword in the genuine handwritten fragment is not fully readable. An uncertainty comment preserves this fact in the TeX; the word is not guessed. The fragment is not presented as a completed handwritten answer.
- No unresolved mathematical uncertainty was found in the approved typed solutions. The red-pixel example preserves R = 180, G = (100+120+110+130)/4 = 115, B = (70+90+80+100)/4 = 85, and final RGB = (180,115,85).
- The sums 460/4 and 340/4 are small directly implied arithmetic steps. No additional independent reasoning was required; repeated summaries were consolidated.
- This test establishes verified typed-source transcription and automatic subquestion export. It does not establish automatic handwriting recognition, or claim that the unfinished handwriting was complete.
- Other questions/exam dates were not batch-exported. They require verified question/solution transcriptions and the same source metadata before the exporter can process them.

## Final PNG checksums

- 2026-08-18_Q06_a_bayer.png: `8e37f2a49f98fe492d9cafa8a78a59f3af733685f7745cb93a19f9dbb47241ea`
- 2026-08-18_Q06_b_demosaicing.png: `8ed5bf90c3dcb93ad9fb8a509e39be4fb50bc511ba29e9dbb9f5819d54f9f94d`
