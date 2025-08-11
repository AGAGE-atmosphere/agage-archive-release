
#  AGAGE Data README file
This archive contains the complete AGAGE/ALE/GAGE dataset. Measurements are made of dry air mole fractions of atmospheric trace gases measured at various AGAGE stations and their predecessors.

The archive is compiled from early ALE/GAGE files combined with AGAGE files output from the GCWerks software. The code for processing and standardising these data is at https://github.com/AGAGE-atmosphere/agage-archive and https://github.com/AGAGE-atmosphere/agage-archive-release. The ALE/GAGE files were created by Derek Cunnold's team at Georgia Tech (GA Tech.) in the early 1990s, and are are included in the AGAGE data specification repository https://github.com/AGAGE-atmosphere/agage-archive-release/tree/main/data/agage/ale_gage_sio1993. These data were themselves converted from earlier scales to the Scripps Institution of Oceanography (SIO) 1993 calibration scale (SIO-93; see Cunnold et al., 1994 and Prinn et al., 2000). The GA Tech. files are reprocessed into netCDF format here and converted to the most recent calibration scales. See the [Methodology notes](https://github.com/AGAGE-atmosphere/agage-archive/blob/main/docs/ale_gage_notes.md) in the agage-archive repository for details.

The code for reprocessing the AGAGE data is currently maintained by the University of Bristol. Contact matt.rigby@bristol.ac.uk with errors and questions, or, preferably, submit Issues or Pull Requests on Github. For questions regarding individual data sources, please contact the relevant AGAGE station PIs (contact details are contained in file metadata).

# Format and Structure

This archive consists of a set of netCDF files. For information on the netCDF file format see: https://www.unidata.ucar.edu/software/netcdf/

Filenames follow the convention

```network{-instrument}_sitecode_species_{filetype-}version.nc```

where the elements in curly brackets are optional, depending on the file.

Below is an example of the archive structure, showing only CFC-11 data:

```
.
├── README.md
└── cfc-11
    ├── agage_cgo_cfc-11_20240513.nc
    ├── agage_cmo_cfc-11_20240513.nc
    ├── agage_mhd_cfc-11_20240513.nc
    ├── agage_rpb_cfc-11_20240513.nc
    ├── agage_smo_cfc-11_20240513.nc
    ├── baseline-flags
    │   ├── agage_cgo_cfc-11_git-baseline-20240513.nc
    │   ├── agage_cmo_cfc-11_git-baseline-20240513.nc
    │   ├── agage_mhd_cfc-11_git-baseline-20240513.nc
    │   ├── agage_rpb_cfc-11_git-baseline-20240513.nc
    │   └── agage_smo_cfc-11_git-baseline-20240513.nc
    ├── individual-instruments
    │   ├── agage-ale-gcmd_adr_cfc-11_20240513.nc
    │   ├── agage-ale-gcmd_cgo_cfc-11_20240513.nc
    │   ├── agage-ale-gcmd_cmo_cfc-11_20240513.nc
    │   ├── agage-ale-gcmd_rpb_cfc-11_20240513.nc
    │   ├── agage-ale-gcmd_smo_cfc-11_20240513.nc
    │   ├── agage-gage-gcmd_cgo_cfc-11_20240513.nc
    │   ├── agage-gage-gcmd_cmo_cfc-11_20240513.nc
    │   ├── agage-gage-gcmd_mhd_cfc-11_20240513.nc
    │   ├── agage-gage-gcmd_rpb_cfc-11_20240513.nc
    │   ├── agage-gage-gcmd_smo_cfc-11_20240513.nc
    │   ├── agage-gcmd_cgo_cfc-11_20240513.nc
    │   ├── agage-gcmd_mhd_cfc-11_20240513.nc
    │   ├── agage-gcmd_rpb_cfc-11_20240513.nc
    │   ├── agage-gcmd_smo_cfc-11_20240513.nc
    │   ├── agage-gcmd_thd_cfc-11_20240513.nc
    │   ├── agage-gcms-medusa_cmn_cfc-11_20240513.nc
    │   ├── agage-gcms-medusa_gsn_cfc-11_20240513.nc
    │   ├── agage-gcms-medusa_jfj_cfc-11_20240513.nc
    │   ├── agage-gcms-medusa_zep_cfc-11_20240513.nc
    │   ├── agage-gcms-mtecimone_cmn_cfc-11_20240513.nc
    │   ├── baseline-flags
    │   │   ├── agage-ale-gcmd_adr_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-ale-gcmd_cgo_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-ale-gcmd_cmo_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-ale-gcmd_rpb_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-ale-gcmd_smo_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gage-gcmd_cgo_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gage-gcmd_cmo_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gage-gcmd_mhd_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gage-gcmd_rpb_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gage-gcmd_smo_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcmd_cgo_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcmd_mhd_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcmd_rpb_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcmd_smo_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcmd_thd_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcms-medusa_cmn_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcms-medusa_gsn_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcms-medusa_jfj_cfc-11_git-baseline-20240513.nc
    │   │   ├── agage-gcms-medusa_zep_cfc-11_git-baseline-20240513.nc
    │   │   └── agage-gcms-mtecimone_cmn_cfc-11_git-baseline-20240513.nc
    │   └── monthly-baseline
    │       ├── agage-ale-gcmd_adr_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-ale-gcmd_cgo_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-ale-gcmd_cmo_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-ale-gcmd_rpb_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-ale-gcmd_smo_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gage-gcmd_cgo_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gage-gcmd_cmo_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gage-gcmd_mhd_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gage-gcmd_rpb_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gage-gcmd_smo_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcmd_cgo_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcmd_mhd_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcmd_rpb_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcmd_smo_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcmd_thd_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcms-medusa_cmn_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcms-medusa_gsn_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcms-medusa_jfj_cfc-11_monthly-baseline-20240513.nc
    │       ├── agage-gcms-medusa_zep_cfc-11_monthly-baseline-20240513.nc
    │       └── agage-gcms-mtecimone_cmn_cfc-11_monthly-baseline-20240513.nc
    └── monthly-baseline
        ├── agage_cgo_cfc-11_monthly-baseline-20240513.nc
        ├── agage_cmo_cfc-11_monthly-baseline-20240513.nc
        ├── agage_mhd_cfc-11_monthly-baseline-20240513.nc
        ├── agage_rpb_cfc-11_monthly-baseline-20240513.nc
        └── agage_smo_cfc-11_monthly-baseline-20240513.nc


```

At the first level, the archive is organised by species (in the above example, dry-air mole fractions of chlorofluorocarbon-11, CFC-11). The files in this top-level directory are the "recommended" ALE/GAGE/AGAGE high-frequency records that should be sufficient for most users. Here, high-frequency can refer to the instantaneous or integrated observations on gas chromatography systems, and/or temporal averages from optical instruments (typically hourly). These files may be a combination of multiple instruments (e.g., for CFC-11 at Cape Grim (CGO), the ALE GCMD, the GAGE GCMD and the AGAGE GCMD instruments) based on careful considerations by AGAGE scientists. 

There are sub-directories within each species directory. 

The AGAGE statistical pollution algorithm (see O'Doherty et al., 2001) is used to determine “pollution-free” baseline flags for each measurement data point in the species folder, which are given in the ```baseline-flags``` directory.

Based on these baseline flags and the high-frequency measurement data, the resulting “pollution-free” monthly mean mole fractions are given in the ```monthly-baseline``` directory. 

The ```individual-instrument``` sub-directory contains files for individual ALE/GAGE/AGAGE instruments (e.g. ALE GCMS, AGAGE Medusa, etc.). For some species and sites, several of these have been combined for the recommended files. The folder again contains sub-folders with ```baseline-flags``` data files and ```monthly-baseline``` data for these individual instruments.

# AGAGE Data Statement:

These data are made available to the scientific community and public to improve understanding of ozone depletion and climate change and to lead to new scientific insights. AGAGE relies on the ethics and integrity of the user to ensure that AGAGE scientists receive fair credit for their work.

If the data are obtained for potential use in a publication or presentation, AGAGE station PIs should be informed at the outset of the proposed work. Station PI contact information is located in the station pages. If the AGAGE data are essential to the work, co-authorship on publications may be appropriate. Manuscripts using the AGAGE data should be sent early to the AGAGE contacts for review before they are submitted for publication, so we can ensure that the quality and limitations of the data are accurately represented.

Every effort is made to produce the most accurate and precise measurements possible. However, we reserve the right to make corrections to the data based on recalibration of standard gases or for other reasons deemed scientifically justified. We are not responsible for results and conclusions based on use of these data without regard to this warning.

Data used in publications must be included as a supplementary file with the publication.

# AGAGE Data Reciprocity Agreement

Use of these data implies an agreement to reciprocate. Laboratories making similar measurements agree to make their own data available to the general public and to the scientific community in an equally complete and easily accessible form. Scientists are encouraged to make available to the community, upon request, their own modelling tools used in the interpretation of the AGAGE data, namely well documented model code, transport fields, and additional information necessary for other scientists to repeat the work and to run modified versions.

# Acknowledgements

Publications must state: “AGAGE is supported principally by the National Aeronautics and Space Administration (USA) grants to the Massachusetts Institute of Technology and the Scripps Institution of Oceanography."

Additional statements must be included to acknowledge funding for the individual stations. These are located on the individual station pages of the AGAGE website.

# Citation of AGAGE Data
 
(1) Obtain and cite the DOI of the specific version of the AGAGE data that you have used.

(2) R.G. Prinn, R.F. Weiss, J. Arduini, T. Arnold, H.L. DeWitt, P.J. Fraser, A.L. Ganesan, J. Gasore, C.M. Harth, O. Hermansen, J. Kim, P.B. Krummel, S. Li, Z. M. Loh, C.R. Lunder, M. Maione, A.J. Manning, B.R. Miller, B. Mitrevski, J. Mühle, S. O’Doherty, S. Park, S. Reimann, M. Rigby, T. Saito, P.K. Salameh, R. Schmidt, P.G.  Simmonds, L.P. Steele, M.K. Vollmer, R.H. Wang, B. Yao, Y. Yokouchi, D. Young, and L. Zhou: History of chemically and radiatively important atmospheric gases from the Advanced Global Atmospheric Gases Experiment (AGAGE), Earth Syst. Sci. Data, 10, 985-1018, 2018, https://doi.org/10.5194/essd-10-985-2018. 

(3) Most recent AGAGE paper publishing the relevant data (e.g., for a specific species), as listed on AGAGE Publications.

# Licence

Distributed under CC-BY 4.0 (https://creativecommons.org/licenses/by/4.0/deed.en)
