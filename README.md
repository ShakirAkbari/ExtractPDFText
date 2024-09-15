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
2. Place the script in a known folder, e.g., C:\Projects\PDFProcessor\.

## Step 3: Install Required Dependencies
Install libraries: 
```
pip install pypdf PyPDF2 pdfminer.six
```

## Step 4: Create the Executable
1. Open a command prompt or terminal.
2. Navigate to the folder containing your pdf_processor.py script:
   ```
   cd C:\Projects\PDFProcessor
   ```
3. Run PyInstaller with the following command:
   ```
   pyinstaller --onefile pdf_processor.py
   ```
   The `--onefile` option creates a single executable file.

## Step 5: Locate the Executable
1. After PyInstaller finishes, you'll find a new `dist` folder in your current folder.
2. Inside the `dist` folder, you'll find your pdf_processor.exe file.

## Step 6: Test the Executable
1. Create a `data` folder in the same folder as your executable.
2. Place some PDF files in the `data` folder.
3. Run the executable by double-clicking it or from the command line:
   ```
   .\pdf_processor.exe
   ```
4. Check that it processes the PDFs and creates an `Output` folder with the results.


# PDF Processor Command-line Options

ExtractPDFText supports several command-line options; here is a detailed description of each option:

1. `-i` or `--input`
   - Purpose: Specifies the input folder containing PDF files to process.
   - Usage: `pdf_processor.exe -i C:\path\to\pdf\files`
   - Default: If not specified, the program looks for a folder called 'data' in the folder where the executable is located.

2. `-o` or `--output`
   - Purpose: Specifies the output folder where processed text files will be saved.
   - Usage: `pdf_processor.exe -o C:\path\to\output\folder`
   - Default: If not specified, an 'Output' folder is created at the same level as the input folder.

3. `-r` or `--recursive`
   - Purpose: Enables recursive processing of PDF files in subdirectories.
   - Usage: `pdf_processor.exe -r`
   - Default: If not specified, only PDF files in the top-level input folder are processed.

4. `-v` or `--verbose`
   - Purpose: Increases output verbosity, providing more detailed information during processing.
   - Usage: `pdf_processor.exe -v`
   - Default: If not specified, minimal output is provided.

5. `--links-only`
   - Purpose: Extracts only hyperlinks from the PDF, skipping full text extraction.
   - Usage: `pdf_processor.exe --links-only`
   - Default: If not specified, both text and links are extracted.

Feel free to combine these options as needed. For example:
```
pdf_processor.exe -i C:\PDFs -o C:\Output -r -v --links-only
```

This command assumes pdf_processor.exe is located in C:\ and would process all PDFs in C:\PDFs and its subdirectories, save the output to C:\Output, provide verbose output, and extract only the links.

If you run the program without any options, it will use default values and look for a 'data' folder.



# PDF Processor Default Folder Structure

The PDF Processor is designed to work with a specific folder structure by default, although this can be overridden using command-line options. Here's the expected default structure:

```
[Parent Folder]
│
├── pdf_processor.exe
│
├── data
│   ├── file1.pdf
│   ├── file2.pdf
│   └── ...
│
└── Output
    ├── file1.txt
    ├── file2.txt
    └── ...
```

## Explanation:

1. **[Parent Folder]**: 
   This is the main folder where the executable is placed. It can be named anything.

2. **pdf_processor.exe**: 
   The executable file should be placed directly in the parent folder.

3. **data**: 
   - This is the default input folder.
   - It should be a subfolder of the parent folder at the same level as the executable.
   - All PDF files to be processed should be placed in this folder.
   - The program will look for this folder by default if no input folder is specified.

4. **Output**: 
   - This is the default output folder.
   - It will be created automatically by the program if it doesn't exist.
   - It will be created at the same level as the 'data' folder.
   - All processed text files will be saved here.

## Notes:

- If the 'data' folder is not found in the expected location, the program will attempt to find it in several predefined locations relative to the executable.
- You can override the default input and output directories using the `-i` and `-o` command-line options respectively.
- If you use the `-r` (recursive) option, the program will also process PDF files in subdirectories of the input folder.

This default structure allows for easy setup and use of the PDF Processor without needing to specify custom directories. Simply place your PDF files in the 'data' folder and run the executable.

 
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
