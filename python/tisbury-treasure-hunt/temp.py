
def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records.

    :param combined_record_group: tuple - everything from both participants.
    :return: str - everything "cleaned", excess coordinates and information are removed.

    The return statement should be a multi-lined string with items separated by newlines.

    (see HINTS.md for an example).
    #q:count the number of items in the tuple
    #a: len(combined_record_group)

    """
    firstString = " \"\"\" "
    cleanedString = ""
    cleanedString = cleanedString + firstString + "\n"
    singleRecord = ""
    for item in combined_record_group:
        singleRecord = item[0], item[2], item[3],item[4]
        cleanedString = cleanedString + str(singleRecord) + "\\n" + "\n"

    cleanedString = cleanedString + firstString + "\n"
    return cleanedString

returnedString = clean_up((('Brass Spyglass', '4B', 'Abandoned Lighthouse', ('4', 'B'), 'Blue'), ('Vintage Pirate Hat', '7E', 'Quiet Inlet (Island of Mystery)', ('7', 'E'), 'Orange'), ('Crystal Crab', '6A', 'Old Schooner', ('6', 'A'), 'Purple')))
print(returnedString)