### Script Overview
This Python script reads a PDF file, encodes it as Base64, and generates a VBScript (.vbs) file. The VBScript is designed to decode the Base64 data back into the original PDF, save it to the specified location, and open it. Additionally, the VBScript runs a PowerShell command.

### Steps in the Script

1. **Import the Base64 Module:**
   - The script imports the `base64` module to handle the encoding of binary data into Base64.

2. **Read the PDF File:**
   - The script opens the specified PDF file in binary mode (`'rb'`) and reads its contents.

3. **Encode the PDF Content:**
   - The content of the PDF is encoded into a Base64 string using `base64.b64encode()`. The encoded data is then decoded to a UTF-8 string format.

4. **Generate VBScript:**
   - The script constructs a VBScript (`vbs_script`) that performs the following tasks:
     - **File Handling:**
       - Uses `Scripting.FileSystemObject` to handle the file system.
       - Sets up the path for saving the output PDF.
       - Initializes an `ADODB.Stream` object to handle binary data for saving the PDF.
     - **Base64 Decoding:**
       - Includes a function `DecodeBase64()` that decodes the Base64 string back into binary data using `MSXML2.DOMDocument`.
     - **Saving and Opening the PDF:**
       - Writes the decoded binary data to a file, saving it at the specified path (`pdfFile`).
       - Opens the PDF using `WScript.Shell`.
     - **PowerShell Command:**
       - Runs a PowerShell command using `WScript.Shell`.

5. **Write VBScript to File:**
   - The generated VBScript is written to the specified `.vbs` file.

### Example Usage
The script is called with:
- `pdf_path` as the path to the PDF file that will be encoded and embedded into the VBScript.
- `vbs_path` as the path to the generated VBScript file.

### Functionality Summary
- Encodes a PDF file to Base64 and embeds it into a VBScript.
- Decodes the Base64 data within the VBScript to recreate and open the PDF file.
- Runs a PowerShell command.
