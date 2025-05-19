# Microservice for Sasan's travel planning program

## Purpose

This program will list popular vacation spots in a geographical area.

### Dependencies

This software uses the geoapify API to retrieve location data. the api key for the software
is kept in a file named "geoapify_key.txt", in a single line with no whitespace.
A free API key can be obtained at their website https://www.geoapify.com/ and
following their instructions.

### Requesting Data

Requesting data from this system can be done by writing to a "sites.txt" file.
Formatting input:
When requesting data, write "get" to the first line of the file, and the area in which
to search to the second line [Edit note: Once you know how to format geo data for
software include that]

### Receiving Data

When the system has the data ready, the first line will read "got". Each following line
will contain data related to each found locale in the following format:
Line will contain locale name, location, average rating, and a link to the locale's website
if available.

## UML Sequence Diagram

![Diagram of the action sequence of the software.] (Software-Eng-1-2025/MicroserviceTPlanner/microservice.png)
