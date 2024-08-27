def create_vbs_for_powershell_test(vbs_path):
    # Create the VBScript content
    vbs_script = f"""
Dim shell
Set shell = CreateObject("WScript.Shell")

' Delete the script itself
Set fso = CreateObject("Scripting.FileSystemObject")
fso.DeleteFile "{vbs_path}", True

' Run PowerShell command to display "Hello World"
Dim psCommand
psCommand = "powershell -Command Write-Output 'Hello World'; Read-Host -Prompt 'Press Enter to continue...'"
shell.Run psCommand, 1, True

"""

    # Write the VBScript file
    with open(vbs_path, 'w') as vbs_file:
        vbs_file.write(vbs_script)

# Example usage
vbs_path = 'test_powershell.vbs'  # Path to the output .vbs file

create_vbs_for_powershell_test(vbs_path)

