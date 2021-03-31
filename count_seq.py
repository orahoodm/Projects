# Author: Morgan Orahood
# Date: 2/22/2021
# Description: A program that uses a generator function to generate a specific sequence.

def count_seq():
    """A generator function that doesn't take any parameters and generates a specific sequence."""
    # Starting point for sequence
    number = "2"
    # Used to organize the new values in the sequence - will clear throughout program
    organizer = ""
    count = 0
    # Used to refer to the current sequence to help with creating the next sequence
    sequence = ""
    while True:
        # Initializes sequence to start with "2" and will yield it to the generator
        if len(number) == 1:
            sequence += number
            organizer += number
            # Clears number and this variable is no longer used
            number = ""
        elif organizer == "2":
            # Initializes organizer
            organizer = ""
            first_number = sequence[0]
            count += 1
            # Add count (1) and first number (2) to the organizer
            organizer += str(count) + str(first_number)
            # Sequence becomes empty and the organizer yields to the generator
            sequence = sequence[1:]
            sequence += organizer
        else:
            # Initializes organizer
            organizer = ""
            while len(sequence) > 0:
                # Will continue to make the first number variable equal to the first string in sequence
                first_number = sequence[0]
                count = 0
                # If first number equals the first string in sequence - continue to count and drop 1 integer at a time
                while len(sequence) > 0 and sequence[0] == first_number:
                    count += 1
                    sequence = sequence[1:]
                # Add count and first number to organizer to yield to generator
                organizer += str(count) + str(first_number)
            # Add to sequence to have a reference for the next value
            sequence += organizer
        yield organizer



