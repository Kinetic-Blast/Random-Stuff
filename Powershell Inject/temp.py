import pikepdf
import os

def add_js_to_pdf(pdf_path, js_path, output_pdf):
    # Open the PDF file
    with pikepdf.open(pdf_path) as pdf:
        # Read the JavaScript code from the file
        with open(js_path, "r") as js_file:
            js_code = js_file.read()

        # Create a dictionary and add the JavaScript action
        open_action = pikepdf.Dictionary()
        open_action[pikepdf.Name("/S")] = pikepdf.Name("/JavaScript")
        open_action[pikepdf.Name("/JS")] = pikepdf.String(js_code)

        # Add the JavaScript at the document level as an OpenAction
        pdf.Root[pikepdf.Name("/OpenAction")] = open_action

        # Save the modified PDF
        pdf.save(output_pdf)

    print(f"JavaScript has been successfully added to {output_pdf}")

if __name__ == "__main__":
    # Get file paths from the user
    pdf_path = input("Enter the path to the PDF file: ")
    js_path = input("Enter the path to the JavaScript file: ")
    
    # Check if the provided files exist
    if not os.path.exists(pdf_path):
        print("PDF file not found.")
        exit(1)

    if not os.path.exists(js_path):
        print("JavaScript file not found.")
        exit(1)

    # Define the output file name
    output_pdf = "output_with_js.pdf"

    # Call the function to add JavaScript to the PDF
    add_js_to_pdf(pdf_path, js_path, output_pdf)


