This directory contains **almost** everything needed for
**Chapter 17 (Build Prediction Models)** in
[*Computational Thinking and Problem Solving (CTPS)*](https://profsmith89.github.io/ctps/ctps.html)
by Michael D. Smith.

The chapter describes how you can download
the Ames Iowa Housing data from Kaggle, which you need as
input for the scripts.

`head.py`: Prints the first 5 rows of the specified CSV file.
This script assumes that the input file has a header row.

`get_header.py`: Jim Waldo's utility that grabs the header
from a CSV file and writes each column label on a separate
indexed line.

`avg_pbbr.py`: Computes the average home price by count
of bedrooms. Custom-made for the Ames-Iowa-Housing data set.

`desc.py`: Reads tabular CSV data into a Panda DataFrame
and uses `pandas.DataFrame.describe` to print some descriptive
statistics by column.

`ames.ipynb`: A Python notebook containing the code used
in Chapter 17 to investigate the Ames-Iowa-Housing data
and fit a predictive model based on decision trees.
