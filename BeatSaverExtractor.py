from os import listdir, remove 
from os.path import splitext, join
import zipfile

maps_path = "YOUR\PATH\TO\steamapps\common\Beat Saber\Beat Saber_Data\CustomLevels"

def main():
    files = [f for f in listdir() if  splitext(f)[1] == ".zip"]
    for file in files:
        with zipfile.ZipFile(file, 'r') as zip_ref:
            zip_ref.extractall(join(maps_path, splitext(file)[0]))
        remove(file) 

if __name__ == "__main__":
    main()