# Microservice for Sasan's travel planning program

## Purpose

This program will list popular vacation spots in a geographical area.

### Dependencies

This software uses the geoapify API to retrieve location data. the api key for the software
is kept in a file named "geoapify_key.txt", in a single line with no whitespace.
A free API key can be obtained at their website https://www.geoapify.com/ and
following their instructions.

### Requesting Data

Requesting data from this system can be done by writing input to a "sites.txt" file,
and running the main file.
Formatting input:
1st line: "get" (tells software to search for given data)
2nd line: name of area to search in
3rd line: limit. This should be an integer value, showing how many locations to fetch
data for.
4th line: category. A full list of acceptable location categories to search for can be found
at https://apidocs.geoapify.com/docs/places/ in the long table labeled "supported Categories".
5th line: area type. "city" or "state" are acceptable values.

### Receiving Data

When the system has the data ready, the first line will read "got". Each following line
will contain data related to each found locale in the following format:
Line will contain locale name, a link to the locale's website if available (if none will say "No website"),
latitude and longitude coordinates, and hours if any (if none will say "no hours").
Each piece of data will be separated by commas.

## UML Sequence Diagram

The Sequence Diagram for this project can be found in the file "microservice.png", in this folder.
Note: the watermark covered up the name of one of the actors so I left a not labeling it.
