def split_text(text, segment_length=40, overlap_percent=0.5):
    # text: a string containing the corpus of text
    # segment_length: an integer indicating the number of words in each segment
    # overlap_percent: a float between 0 and 1 indicating the percentage of overlap between segments
    # returns: a list of strings containing the overlapping segments

    # check if the parameters are valid
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not isinstance(segment_length, int) or segment_length <= 0:
        raise ValueError("segment_length must be a positive integer")
    if not isinstance(overlap_percent, float) or overlap_percent < 0 or overlap_percent > 1:
        raise ValueError("overlap_percent must be a float between 0 and 1")

    # initialize an empty list to store the segments
    segments = []

    # split the text into words by whitespace
    words = text.split()

    # calculate the number of words to skip for each segment
    skip = int(segment_length * (1 - overlap_percent))

    # loop through the words with a sliding window
    for i in range(0, len(words), skip):
        # get the current segment by slicing the words
        segment = " ".join(words[i:i+segment_length])
        # append the segment to the list
        segments.append(segment)

    return segments
