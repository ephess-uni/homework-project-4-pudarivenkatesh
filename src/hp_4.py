# hp_4.py
#
from datetime import datetime, timedelta
from csv import DictReader, DictWriter
from collections import defaultdict


def reformat_dates(old_dates):
    """Accepts a list of date strings in format yyyy-mm-dd, re-formats each
    element to a format dd mmm yyyy--01 Jan 2001."""
    new_dates = []
    for old_date in old_dates:
        new_date = datetime.strptime(old_date, "%Y-%m-%d").strftime("%d %b %Y")
        new_dates.append(new_date)
    return new_dates
        


def date_range(start, n):
    """For input date string `start`, with format 'yyyy-mm-dd', returns
    a list of of `n` datetime objects starting at `start` where each
    element in the list is one day after the previous."""
    new_dates = []
    start_date = datetime.strptime(start, "%Y-%m-%d")
    for i in range(n):
        new_date =  start_date + timedelta(days=i)
        new_dates.append(new_date)
    return new_dates
        


def add_date_range(values, start_date):
    """Adds a daily date range to the list `values` beginning with
    `start_date`.  The date, value pairs are returned as tuples
    in the returned list."""
    new_dates  = []
    start_Date = datetime.strptime(start_date,"%Y-%m-%d")
    for pos,val in enumerate(values):
        new_dates.append((start_date+timedelta(days=pos),val))
    return new_dates


def fees_report(infile, outfile):
    """Calculates late fees per patron id and writes a summary report to
    outfile."""
    late_fees_dict = defaultdict(float)
    with open(infile,'r') as file:
        reader = DictReader(file)
        for row in reader:
            date_due = datetime.strptime(row['date_due'],"%m/%d/%Y")
            date_returned = datetime.strptime(row['date_returned'],"%m/%d/%Y")
            if date_returned > date_due:
                days_late = (date_returned - date_due).days
                late_fee = days_late * 0.25
                late_fees_dict[row['patron_id']] += late_fee
    with open(outfile,'w',newline='') as file:
        writer = writer(file)
        writer.writerow(['patron_id','late_fees'])
        for patroon_id,late_fee  in late_fees_dict.items():
            write.writerow([patron_id, '{:.2f}'.format(late_fee)])
            


# The following main selection block will only run when you choose
# "Run -> Module" in IDLE.  Use this section to run test code.  The
# template code below tests the fees_report function.
#
# Use the get_data_file_path function to get the full path of any file
# under the data directory.

if __name__ == '__main__':
    
    try:
        from src.util import get_data_file_path
    except ImportError:
        from util import get_data_file_path

    # BOOK_RETURNS_PATH = get_data_file_path('book_returns.csv')
    BOOK_RETURNS_PATH = get_data_file_path('book_returns_short.csv')

    OUTFILE = 'book_fees.csv'

    fees_report(BOOK_RETURNS_PATH, OUTFILE)

    # Print the data written to the outfile
    with open(OUTFILE) as f:
        print(f.read())
