"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    try:
        os.mkdir('temp')
        # Loop through each file in the (current) directory
        for filename in os.listdir('.'):
            # Ignore directories, just process files
            if os.path.isdir(filename):
                continue

            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

    except FileExistsError:
        pass


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename.title()
    previous = ''

    if ' ' in filename:
        new_name = filename.replace(" ", "_").replace(".TXT", ".txt")

    new_name = ''
    for i in filename:
        if i.isupper() and previous.islower():
            new_name += '_'
        else:
            new_name += i
        print(new_name)
        previous = i
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

    for filename in filenames:
        full_name = os.path.join(directory_name, filename)
        new_name = get_fixed_filename(full_name)
        print(new_name)


# main()
demo_walk()
