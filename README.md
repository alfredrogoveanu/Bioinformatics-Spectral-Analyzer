# Spectral Analyzer

Student: ROGOVEANU Alfred (1240F)

An implementation after: Paul A. Gagniuc et al. Spectral forecast: A general purpose prediction model as an alternative to classical neural networks. Chaos 30, 033119 (2020); doi: 10.1063/1.5120818 (https://aip.scitation.org/doi/10.1063/1.5120818)

The following equation was implemented in Python:

<a href="https://www.codecogs.com/eqnedit.php?latex=M_{ijd}&space;=&space;[(\frac{d}{Max(A_{ij})})\times&space;A_{ij}]&plus;[(\frac{Max(d)-d}{Max(B_{ij})})\times&space;B_{ij}]" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{ijd}&space;=&space;[(\frac{d}{Max(A_{ij})})\times&space;A_{ij}]&plus;[(\frac{Max(d)-d}{Max(B_{ij})})\times&space;B_{ij}]" title="M_{ijd} = [(\frac{d}{Max(A_{ij})})\times A_{ij}]+[(\frac{Max(d)-d}{Max(B_{ij})})\times B_{ij}]" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=M_{ijd}" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{ijd}" title="M_{ijd}" /></a> represents the predicted matrix at every discrete step (<a href="https://www.codecogs.com/eqnedit.php?latex=d" target="_blank"><img src="https://latex.codecogs.com/png.latex?d" title="d" /></a>), <a href="https://www.codecogs.com/eqnedit.php?latex=A_{ij}" target="_blank"><img src="https://latex.codecogs.com/png.latex?A_{ij}" title="A_{ij}" /></a> represents the matrix of the normal group, and <a href="https://www.codecogs.com/eqnedit.php?latex=B_{ij}" target="_blank"><img src="https://latex.codecogs.com/png.latex?B_{ij}" title="B_{ij}" /></a> is the matrix associated with the diabetic group. Also, <a href="https://www.codecogs.com/eqnedit.php?latex=d" target="_blank"><img src="https://latex.codecogs.com/png.latex?d" title="d" /></a> stands for distance and represents the total number of discrete steps taken from matrix <a href="https://www.codecogs.com/eqnedit.php?latex=A" target="_blank"><img src="https://latex.codecogs.com/png.latex?A" title="A" /></a> to matrix <a href="https://www.codecogs.com/eqnedit.php?latex=B" target="_blank"><img src="https://latex.codecogs.com/png.latex?B" title="B" /></a>. Thus, <a href="https://www.codecogs.com/eqnedit.php?latex=M_{ijd}" target="_blank"><img src="https://latex.codecogs.com/png.latex?M_{ijd}" title="M_{ijd}" /></a> can be considered a 3D tensor-like structure.

The discrete step used in this particular implementation is 100. The <a href="https://www.codecogs.com/eqnedit.php?latex=A" target="_blank"><img src="https://latex.codecogs.com/png.latex?A" title="A" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=B" target="_blank"><img src="https://latex.codecogs.com/png.latex?B" title="B" /></a> matrixes are read from the *Matrix_A.txt* and *Matrix_B.txt* files. The resulting <a href="https://www.codecogs.com/eqnedit.php?latex=M" target="_blank"><img src="https://latex.codecogs.com/png.latex?M" title="M" /></a> matrix can be seen in the following charts, but also in the *Matrix_M.txt* file.

Additionally, one of the charts shows the <a href="https://www.codecogs.com/eqnedit.php?latex=M" target="_blank"><img src="https://latex.codecogs.com/png.latex?M" title="M" /></a> matrix in the form of a heat map, where red and dark red represent the higher values and blue to dark blue the lower values. Dark red represents 100, yellow represents 50 and dar blue represents 0.

## Heat map with values for the M matrix
![Alt text](https://github.com/alfredrogoveanu/Bioinformatics-Spectral-Analyzer/blob/master/Matrix_M_1.png?raw=true "Spectral Analyzer chart 1")

## Heat map without values for the M matrix
![Alt text](https://github.com/alfredrogoveanu/Bioinformatics-Spectral-Analyzer/blob/master/Matrix_M_3.png?raw=true "Spectral Analyzer chart 2")

## The values for the M matrix
![Alt text](https://github.com/alfredrogoveanu/Bioinformatics-Spectral-Analyzer/blob/master/Matrix_M_2.png?raw=true "Spectral Analyzer chart 3")

