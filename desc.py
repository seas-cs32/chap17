### chap17/desc.py
import sys
import pandas as pd

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: desc.py input.csv')

    # Read the CSV data into a DataFrame
    df = pd.read_csv(sys.argv[1])

    # Print a summary of the data
    print(df.describe())

if __name__ == '__main__':
    main()
