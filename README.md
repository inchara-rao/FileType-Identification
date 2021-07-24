#D-File Identification

#Problem statement
This work sample requires you to identify different sources that could be used to identify details of a file type
like following (but not limited to) 
1. Short Description (explaining the usage of the file type)
2. Category (i.e. Logical Source, Configuration, Data, etc.)
3. Language Family (Java, Python, Perl, etc.)
4. Programming Paradigm (Procedural, OOP, Dynamic, etc)
5. Associated applications



The detailed problem statement is available in the documents directory.



#Solution:
**Deliverable 1:**

The data sources have been identified and the rationale behind using them is expanded in the dataSources.pdf file.

**Deliverable 2:**

Implementation and Presentation of information about the given input file types are done in the code.

We considered two very good websites for getting the information about file types. Namely, fileinfo.com and fileext.com
The reasons these have been chosen are the ease of data extraction and the amount of information that could be extracted. These two websites combined, had most of the information that we needed. Also, these data sources do not need the exact file to be present which prevents the overhead and also pretty much solves the problem of effectively identifying and categorizing a file into its type solely based on the Extension and Name of the file itself.

#Excetution flow:
There are 4 directories, namely, documents, input, parsers, and output and there is a main.py and requirements.txt file.

**Step 1 - Install python dependencies from the requirement.txt file.**
This can be done using pip install -r requirements.txt command

**Step 2 - Place your input file.**
Place the file containing the list of file names and extensions whose type and information have to be extracted in the input directory.

**Step 3 - Run main.py**
Specify the input file in main.py and run it. This calls the 2 functions from the parsers directory which takes extension as a parameter and returns the dictionary of information as output.

**Step 4 - The output.txt file is obtained**
Once the parsers return the data, the data is appended to the output file in the output directory.

# Input

The input file is found in the input directory. The filenames with its extension  are taken as shown below.
> **input.csv**
```
      todo_app.py
      Resume.pdf
      
```
>**output.txt**
```
    Extension:py
    Name:Python Script
    Format:Text
    Popularity:4.2
    Category:Developer File
    Description:PY files mostly belong to Python by Python Software Foundation. Python is a dynamic object-oriented programming language that can be used for many kinds of software development. It offers strong support for integration with other languages and tools, comes with extensive standard libraries, and can be learned in a few days. .PY files can be executed with the Python interpreter and the .EXE container format itself can contain compiled Python source.
    Primarily associated with:Python
    File type:Script or Library
    Methods to open the file:You need a suitable software like Python to open a PY file.Without proper software you will receive a Windows message "How do you want to open this file?" or "Windows cannot open this file" or a similar Mac/iPhone/Android alert. If you cannot open your PY file correctly, try to right-click or long-press the file. Then click "Open with" and choose an application. You can also display a PY file directly in the browser
    File classification:Source Code
    Mime type:application/x-python, text/plain, application/octet-stream
    Related files:pyo, pyc, pyw, rpy, pv, pyd, rpa, rpyc, pyx, zip, python, exe, rpym, whl, fy, sh, npy, pxi, the, ipynb
    Information to solve problems:Associate the PY file extension with the correct application.   Update your software that should actually open script or librarys. Because only the current version supports the latest PY file format. Search, therefore, e.g. on the Python Software Foundation manufacturer website after an available Python update. To make sure that your PY file is not corrupted or virus-infected, get the file again and scan it with Google's virustotal.com.

    Extension:pdf
    Name:Portable Document Format File
    Format:Binary
    Popularity:4.1
    Category:Page
    Description:PDF files mostly belong to Acrobat by Adobe Systems Incorporated. Adobe Acrobat is a family of computer programs developed by Adobe Systems, designed to view, create, manipulate and manage files in Adobe's Portable Document Format (PDF). Some software in the family are commercial, and some are free. Adobe Reader (formerly Acrobat Reader) is available as a no-charge download from Adobe's Web site, and allows the viewing and printing of PDF files. Acrobat and Reader are widely used as a way to present information with a fixed layout similar to a paper publication. The PDF format has become a standard for document transfer between computer architectures. A PDF file retains formatting for the file being transmitted. Free viewers are available at the Adobe website and other locations. Starting in 2007, PDF files sent as attachments started to show up as spam. When the PDF file is opened, the spammed ad is shown.
    Primarily associated with:Acrobat
    File type:Portable Document Format
    Methods to open the file:You need a suitable software like Acrobat to open a PDF file.Without proper software you will receive a Windows message "How do you want to open this file?" or "Windows cannot open this file" or a similar Mac/iPhone/Android alert. If you cannot open your PDF file correctly, try to right-click or long-press the file. Then click "Open with" and choose an application. You can also display a PDF file directly in the browser
    Mime type:application/pdf, application/x-pdf, application/acrobat, applications/vnd.pdf, text/pdf, text/x-pdf
    Identifier: %PDF-1. (provided by TrID database)
    Related files:jpg, check, epdf, docx, csi, zip, png, unknown, txt, do, jpeg, xdo, dcf, pptx, file, exe, online, mp4, xlsx, download, edn, pdx, env
    Information to solve problems:Associate the PDF file extension with the correct application.   Update your software that should actually open portable document formats. Because only the current version supports the latest PDF file format. Search, therefore, e.g. on the Adobe Systems Incorporated manufacturer website after an available Acrobat update. To make sure that your PDF file is not corrupted or virus-infected, get the file again and scan it with Google's virustotal.com.

```