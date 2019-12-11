import io
import os 
import re 

import pandas as pd

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 

pdf = 'roo_Invoices/invoice_9256ec7b_1279_48e4_ba52_bd1550587036_2.pdf'

def extract_text(pdf_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle)
    page_interpreter = PDFPageInterpreter(resource_manager, converter)
 
    with open(pdf_path, 'rb') as fh:
        for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
 
        text = fake_file_handle.getvalue()
 
    # close open handles
    converter.close()
    fake_file_handle.close()
 
    if text:
        return text

def create_summary_df(text):
    s = text.split('Summary')[1] # Take all text after 'Summary'
    split = re.split('(.\d+.\d+)',s) # Split based £xx.xx where x is a didget
    for i in range(len(split)): # Remove weird thing
        if split[i] == "\x0c":
            split.remove(split[i])

    names = []
    values = [] 
    for i in range(len(split)): # Deinterleave list into names and values
        if (i % 2) == 0:
            names.append(split[i])
        else:
            values.append(split[i])
    # Create pandas dataframe from names and values
    df = pd.DataFrame(
        {
            'names': names,
            'values': values
        }
    )
    return(df)

def create_df(text):
    s = text.split('Summary')[0] # Take all text before 'Summary'
    #s = text.split('Fee Adjustments')[0] # Take all text before 'Summary'
    s = s.split('DayDateTime')[1]

    with open("raw.txt", "w") as raw:
        raw.write(s)
    # get time in and out as one then split
    t = re.findall('..:....:..',s) # re for time in
    ti = [i [ :int(len(i)/2)] for i in t]
    to = [i [int(len(i)/2): ] for i in t]

    h = re.findall('\d{1,2}.\d?h', s) # re for hours
    d = re.findall('\d{2}\D{3,}\d{4}',s) # re for date
    # v = re.findall('£\d{1,}.\d{2}',s)
    ov = re.findall('\d*: £\d{1,}.\d{2}',s) # get number of orders and value in £
    o = [i.split(': ')[0] for i in ov] # Split into orders and value 
    v = [i.split(': ')[1] for i in ov]

    day = re.findall('(Mon|Tues|Wed|Thurs|Fri|Sat|Sun)day', s)

    #print(s)
    print(str(day) + '\n' + str(d) + '\n' + str(ti) + '\n' + str(to) + '\n' + str(h) + '\n' + str(o) + '\n' + str(v))

    df = pd.DataFrame(
        {
            'Day': day,
            'Date': d,
            'Time_in': ti,
            'Time_out': to,
            'Hours_worked': h,
            'Orders': o,
            'Total': v
        }
    )

    return df

if __name__ == '__main__':
    text = extract_text(pdf)
    summary_df = create_summary_df(text)
    df = create_df(text)
    print(summary_df)
    print(df)
    #os.system('open ' + pdf)
