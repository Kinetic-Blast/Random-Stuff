
# This script converts an executable file (.exe) into a Python script that, when executed, will decode the encoded executable and rebuild it on the system. It essentially embeds the executable file within the Python script as a Base64-encoded string and then writes code to decode it back to its original binary form and execute it.

#you can also add other features/ other code

import base64
import os



def encode_exe_to_python(exe_path, output_python_file):
    # Read the exe file as binary data
    with open(exe_path, 'rb') as exe_file:
        exe_data = exe_file.read()
    
    # Encode the exe data into base64
    base64_encoded_exe = base64.b64encode(exe_data).decode('utf-8')

    # Write the encoded data to a Python file
    with open(output_python_file, 'w') as python_file:
        python_file.write(f"import base64\n")
        python_file.write(f"import os\n\n")
        python_file.write(f"encoded_exe = \"{base64_encoded_exe}\"\n\n")
        python_file.write(f"decoded_exe = base64.b64decode(encoded_exe)\n\n")
        python_file.write(f"with open('{exe_path}', 'wb') as rebuilt_exe:\n")
        python_file.write(f"    rebuilt_exe.write(decoded_exe)\n\n")
        python_file.write(f"os.system('start {exe_path}')\n")
        # this is where you add other fun parts that should not be there or parts that should. you get the idea.



if __name__ == "__main__":
    exe_path = "<path to program>"  # Hardcoded exe path
    output_python_file = "<output.py>"
    encode_exe_to_python(exe_path, output_python_file)
    print(f"Encoded Python file '{output_python_file}' generated successfully!")


#you will need pyinstaller
#pyinstaller --onefile  <output.py>