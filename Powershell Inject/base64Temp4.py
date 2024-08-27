import base64

def create_vbs_with_pdf_and_powershell(pdf_path, vbs_path):
    # Read the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_content = pdf_file.read()
    
    # Encode the PDF content to a Base64 string
    base64_content = base64.b64encode(pdf_content).decode('utf-8')
    
    # Create the VBScript content
    vbs_script = f"""
Dim fso, stream, pdfFile, base64Data, shell
Set fso = CreateObject("Scripting.FileSystemObject")
Set shell = CreateObject("WScript.Shell")



' Define the path for the output PDF file
pdfFile = "{pdf_path}"

' Base64 encoded data of the PDF
base64Data = "{base64_content}"

' Create a stream object to handle binary data
Set stream = CreateObject("ADODB.Stream")
stream.Type = 1 ' adTypeBinary
stream.Open

' Write Base64 data to the stream as binary
stream.Write DecodeBase64(base64Data)
stream.SaveToFile pdfFile, 2 ' adSaveCreateOverWrite
stream.Close

' Open the PDF file
shell.Run pdfFile, 1, False

' Run PowerShell command to display "Hello World" and pause
Dim psCommand
psCommand = "powershell -Command Write-Output 'Hello World'; Read-Host -Prompt 'Press Enter to continue...'"
shell.Run psCommand, 1, True

' Function to decode Base64 to binary
Function DecodeBase64(base64Str)
    Dim xml, node
    Set xml = CreateObject("MSXML2.DOMDocument")
    Set node = xml.createElement("Base64Data")
    node.dataType = "bin.base64"
    node.text = base64Str
    DecodeBase64 = node.nodeTypedValue
End Function
"""

    # Write the VBScript file
    with open(vbs_path, 'w') as vbs_file:
        vbs_file.write(vbs_script)

# Example usage
pdf_path = 'example.pdf'  # Path to the PDF file you want to encode
vbs_path = 'create_pdf_vbs.vbs'  # Path to the output .vbs file

create_vbs_with_pdf_and_powershell(pdf_path, vbs_path)
