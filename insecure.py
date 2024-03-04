# This is an intentionally insecure Python code for testing purposes.

import os

def insecure_password_storage(password):
    # Security Issue: Storing passwords in plaintext
    with open('passwords.txt', 'a') as file:
        file.write(password + '\n')

def insecure_eval(input_data):
    # Security Issue: Using eval can introduce code injection vulnerabilities
    result = eval(input_data)
    print("Result of eval:", result)

def insecure_command_injection(command):
    # Security Issue: Using subprocess without proper input validation can lead to command injection
    os.system('echo ' + command)

def insecure_pickle(data):
    # Security Issue: Using pickle without proper validation can lead to deserialization vulnerabilities
    import pickle
    obj = pickle.loads(data)
    print("Unpickled object:", obj)

if __name__ == "__main__":
    # Insecure function calls for testing
    insecure_password_storage("insecure_password123")
    insecure_eval("__import__('os').system('echo Insecure eval')")
    insecure_command_injection("echo Insecure command injection")
    insecure_pickle(b'\x80\x04\x95\x07\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x11insecure_pickle\x94\x93\x94.')

    print("Insecure code executed.")
