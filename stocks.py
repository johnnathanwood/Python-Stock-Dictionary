# Instructions
# A block of publicly traded stock has a variety of attributes. Let's look at a few of them. A stock has a ticker symbol and a company name. Create a simple dictionary with ticker symbols and company names.

# Example
# stockDict = { 'GM': 'General Motors',
#  'CAT':'Caterpillar', 'EK':"Eastman Kodak" }
# Create a simple list of blocks of stock. These could be tuples with ticker symbols, number of shares, dates and price.

# Example
# purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
#  ( 'CAT', 100, '1-apr-1999', 24 ),
#  ( 'GE', 200, '1-jul-1998', 56 ) ]
# Create a purchase history report that computes the full purchase price (shares times dollars) for each block of stock and uses the stockDict to look up the full company name. This is the basic relational database join algorithm between two tables.
# Example output for one block: I purchased General Electric stock for $4800

# Create a second purchase summary that which accumulates total investment by ticker symbol. In the above sample data, there are two blocks of GE. These can easily be combined by creating a dict where the key is the ticker and the value is the list of blocks purchased. The program makes one pass through the data to create the dict. A pass through the dict can then create a report showing each ticker symbol and all blocks of stock.

# Example output:

# ------ GE ------
#     ('GE', 100, '10-sep-2001', 48)
#     ('GE', 200, '1-jul-1998', 56)
# Total value of stock in portfolio: $16000

purchases = [ ( 'GE', 100, '10-sep-2001', 48 ),
 ( 'CAT', 100, '1-apr-1999', 24 ),
 ( 'GE', 200, '1-jul-1998', 56 ) ]


stockDict = { 'GM': 'General Motors',
 'CAT':'Caterpillar', 'EK':"Eastman Kodak", "GE": "General Electric" }


report = {}
for purchase in purchases:
    abbrev = purchase[0]
    full_name = stockDict[abbrev]
    no_of_shares = purchase[1]
    purch_date = purchase[2]
    purch_price = purchase[3]
    full_purchase_price = no_of_shares * purch_price
    print("I purchases {0} stock on {1} for ${2}.".format(full_name,purch_date,full_purchase_price))

    try:
        report[abbrev].append(purchase)
    except KeyError:
            report[abbrev] = list()
            report[abbrev].append(purchase)

for abbrev, purchases in report.items():
    print("-----{0}-----".format(abbrev))
    total_portfolio_stock_value = 0
    for purchase in purchases:
        total_portfolio_stock_value += purchase[1] * purchase[3]
        print(" {0}".format(purchase))
    print("Total value of stock in portfolio: ${0}\n\n".format(total_portfolio_stock_value))


# Comprehensions

flowers = ['Lily', 'Snapdragon', 'Rose', 'Tulip']

bees = ['bumblebee', 'honeybee', 'dobee', 'aybee']

flowers_quotes = ["{0}s make me sneeze".format(flower) for flower in flowers]

print(flowers_quotes)

large_flowers = []
for flower in flowers:
    for bee in bees:
        large_flowers.append('The {0} pollinates the {1}.'.format(bee,flower))

print(large_flowers)

large_flowers = [
    'The {0} pollinates the {1}.'.format(bee,flower)
    for flower in flowers
    for bee in bees
]

print(large_flowers)
