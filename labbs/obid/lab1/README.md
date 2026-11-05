# Lab 1, Sections 1.1 and 1.2 — Jakob Obid

Sections 1.1 and 1.2 are implemented. The script starts from the teacher's time vector and original signal expressions.

From the repository root, with NumPy and Matplotlib installed:

    python labbs/obid/lab1/code/section1_1.py

Run Section 1.2 with:

    python labbs/obid/lab1/code/section1_2.py

Each script prints its results, saves three figures and opens the plots. Close the plot windows to finish.

Files:
- code/section1_1.py: all five questions' signal calculations and three plots.
- figures/q1_sawtooth.png: 5 Hz repeating ramp.
- figures/q2_sine_frequencies.png: separate 10 Hz and 20 Hz panels.
- figures/q4_composite.png: original 10 Hz sine plus 5 Hz square.
- code/section1_2.py: Fourier analysis, added 30 Hz wave, Gaussian noise and chirp.
- figures/section1_2_original_fft.png: original signal and FFT.
- figures/section1_2_spectra_comparison.png: original, modified and noisy spectra.
- figures/section1_2_chirp_fft.png: 15–65 Hz chirp and its FFT.
- report/main.tex: editable Sections 1.1–1.2 report.
- report/DT081A_Lab1_Report_Jakob_Obid.pdf: compiled report.

To compile the report, run pdflatex twice from labbs/obid/lab1/report/:

    pdflatex -jobname=DT081A_Lab1_Report_Jakob_Obid main.tex

Q3 differs only at sample 0 (time 0): original 0, replacement -1. The remaining 999 samples match. The replacement can give -3 at an exact sine value of -1, but that value does not occur with this time vector.

The report uses the name Jakob Obid exactly as supplied in the task. No email was supplied. The reports and code in labbs/lab1, labbs/lab2 and labbs/lab3 have not been edited.
