import os 
import glob
import tarfile
import gzip
import shutil

def extract_gz(file_path, output_dir):
    """
    Extracts a .gz file.

    Parameters:
        file_path (str): Path to the .gz file.
        output_dir (str): Directory to save the extracted file.
    """
    file_name = os.path.basename(file_path).replace('.gz', '')
    output_path = os.path.join(output_dir, file_name)

    os.makedirs(output_dir, exist_ok=True)
    
    with gzip.open(file_path, 'rb') as f_in:
        with open(output_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
    print(f"Extracted: {output_path}")


def extract_tar(file_path, output_dir):
    """
    Extracts a .tar or .tar.gz file.

    Parameters:
        file_path (str): Path to the tar file.
        output_dir (str): Directory to save the extracted files.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    with tarfile.open(file_path, 'r:*') as tar:
        tar.extractall(path=output_dir)
        print(f"Extracted: {file_path} to {output_dir}")


def extract_all(directory, output_dir, acc_id):
    """
    Extracts all .gz and .tar.gz files in a directory.

    Parameters:
        directory (str): Directory containing the files to extract.
        output_dir (str): Directory to save the extracted files.
    """
    os.listdir("./geo_datasets/")
    print(os.listdir("./geo_datasets/"))
    os.makedirs(output_dir, exist_ok=True)
    for file_path in glob.glob(f"{directory}/*.tar"):
        if file_path.endswith('.tar'):
            extract_tar(file_path, output_dir)
    for file_path in glob.glob(f"{output_dir}/*"):
        print()
        print(file_path)
        print()
        if file_path.endswith('.gz'):
            extract_gz(file_path, output_dir)
            os.remove(file_path)
