# Data specification files for releasing the public AGAGE archive

Uses the [agage-archive](https://github.com/AGAGE-atmosphere/agage-archive) code to process ALE/GAGE/AGAGE data into a set of netCDF files for public release.

Release schedules (typically stating the final date through which the data should be released) for individual species on each instrument are in ```data/agage/data_release_schedule_{INSTRUMENT}.csv```.

Any unflagged data that should be excluded from the public archive can be specified in ```data/agage/data_exclude/data_exclude_{SITE}.csv```

Individual instruments can be combined into a "recommended" continuous data record by adding to species to ```data/agage/data_combination/data_combination.csv```.

These files should be updated for each new release, and a new tagged version of this repo created.
