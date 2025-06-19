import time
import os

from agage_archive.config import Paths, data_file_path
from agage_archive.run import run_all
from agage_archive.util import archive_to_csv


def preprocess():
    """Preprocess data files before running the main script
    Hopefully this will become redundant in the future
    
    """

    from pathlib import Path

    paths = Paths("agage")

    md_folder = data_file_path("", "agage", sub_path=paths.md_path)
    # For CGO H2 data, the PDD is mis-labelled (Issue #47)
    if (md_folder / "AGAGE-GCMD_CGO_h2_pdd.nc").exists():
        os.system(f"cp {md_folder / 'AGAGE-GCMD_CGO_h2_pdd.nc'} {md_folder / 'AGAGE-GCPDD_CGO_h2.nc'}")

    # Copy TAC GCMD data into the AGAGE MD folder (not synced with the main archive at the mo)
    decc_path = Path("/agage/summary/netcdf-decc/md")
    decc_md_co = decc_path / "AGAGE-GCMD_TAC_co.nc"
    decc_md_n2o = decc_path / "AGAGE-GCMD_TAC_n2o.nc"
    decc_md_sf6 = decc_path / "AGAGE-GCMD_TAC_sf6.nc"
    if (decc_md_co).exists():
        os.system(f"cp {decc_md_co} {md_folder / 'AGAGE-GCMD_TAC_co.nc'}")
    if (decc_md_n2o).exists():
        os.system(f"cp {decc_md_n2o} {md_folder / 'AGAGE-GCMD_TAC_n2o.nc'}")
    if (decc_md_sf6).exists():
        os.system(f"cp {decc_md_sf6} {md_folder / 'AGAGE-GCMD_TAC_sf6.nc'}")

    # Copy a frozen copy of the TOB SF6 ECD (not synced with the main archive at the mo)
    tobsf6_path = Path("/data/summary/netcdf-other/md")
    tobsf6 = tobsf6_path / "AGAGE-GCECD_TOB_sf6.nc"
    if (tobsf6).exists():
        os.system(f"cp {tobsf6} {md_folder / 'AGAGE-GCECD_TOB_sf6.nc'}")


if __name__ == "__main__":

    # Preprocess data files
    # preprocess()

    start_time = time.time()

    print("####################################")
    print("#####Processing public archive######")
    print("####################################")
    run_all("agage", species = ["cfc-11"])

    print("####################################")
    print("#####Converting to csv######")
    print("####################################")
    archive_to_csv("agage")

    print(f"Time taken: {time.time() - start_time:.2f} seconds")