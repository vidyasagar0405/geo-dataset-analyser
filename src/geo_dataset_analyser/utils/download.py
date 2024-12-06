import ftplib
import os

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

