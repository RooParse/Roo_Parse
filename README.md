# Roo_Parse

This program was created to make tax returns easier and facilitate gathering of data so riders can see what the effects of changes in the algorithms are having on hourly rate over time.

## Usage
***

1. Slect a folder containing the invoices you wish to parse, it should then show the file path at the bottom of the window. 

2. Click run to extract the data from the pdfs to csv files. 

3. Select the folder you wish to save a zip file containing the csv files in, it should then show the file path at the bottom of the window. 

4. Click save. This will overwrite any folder called "data.zip" in the directory you selected. 

![image](https://i.imgur.com/w2aJVEB.png)

## To Do
***
* Write up read me properly
* Make sure correct date is parsed consistently 
* Adjustments df
* Settle on a format for data
* Finish GUI
    * Add help 
    * Add about - info, contact etc
    * Add license and warnings etc
    * dark mode?
* Create Column for file name of invoice
* Fix bug with dates, alternating dashes and slashes for some reason 

#### For data processing.
* Create script to read the rooparse email box 
* Add a system to pass on the rooparse version in the file name 

## Done
***
* Change format of date
* Merge summary dataframes by date
* Parse drops, fee adjustments and summery to pandas df
* Zip CSVs for emailing

## Liscense

***

Begin license text.  
Copyright 2019 

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

End license text.