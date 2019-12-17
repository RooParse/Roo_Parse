
import io
import os 
import re 

import pandas as pd

from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
 
invoices = 'invoices'
pdf = 'invoices/invoice_9256ec7b_1279_48e4_ba52_bd1550587036_2.pdf'

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

def create_df(text):
    s = text.split('Summary')[0] # Take all text before 'Summary'
    s = s.split('DayDateTime')[1]
    s = s.split('Fee Adjustments')[0] # Take all text before 'Fee Adjustments'

    with open("raw.txt", "w") as raw:
        raw.write(s)
    # get time in and out as one then split
    t = re.findall('..:....:..',s) # re for time in
    ti = [i [ :int(len(i)/2)] for i in t]
    to = [i [int(len(i)/2): ] for i in t]

    h = re.findall(':..\d{1,2}.\d{1}h', s) # re for hours worked and :xx of time out
    h = [re.sub('h','' , i) for i in h] # remove h
    h = [re.sub(':..','' , i) for i in h] # remove :xx

    d = re.findall('\d{2}\D{3,}\d{4}',s) # re for date
    # v = re.findall('£\d{1,}.\d{2}',s)
    ov = re.findall('\d*: £\d{1,}.\d{2}',s) # get number of orders and value in £
    o = [i.split(': ')[0] for i in ov] # Split into orders and value 
    #v = [i.split(': ')[1] for i in ov]
    v = [re.sub('£', '', i.split(': ')[1]) for i in ov]

    day = re.findall('Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday', s)

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

def concat_invoices():
    data_df = pd.DataFrame(columns = ['Day', 'Date', 'Time_in', 'Time_out', 'Hours_worked', 'Orders', 'Total'])
    
    for filename in os.listdir(invoices):
        if filename.endswith(".pdf"):
            print(os.path.join(invoices, filename))
            text = extract_text(os.path.join(invoices, filename))
            df = create_df(text)
            # Could use keys arg to concat lable by date
            data_df = pd.concat([data_df, df]) # ineficient could do better 
            data_df.reset_index(drop=True, inplace=True)
    return data_df

def create_summary_df(text):
    s = text.split('Summary')[1] # Take all text after 'Summary'
    split = re.split('(.\d+.\d+)',s) # Split based £xx.xx where x is a didget
    date = re.findall('\d{2}\D{3,}\d{4}',text)[0]

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
            'names_' + date: names,
            'values_' + date: values
        }
    )
    df.set_index('names_' + date, inplace=True)
    return(df)

def concat_summary():

    df_list = []
    full_df = pd.DataFrame()

    for filename in os.listdir(invoices):
        if filename.endswith(".pdf"):
            print(os.path.join(invoices, filename))
            text = extract_text(os.path.join(invoices, filename))
            summary_df = create_summary_df(text)
            df_list.append(summary_df)

    for i, df in enumerate(df_list):
        print(df)
        full_df = pd.merge(full_df, df_list[i], left_index=True, right_index=True, how='outer')
        #full_df = full_df.join(df, how= "outer")
        #full_df.join(df_list[i]) 

    return full_df
 
def create_fee_adjustments_df(text):
    head = ["Category","Note","Amount"]

    s = text.split('Summary')[0] # Take all text after 'Summary'
    if re.search('Fee Adjustments', s):
        s = s.split('CategoryNoteAmount')[1] # Take all text after 'Fee Adjustments'
    else:
        return 'No Adjustments'
    head = ["Category","Note","Amount"]
    total = re.split('(£\d+.\d{2})',s)[-3:-1]
    ex_total = re.split('(£\d+.\d{2})',s)[:-3]
    
    cat = re.findall("[A-Z]{2,} [A-Z]{2,}", str(ex_total))
    cat = [i[:-1] for i in cat]
    note = re.findall("[A-Z][a-z][A-Za-z0-9 ]*", str(ex_total))
    amount = re.findall('(£\d+.\d{2})', str(ex_total))

    list_list = []
    for c, n, a in zip(cat, note, amount):
        list_list.append([c, n, a])

    print(list_list)

    #print(ex_total)
    #print(cat)
    #print(note)
    #print(amount)

    total.insert(1,"-")

    df = pd.DataFrame()
    df = df.append(pd.DataFrame(data=[head]))

    for row in list_list:
        df = df.append(pd.DataFrame(data=[row]), ignore_index=True)
    
    df = df.append(pd.DataFrame(data=[total]))
    print(df)

    with open("raw.txt", "w") as raw:
        raw.write(s)
    return df

def concat_fee_adjustments():

    df_list = []
    full_df = pd.DataFrame()

    for filename in os.listdir(invoices):
        if filename.endswith(".pdf"):
            print(os.path.join(invoices, filename))
            text = extract_text(os.path.join(invoices, filename))
            df = create_fee_adjustments_df(text)
            if type(df) != str:
                df_list.append(df)
    for i, df in enumerate(df_list):
        print(df)
        full_df = pd.merge(full_df, df_list[i], left_index=True, right_index=True, how='outer')
  
if __name__ == '__main__':

    fa_df = concat_fee_adjustments()
    print(fa_df)

    # Done --------------------------+
    
    #data_df = concat_invoices()
    #data_df.to_csv("outputs/data.csv")
    #print(data_df)

    #summary_df = concat_summary()
    #print(summary_df)
