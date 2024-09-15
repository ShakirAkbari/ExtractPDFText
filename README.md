# ExtractPDFText
The PDF Processor is a standalone executable program designed to automate the extraction of text and hyperlinks from PDF files. It processes multiple PDF documents in batch, creating corresponding text files that contain the extracted content.

# Instructions for Creating the PDF Processor Executable

Follow these steps to turn the pdf_processor.py script into a standalone executable (.exe) file using PyInstaller:

## Prerequisites
1. Ensure you have Python installed on your system (preferably Python 3.6 or later).
2. Make sure you have pip (Python package installer) installed.

## Step 1: Install PyInstaller
1. Open a command prompt or terminal.
2. Run the following command to install PyInstaller:
   ```
   pip install pyinstaller
   ```

## Step 2: Prepare Your Script
1. Download pdf_processor.py.
2. Place the script in a known directory, e.g., C:\Projects\PDFProcessor\.

## Step 3: Install Required Dependencies
Install libraries: 
```
pip install pypdf PyPDF2 pdfminer.six
```

## Step 4: Create the Executable
1. Open a command prompt or terminal.
2. Navigate to the directory containing your pdf_processor.py script:
   ```
   cd C:\Projects\PDFProcessor
   ```
3. Run PyInstaller with the following command:
   ```
   pyinstaller --onefile pdf_processor.py
   ```
   The `--onefile` option creates a single executable file.

## Step 5: Locate the Executable
1. After PyInstaller finishes, you'll find a new `dist` folder in your current directory.
2. Inside the `dist` folder, you'll find your pdf_processor.exe file.

## Step 6: Test the Executable
1. Create a `data` folder in the same directory as your executable.
2. Place some PDF files in the `data` folder.
3. Run the executable by double-clicking it or from the command line:
   ```
   .\pdf_processor.exe
   ```
4. Check that it processes the PDFs and creates an `Output` folder with the results.

## Troubleshooting
- If you encounter any "module not found" errors, you may need to explicitly include those modules. Use the `--hidden-import` option with PyInstaller:
  ```
  pyinstaller --onefile --hidden-import=module_name pdf_processor.py
  ```
- If the executable fails to run, try running it from the command line to see any error messages.

## Distribution
To distribute your program:
1. Copy the pdf_processor.exe file.
2. Instruct users to place it in a folder and create a `data` subfolder for their PDFs.
3. Users can then run the executable to process their PDFs.

Remember, the executable is platform-specific. An .exe file created on Windows will only run on Windows machines.
