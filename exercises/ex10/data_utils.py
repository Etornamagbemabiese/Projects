"""Working with CSV Data."""

from csv import DictReader

__author__ = "730645861"


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read csv file and return as a list of dicts with the headers as the keys."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader: 
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], header: str) -> list[str]:
    """Return a list of all values under a specific header."""
    result: list[str] = []
    # loop through each element (dictionary) of the list
    for elem in table:
        # for each dictionary (elem), get the value at key "header" and add that to result
        result.append(elem[header])
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Reformat data so it's a dictionary with column headers as keys."""
    result: dict[str, list[str]] = {}
    # loop through keys of one row of the table to get the headers
    first_row: dict[str, str] = table[0]
    for key in first_row:
        # for each key (header), make a dictionary entry with all the column values
        result[key] = column_values(table, key)
    return result


def head(dicinput: dict[str, list[str]], intinput: int) -> dict[str, list[str]]:
    """Producing a column based table with only the first parameter rows of data."""
    retdict: dict[str, list[str]] = {}
    for x in dicinput:
        inplist: list[str] = []
        counter: int = 0  
        while counter < intinput and counter < len(dicinput[x]):
            inplist.append(dicinput[x][counter])
            counter += 1
        retdict[x] = inplist  

    return retdict


def select(dicinput: dict[str, list[str]], lisinput: list[str]) -> dict[str, list[str]]:
    """Produces a new column based table with only a specific subset of the original columbs."""
    retdict: dict[str, list[str]] = {}
    for x in lisinput:
        retdict[x] = dicinput[x]
    return retdict


def concat(inpone: dict[str, list[str]], inptwo: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column based table with two column based tables combined."""
    retdict: dict[str, list[str]] = {}
    for x in inpone:
        retdict[x] = inpone[x]
    for x in inptwo:
        if x in retdict:
            retdict[x] += inptwo[x]
        else:
            retdict[x] = inptwo[x]
        
    return retdict