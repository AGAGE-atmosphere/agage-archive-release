# Changelog

Notable changes to this the AGAGE dataset will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)

## [20260716] - 2026-07-16

July 2026 update of the ALE/GAGE/AGAGE data archive. Data were most recently reviewed at the AGAGE 73 meeting, 15-18 June, 2026.

### Changed
- Data updated through June 2025 for most compounds at most sites (end of 2025 for CH4)
- HFOs 1234yf, 1234zee and hcfo-1233zde released (Vollmer et al., 2026: https://doi.org/10.5194/acp-26-6993-2026)
- 1,2 dichloroethane (ClH2CH2Cl, clch2ch2cl) released (Pitt, Rust et al., 2026: https://doi.org/10.5194/acp-26-10167-2026)
- CMN HFC-23 ADS data released
- MUG (Mt. Mugogo, Rwanda) CH4 data released
- Previously withheld ZEP HCFC-22 Medusa data released after 2024-05-31
- Previously withheld THD CH4 Picarro data released after 2024-12-31
- Previously withheld TAC HFC-4310mee released data after 2023-06-20
- Data are now processed against the agage-archive v0.3.0, which includes several bug fixes


## [20251230] - 2025-12-30

December 2025 update of the ALE/GAGE/AGAGE data archive. Data were most recently reviewed at the AGAGE 72 meeting, 17-20 December, 2025.

### Changed
- Data updated up to the end of 2024 for most compounds (end of June 2025 for CH4)
- TOB HFC-134a data has been withheld while potential local leaks are investigated
- TOB CF4 data is now released after the invalid periods were flagged
- GSN records have been extended to more recent dates for some species
- THD Picarro CH4 is withheld for 2025 while a potential calibration issue is investigated


## [20250721] - 2025-07-21

July 2025 update of the ALE/GAGE/AGAGE data archive. Data were most recently reviewed at the AGAGE 71 meeting, 9-13 June, 2025.

### Changed
- Data updated through July 2024 for most compounds
- Data files now have a more uniform set of variables: mf_count, instrument_type, etc. are included in all files, whether strictly required or not
- Small amount of MHD CF4 data removed June - September 2022, due to potential trap icing issue that needs investigating
- Carbon monoxide (CO) data from MHD and CGO are now released on the calibration scales used by the individual labs: MHD on WMO-X2014A and CGO on CSIRO-2020.


## [20250123] - 2025-01-23

This version represents several major changes in the way that AGAGE data are archived and formatted. Data will now be released in a Climate and Forecasting (CF) convention-compliant netCDF format. The archive contains several sets of files:
- a "recommended" file for each site and species, where the relevant ALE/GAGE/AGAGE measurements from a range of instruments have been combined together, with instrument change-over dates specified by the data owner
- "individual instrument" files for each site, species and instruments. This represents the entire public ALE/GAGE/AGAGE dataset, including periods where species have been simultaneously measured in different instruments
- monthly baseline mean mole fractions, representative of monthly averages at a particular site, where conditions have been identified as baseline
- baseline flags as estimated by the Georgia Tech. statistical baseline algorithm

Efforts have been made to restore ALE and GAGE observations and combine them with the AGAGE record in a consistent format, and some early GCMS measurements have also been restored to the archive. 

### Added

- Repeatabilities have been included for ALE and GAGE measurements, based on values inferred from early AGAGE literature (see code repository notes for further details)
- Early GCMS-ADS "Magnum" data have been restored to the public archive
- A "recommended" record for each site and species is provided, so that users do not have to decide which instrument(s) to use for a given time period

### Fixed

- ALE and GAGE timestamps have been converted to UTC (previously local time in some versions)

### Changed

- Data generally released through 2023 (with some exceptions as noted in release schedule in code repository)
- Files are now presented only in netCDF format
- File naming convention has been established:
  - For recommended files: ```agage_<site>_<species>_<version>.nc```
  - For individual instrument files: ```agage-<instrument>_<site>_<species>_<version>.nc```
- Baseline flags are provided in separate files to the observations

### Removed

- Files are not currently provided in ASCII format