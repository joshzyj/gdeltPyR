#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author:
# Linwood Creekmore
# Email: valinvescap@gmail.com

from io import BytesIO
import pandas as pd
import requests


#######################################
# Headers for GDELT 1.0 Events
#######################################

def events1Heads():
    # type: () -> object
    """

    :rtype: dateframe
    """
    eventsDbHeaders = pd.read_csv(
        BytesIO(
            requests.get(
                ("https://raw.githubusercontent.com/linwoodc3/gdeltPyR"
                 "/master/utils/schema_csvs/"
                 "GDELT_1.0_event_Column_Labels_Header_Row_Sep2016.tsv")
            ).content), delimiter='\t', usecols=['tableId'])
    return eventsDbHeaders.tableId.tolist()


#######################################
# Headers for GDELT 2.0 Events
#######################################

def events2Heads():
    eventsDbHeaders = pd.read_csv(
        BytesIO(
            requests.get(
                ("https://raw.githubusercontent.com/linwoodc3/gdeltPyR/"
                 "master/utils/schema_csvs/"
                 "GDELT_2.0_Events_Column_Labels_Header_Row_Sep2016.csv")
            ).content), delimiter=',', usecols=['tableId', 'dataType',
                                                'Description'])
    return eventsDbHeaders.tableId.tolist()


#######################################
# Headers for GDELT 2.0 Mentions
#######################################

def mentionsHeads():
    eventsMentionsHeaders = pd.read_csv(
        BytesIO(
            requests.get(
                ("https://raw.githubusercontent.com/linwoodc3/gdeltPyR/master/"
                 "utils/schema_csvs/"
                 "GDELT_2.0_eventMentions_Column_Labels_Header_"
                 "Row_Sep2016.tsv")
            ).content), delimiter='\t', usecols=['tableId', 'dataType',
                                                 'Description'])
    return eventsMentionsHeaders.tableId.tolist()


#######################################
# Headers for GDELT 2.0 GKG
#######################################

def gkgHeads():
    gkgHeaders = pd.read_csv(
        BytesIO(
            requests.get(
                ("https://raw.githubusercontent.com/linwoodc3/gdeltPyR/"
                 "master/utils/schema_csvs/"
                 "GDELT_2.0_gdeltKnowledgeGraph_Column_Labels_Header_Row_"
                 "Sep2016.tsv")
            ).content), delimiter='\t', usecols=['tableId', 'dataType',
                                                 'Description'])
    return gkgHeaders.tableId.tolist()
