import ftplib
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


def download_geo_dataset(accession_id, output_dir="."):
    """
    Downloads GEO dataset files for the given accession ID.

    Parameters:
        accession_id (str): GEO accession ID (e.g., GSE12345).
        output_dir (str): Directory to save the downloaded files.
    """
    base_url = "ftp.ncbi.nlm.nih.gov"
    ftp_path = f"/geo/series/{accession_id[:-3]}nnn/{accession_id}/suppl/"

    try:
        # Connect to GEO FTP
        ftp = ftplib.FTP(base_url)
        ftp.login()

        # Navigate to the dataset folder
        ftp.cwd(ftp_path)
        ftp.set_pasv(True)


        # List available files
        files = ftp.nlst()
        print(f"Files available for {accession_id}: {files}")

        if not files:
            print(f"No files found for {accession_id}.")
            return

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Download files
        for file in files:
            local_file_path = os.path.join(output_dir, file)
            with open(local_file_path, "wb") as f:
                ftp.retrbinary(f"RETR {file}", f.write)
                print(f"Downloaded: {file}")

        print(f"All files for {accession_id} have been downloaded to {output_dir}.")
        ftp.quit()
    except ftplib.all_errors as e:
        print(f"FTP error: {e}")

def main():
    accession_id = "GSE232522"  # Replace with your GEO accession ID
    # output_dir = "./geo_datasets"  # Directory to save files
    # download_geo_dataset(accession_id, output_dir)
    #

    # Usage
    input_dir = "./geo_datasets"   # Directory containing the downloaded files
    output_dir = f"./geo_datasets/{accession_id}"  # Directory for extracted files
    extract_all(input_dir, output_dir, accession_id)


if __name__ == "__main__":
    main()
