# Arctic Carbon
This repository contains processing and plotting code for 'common carbon variables' from CMIP6 model outputs to provide the basis of an analysis of the Arctic carbon budget done at UHH in cooperation with UBA.

## Notebook Overview
- AC-data-processing
  - calculate annual mean or sum from CMIP6 RAW data on Levante
  - calculate spatial sum
  - apply regional masks
- AC-Combine-vars-CDO
  - Calculate (using CDO) additional variables by adding or subtracting the base variables processed in the previous script
- AC-RECCAP-plots
  - Code to reproduce RECCAP2 plots
- AC-maps
  - Map plots for all varibales comparing ssp126 and ssp370 to historical
- AC-catalog-search-example
  - example output from ```search_cmip6-catalog.py```
- CMIP6-Model-availability
  - Code to check with intake which models have a certain set of varibles
  - Produces a table with color coded entries
- UHH-CMIP6_Create-gridareas_modified
  - adapted code from the UHH SIA CMIP6 product
  - Processing functions to calculate gridareas using CDO for land and ocean vars

## Flowchart of AC-data-processing
![Flowchart](https://github.com/QuentinRauschenbach/ArcticCarbon/blob/master/code/Flowchart.png)
