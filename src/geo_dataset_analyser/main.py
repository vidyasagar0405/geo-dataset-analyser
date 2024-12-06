from utils import download, extract_utils

def main():
    accession_id = "GSE232522"  # Replace with your GEO accession ID
    # output_dir = "./geo_datasets"  # Directory to save files
    # download.download_geo_dataset(accession_id, output_dir)

    # Usage
    input_dir = "./geo_datasets"   # Directory containing the downloaded files
    output_dir = f"./geo_datasets/{accession_id}"  # Directory for extracted files
    extract_utils.extract_all(input_dir, output_dir, accession_id)


if __name__ == "__main__":
    main()
