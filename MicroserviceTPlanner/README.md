# Microservice for Sasan's travel planning program

## Purpose

This program will list popular vacation spots in a geographical area.

### Requesting Data

Requesting data from this system can be done by writing to a "popular_sites.txt" file.
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
