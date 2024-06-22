import os
import base64
import subprocess


def decompile():
    wasm_file = '../hsw.wasm.base64'
    
    with open(wasm_file, 'rb') as file:
        wasm_data = file.read()
    
    decoded_data = base64.b64decode(wasm_data)
    
    with open('original.wasm', 'wb') as file:
        file.write(decoded_data)
    
    subprocess.run(['wasm2wat', '.\original.wasm --output=original.wat'])

decompile()