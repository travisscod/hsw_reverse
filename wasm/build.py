import subprocess
import base64

with open("original.wat", "rb") as file:
    wasm_data = file.read()
    
with open("temp.wat.base64", "wb") as file:
    file.write(wasm_data)
    subprocess.run(["wat2wasm", "temp.wat.base64", "-o", "original.wasm"])

    # Encode the file
    with open("original.wasm", "rb") as file:
        encoded_data = base64.b64encode(file.read()).decode('utf-8')
        with open("original.wasm.base64", "w") as output_file:
            output_file.write(encoded_data)