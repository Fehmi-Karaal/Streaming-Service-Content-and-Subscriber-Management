from program import *
from subscriber import *
from streaming_service import *
import csv

'''This file contains functions that are used for processing the files associated with
streaming services.'''

# This function reads a data file containing a streaming service's information.
def build_new_service(file):

    # instantiate a StreamingService object.
    stream_service = StreamingService()
    # used try/except to ensure that the file it is passed is valid.
    try :
        # reading csv file
        with open(file, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            i = False
            type = 0
            for line in reader:
                # The first line of the file is the name of the streaming service.
                if (not i):
                    stream_service.set_name(line[0].upper())
                    i = True
                # find PROGRAMS line
                if (line[0] == "PROGRAMS"):
                    type = 1
                # find SUBSCRIBERS line
                elif (line[0] == "SUBSCRIBERS"):
                    type = 2
                # Everything after PROGRAMS and before SUBSCRIBERS listed as a Program object.
                elif (type == 1):
                    temp_program = Program(line[0], line[1], line[2], line[3])
                    print("Adding program...", line[0])
                    stream_service.add_program(temp_program)
                # Everything after SUBSCRIBERS listed as a Subscriber object.
                elif (type == 2):
                    temp_subscriber = Subscriber(line[0], line[1], line[2])
                    print("Adding subscriber...", line[0])
                    stream_service.add_subscriber(temp_subscriber)
    # except the file it is passed is not valid
    except FileNotFoundError:
            return None
    return stream_service

# This function reads an update file containing changes to a streaming service's data.
def update_service(update_file, stream_service):
    # use try/except to ensure that the file it is passed is valid
    try :
        # reading csv file
        with open(update_file, encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            i = False
            type = 0

            for line in reader:
                # The first line of the file is the name of the streaming service.
                if (not i):
                    stream_service.set_name(line)
                    i = True
                # find PROGRAMS line
                if (line[0] == "PROGRAMS"):
                    type = 1
                # find SUBSCRIBERS line
                elif (line[0] == "SUBSCRIBERS"):
                    type = 2
                # update PROGRAMS
                elif (type == 1):
                    if (line[0] == '^'):
                        temp_program = stream_service.get_program(line[1])
                        if (temp_program == None):
                            return None
                        print("Updating program...", line[1])
                        if (line[1] != ''):
                            temp_program.set_title(line[1])
                        if (line[2] != ''):
                            temp_program.set_genre(line[2])
                        if (line[3] != ''):
                            temp_program.set_creator(line[3])
                        if (line[4] !=''):
                            temp_program.set_release_date(line[4])
                    elif (line[0] == '-'):
                        print("Removing program...", line[1])
                        stream_service.remove_program(line[1])
                    elif (line[0] == '+'):
                        temp_program = Program(line[1], line[2], line[3], line[4])
                        print("Adding program...", line[1])
                        stream_service.add_program(temp_program)
                # update SUBSCRIBERS
                elif (type == 2):
                    if (line[0] == '^'):
                        temp_subscriber = stream_service.get_subscriber(line[1])
                        print("Updating subscriber...", line[1])
                        if (line[1] != ''):
                            temp_subscriber.set_name(line[1])
                        if (line[2] != ''):
                            temp_subscriber.set_userid(line[2])
                        if (line[3] != ''):
                            temp_subscriber.set_password(line[3])
                    elif (line[0] == '-'):
                        print("Removing subscriber...", line[1])
                        stream_service.remove_subscriber(line[1])
                    elif (line[0] == '+'):
                        temp_subscriber = Subscriber(line[1], line[2], line[3])
                        print("Adding subscriber...", line[1])
                        stream_service.add_subscriber(temp_subscriber)
    # except the file it is passed is not valid
    except FileNotFoundError:
        return None
    return stream_service

#This function writes the updated streaming service to a new file.
def write_update(write_file, stream_service):
    # open writing csv file
    writer = open(write_file, 'w', encoding='utf-8')
    # write the name of the service
    writer.write(stream_service.get_name()[0])
    # write second line as  PROGRAMS
    writer.write("\nPROGRAMS\n")
    # streaming_service programs variable
    list_temp = stream_service.get_programs()

    # write the list of Program objects
    for i in list_temp:
        row = []
        row.append(i.get_title())
        row.append(i.get_genre())
        row.append(i.get_creator())
        row.append(i.get_release_date())
        writer.write(','.join(row))
        writer.write("\n")

    writer.write("SUBSCRIBERS\n")

    list_temp = stream_service.get_subscribers()
    # write the list of Subscriber objects
    for i in list_temp:
        row = []
        row.append(i.get_name())
        row.append(i.get_userid())
        row.append(i.get_password())
        writer.write(','.join(row))
        writer.write("\n")
