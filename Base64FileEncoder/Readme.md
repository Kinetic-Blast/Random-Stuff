This script converts an executable file (.exe) into a Python script. Upon execution, the Python script decodes the encoded executable back to its original binary form and reconstructs it on the system, effectively concealing the executable within the Python script.

With this capability, additional functions can be integrated into the Python script before encoding. Subsequently, the enhanced script can be exported to an executable (.exe) format, allowing for utilization on systems without the necessity of a Python installation.

you will need pyinstaller - pip install pyinstaller to make use of that last part
pyinstaller --onefile  <output.py> <----- how to export you can also add a icon to it
