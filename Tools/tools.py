import os
import sys
import time

folder_path = "./"

class fileLocator():

    path = str()

    def __init__(self) -> None:
        path = os.getcwd()

class logCreacter():
    def __init__(self):
        self.log_file = "log.txt"
        self.log_file_path = os.path.join(os.getcwd(), self.log_file)

    def log(self, log_message):
        with open(self.log_file_path, "a") as f:
            f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + log_message + "\n")

class convertByteToHex:

    @staticmethod
    def swap_endianness(data):
        swapped_data = bytearray()
        for i in range(0, len(data), 4):
            chunk = data[i:i+4]
            swapped_chunk = chunk[::-1]
            swapped_data.extend(swapped_chunk)
        return swapped_data

    def convert_byte_to_hex(self, byte_file, hex_file):
        with open(byte_file, 'rb') as f_in:
            with open(hex_file, 'w') as f_out:
                byte_data = f_in.read()
                swapped_data = self.swap_endianness(byte_data)
                hex_data = swapped_data.hex()

                formatted_hex_data = '\n'.join(hex_data[i:i+8] for i in range(0, len(hex_data), 8))

                f_out.write(formatted_hex_data)

class UI():

    def cil_ui(self):
        while(True):
            file_names = [file 
                          for file in os.listdir(folder_path)
                          if os.path.isfile(os.path.join(folder_path, file))]
            bin_files = [file
                         for file in file_names
                         if file.endswith(".bin")]
            if len(bin_files) == 0:
                print("No .bin files found in the current directory")
                byte_file = input("Enter the byte file: ")
            elif len(bin_files) == 1:
                byte_file = bin_files[0]
            else:
                print("Multiple .bin files found in the current directory")
                byte_file = input("Enter the byte file: ")
            
            file_name = byte_file.split(".")[0]
            hex_file = file_name + ".hex"

            convertByteToHex().convert_byte_to_hex(byte_file, hex_file)

            print(f"Operate\t:\t{byte_file} -> {hex_file}")
            print("Status\t:\tSeccess\n")
            
            return 0

def main():
    UI().cil_ui()

if __name__ == "__main__": 
    main()