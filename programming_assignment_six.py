# Team Members: Jonathan Ramos
# Course: CS151, Dr. Rajeev
# Programming Assignment: 6
# Program Inputs:
# Program Outputs:

# All index values
page_total_likes = 0
type_of_post = 1
category = 2
post_month = 3
post_weekday = 4
post_hour = 5
paid = 6
lifetime_post_total_reach = 7
lifetime_post_total_impressions = 8
lifetime_engaged_users = 9
lifetime_post_consumers = 10
lifetime_post_consumptions = 11
lifetime_post_impressions_liked_page = 12
lifetime_post_reach_liked_page = 13
lifetime_people_liked_and_engaged_with_post = 14
comments = 15
likes = 16
shares = 17
total_interactions = 18


# Creating a list of list from data file
def list_data(filename):
    data = []
    try:
        posts = open(filename, "r")
        # Tracks line
        line_counter = 0
        for line in posts:
            # Converts each line to a list of its proper type
            try:
                # For every line in the given file it will separate the string into a list using "," as a separator
                line_entries = line.split(";")
                # Converts element of created list into its proper type
                line_entries[page_total_likes] = int(line_entries[page_total_likes])
                line_entries[type_of_post] = line_entries[type_of_post].strip()
                line_entries[category] = int(line_entries[category])
                line_entries[post_month] = int(line_entries[post_month])
                line_entries[post_weekday] = int(line_entries[post_weekday])
                line_entries[post_hour] = int(line_entries[post_hour])
                line_entries[paid] = int(line_entries[paid])
                line_entries[lifetime_post_total_reach] = int(line_entries[lifetime_post_total_reach])
                line_entries[lifetime_post_total_impressions] = int(line_entries[lifetime_post_total_impressions])
                line_entries[lifetime_engaged_users] = int(line_entries[lifetime_engaged_users])
                line_entries[lifetime_post_consumers] = int(line_entries[lifetime_post_consumers])
                line_entries[lifetime_post_consumptions] = int(line_entries[lifetime_post_consumptions])
                line_entries[lifetime_post_impressions_liked_page] = int(line_entries[lifetime_post_impressions_liked_page])
                line_entries[lifetime_post_reach_liked_page] = int(line_entries[lifetime_post_reach_liked_page])
                line_entries[lifetime_people_liked_and_engaged_with_post] = int(line_entries[lifetime_people_liked_and_engaged_with_post])
                line_entries[comments] = int(line_entries[comments])
                line_entries[likes] = int(line_entries[likes])
                line_entries[shares] = int(line_entries[shares])
                line_entries[total_interactions] = int(line_entries[total_interactions])
                # Adds the line made into a list into the list of lists which will contain all the data
                data.append(line_entries)
                line_counter += 1
            # Will run if the line is not of the correct type
            except ValueError:
                pass
                print("Value not accepted, line", (line_counter + 1), "will be skipped!")
        # Closes the file given by the user
        posts.close()
    # Will run if the file given by the user is not found
    except FileNotFoundError:
        print("File Not Found!")
        exit()
    return data


facebook_data_list = list_data("facebook.csv")
print(facebook_data_list)
