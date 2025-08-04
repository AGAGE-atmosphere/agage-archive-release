# Data specification files for releasing the public AGAGE archive

Uses the [agage-archive](https://github.com/AGAGE-atmosphere/agage-archive) code to process ALE/GAGE/AGAGE data into a set of netCDF files for public release.

Release schedules (typically stating the final date through which the data should be released) for individual species on each instrument are in ```data/agage/data_release_schedule_{INSTRUMENT}.csv```.

Any unflagged data that should be excluded from the public archive can be specified in ```data/agage/data_exclude/data_exclude_{SITE}.csv```

Individual instruments can be combined into a "recommended" continuous data record by adding to species to ```data/agage/data_combination/data_combination.csv```.

These files should be updated for each new release, and a new tagged version of this repo created.

For running on DAGAGE2, the following setup should work:

- create symlinks in ```data/agage```

```
data-gcms-nc -> /agage/summary/netcdf/ms
data-nc -> /agage/summary/netcdf/md
data-optical-nc -> /agage/summary/netcdf/optical
```

- Specify instrument paths in ```config.yaml```

```
paths:
  agage:
    ALE_path: ale_gage_sio1993/ale
    GAGE_path: ale_gage_sio1993/gage
    GCMD_path: data-nc
    GCMS-ADS_path: data-gcms-nc
    GCECD_path: data-nc
    GCMS-MteCimone_path: data-gcms-nc
    GCPDD_path: data-nc
    GCMS-Medusa_path: data-gcms-nc
    GCMS-Magnum_path: data-gcms-magnum.tar.gz
    Picarro_path: data-optical-nc
    Picarro-1_path: data-optical-nc
    Picarro-2_path: data-optical-nc
    LGR_path: data-optical-nc
    GCTOFMS_path: data-gcms-nc
    output_path: agage-public-archive.zip
```