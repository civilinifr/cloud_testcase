"""
Scratch codes to test certain functionality
"""
import glob
from datetime import datetime
from obspy.core import read
from matplotlib import pyplot as plt
import numpy as np
import os
import requests
import datetime as dt
import pds.peppi as pep

def main():
    """
    Main wrapper function

    :return:
    """

    client = pep.PDSRegistryClient()

    day_to_download = '1970-03-25'
    day = datetime.strptime(day_to_download, "%Y-%m-%d")

    products = pep.Products(client).of_collection("urn:nasa:pds:apollo_pse:data_seed::1.0")

    dataless_data_products = [p for p in products if
                             p.properties["pds:File.pds:file_name"][0] == 'dataless.xa.0.seed']
    #'pds:File.pds:file_name': ['xa.s12..att.1970.084.0.mseed'],

    for p in products:

        cake = 'good'
    seismic_data_products = [p for p in products if
                             p.properties["apollo:Seismic_Parameters.apollo:pse_data_type"][0] == "waveform"]



    for p in seismic_data_products:
        print(p.id, p.properties["apollo:Seismic_Parameters.apollo:channel"][0],
              p.properties["ops:Data_File_Info.ops:file_ref"][0])
    return

main()