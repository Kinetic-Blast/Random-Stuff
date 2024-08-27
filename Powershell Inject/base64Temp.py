import base64

def create_bat_with_pdf(pdf_path, bat_path):
    # Read the PDF file
    with open(pdf_path, 'rb') as pdf_file:
        pdf_content = pdf_file.read()
    
    # Encode the PDF content to Base64
    base64_content = base64.b64encode(pdf_content).decode('utf-8')
    
    # Write the batch file
    with open(bat_path, 'w') as bat_file:
        bat_file.write('@echo off\n')
        bat_file.write('echo Rebuilding PDF from Base64...\n')
        
        # Split the Base64 string into chunks of 76 characters (which is standard for Base64)
        chunk_size = 76  # 76 characters is the default line length for Base64 encoding
        for i in range(0, len(base64_content), chunk_size):
            chunk = base64_content[i:i+chunk_size]
            if i == 0:
                # Create the file with the first chunk
                bat_file.write(f'echo {chunk} > temp_base64.txt\n')
            else:
                # Append the remaining chunks to the file
                bat_file.write(f'echo {chunk} >> temp_base64.txt\n')
        
        # Decode the Base64 back to the original PDF
        bat_file.write('certutil -f -decode temp_base64.txt rebuilt_file.pdf\n')
        
        # Clean up
        bat_file.write('del temp_base64.txt\n')
        bat_file.write('echo PDF has been rebuilt as rebuilt_file.pdf\n')
        bat_file.write('pause\n')

# Example usage
pdf_path = 'example.pdf'  # Path to the PDF file you want to encode
bat_path = 'rebuild_pdf.bat'  # Path to the output .bat file

create_bat_with_pdf(pdf_path, bat_path)
