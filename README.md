This directory contains **almost** everything needed for
**Chapter 17 (Build Prediction Models)** in
*Computational Thinking and Problem Solving*.

Almost defined: The chapter describes how you can download
the Ames Iowa Housing data from Kaggle, which you need as
input for the scripts.

`head.py`: Prints the first 5 rows of the specified CSV file.

`get_header.py`: Jim Waldo's utility that grabs the header
from a CSV file and writes each column label on a separate
indexed line.

`avg_pbbr.py`: Computes the average home price by count
of bedrooms.

`desc.py`: Reads tabular CSV data into a Panda DataFrame
and uses `pandas.DataFrame.describe` to print some descriptive
statistics by column.

`ames.ipynb`: A Python notebook containing the code used
in Chapter 17 to investigate the Ames-Iowa-Housing data
and fit a predictive model based on decision trees.
