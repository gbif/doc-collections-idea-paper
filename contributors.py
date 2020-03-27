#!/bin/python3

import csv

with open('contributors.csv', newline='') as csvfile:
    contributorsreader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in contributorsreader:
        fullName = "{first} {last}".format(first=row['fname'], last=row['lname'])
        if row['orcidId']:
            linkedName = "{orcid}[{fullName}]".format(orcid=row['orcidId'], fullName=fullName)
        else:
            linkedName = fullName

        affiliations = ", ".join(filter(None, [row['affiliation'], row['affiliation2']]))

        print("* {0}, {1}".format(linkedName, affiliations))
