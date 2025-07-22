### chap17/avg_pbbr.py -- custom-made for Ames-Iowa-Housing data set
import sys, csv

# Each `homes` element is a tuple with these elements:
# 1. count of homes with a number of bedrooms equal to the index
# 2. total sales price for all such homes
MAX_BEDROOMS = 9
homes = [
    (0, 0), (0, 0), (0, 0), (0, 0),
    (0, 0), (0, 0), (0, 0), (0, 0),
    (0, 0), (0, 0),
]

def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: avg_pbbr.py input.csv')

    with open(sys.argv[1], encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            # Grab this entry's number of bedrooms
            num_bedrooms = int(row['Bedroom AbvGr'])
            assert num_bedrooms <= MAX_BEDROOMS, f"We need a bigger list ({num_bedrooms})"

            # Grab its sales price
            price = int(row['SalePrice'])

            # Update the right tuple in homes
            homes[num_bedrooms] = (
                homes[num_bedrooms][0] + 1,
                homes[num_bedrooms][1] + price
            )

        # Print out the results
        for i, t in enumerate(homes):
            if t[0] != 0:
                print(f'Avg. sale price of {t[0]:>{4}} homes with {i} bedrooms: ', end='$')
                print(format(t[1]/t[0], '.2f'))

if __name__ == '__main__':
    main()
