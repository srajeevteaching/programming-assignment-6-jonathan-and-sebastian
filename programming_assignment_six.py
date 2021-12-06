# Team Members: Jonathan, Sebastian
# Course: CS151, Dr. Rajeev
# Programming Assignment: 6
# Program Inputs:
# Program Outputs:
import matplotlib.pyplot as plt

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
        line_counter = 1
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
                print("Line", line_counter,  "will be skipped! Value not accepted.")
        # Closes the file given by the user
        posts.close()
    # Will run if the file given by the user is not found
    except FileNotFoundError:
        print("File Not Found!")
        exit()
    return data


def save_file(filename, data_list):
    # Opens/Creates a new file with the name given by the user
    with open(filename, "w") as file:
        for line in data_list:
            for element in line:
                # Writes each element in the list and separates it by semi-colon until the list finishes
                file.write(str(element) + ";")
            file.write("\n")


def find_difference(data_list):
    new_list = []
    # Loops through the data list
    for i in range(len(data_list)):
        temp_list = []
        # Finding the difference between likes and shares if likes is greater or equal to shares
        if data_list[likes] > data_list[shares]:
            current_post_difference = data_list[i][likes] - data_list[i][shares]
            temp_list.append(current_post_difference)
            if current_post_difference <= 25:
                change = "the same"
                temp_list.append(change)
            elif 25 < current_post_difference < 100:
                change = "more likes"
                temp_list.append(change)
            elif current_post_difference >= 100:
                change = "significantly more likes"
                temp_list.append(change)
        else:
            # Finding the difference between likes and shares if shares is greater than likes
            current_post_difference = data_list[shares] - data_list[likes]
            temp_list.append(current_post_difference)
            if current_post_difference <= 25:
                change = "the same"
                temp_list.append(change)
            elif 25 < current_post_difference < 100:
                change = "more shares"
                temp_list.append(change)
            elif current_post_difference >= 100:
                change = "significantly more shares"
                temp_list.append(change)
        new_list.append(temp_list)
    return new_list


def create_graph_data(data_list):
    engaged_users = []
    low_users = 0
    moderate_users = 0
    high_users = 0
    for i in range(len(data_list)):
        engaged_users.append(data_list[i][lifetime_engaged_users])
    print(engaged_users)
    for j in range(len(engaged_users)):
        if engaged_users[j] < 100:
            low_users += 1
        elif 100 <= engaged_users[j] <= 400:
            moderate_users += 1
        elif engaged_users[j] > 400:
            high_users += 1
    list_of_engaged_user_count = [low_users, moderate_users, high_users]
    return list_of_engaged_user_count


def posts_dictionary(data_list):
    word_list = []
    for i in range(len(data_list)):
        word_list.append(data_list[i][type_of_post])

    posts_count = {}
    for word in word_list:
        if word in posts_count:
            posts_count[word] += 1
        else:
            posts_count[word] = 1
    return posts_count


def main():
    continue_program = True
    while continue_program:
        # Loading Data From User File
        file_input = input("Enter Name of File: ")
        print("Opening File...")
        facebook_data_list = list_data("facebook.csv")
        # print(facebook_data_list)
        # Listing Program Options
        print("\nChoose From The Following: 'Find Differences', 'Graph', 'Avg Likes', 'Most Popular Day'")
        program_option = input("Program Option: ").lower().strip()
        # First Program Option, Finding Difference Between Likes and Shares
        if program_option == "find differences":
            # Creating List of List of Differences
            difference_list = find_difference(facebook_data_list)
            # print(difference_list)
            # Getting User Input For The Name Of The File Where This Data Will Be Saved
            new_file_name = input("Please Enter File Name Of Where You Would Like To Write or Save Data: ")
            # Saving The File With the List of List of Differences
            save_file(new_file_name, difference_list)
            print("Done! A new file named,", new_file_name, "was created!")
            # Asking User To Continue Or End Program
            continue_choice = input("\nWould you like to run this program again or end (choices: 'again' or 'end'): ")
            continue_choice = continue_choice.lower().strip()
            if continue_choice != "again":
                print("Ending Program...")
                continue_program = False

        elif program_option == "graph":
            graph_data = create_graph_data(facebook_data_list)
            x = ["Low", "Moderate", "High"]
            y = [graph_data[0], graph_data[1], graph_data[2]]
            plt.bar(x, y)
            plt.xlabel("Amount Of Engaged Users")
            plt.ylabel("Number Of Posts")
            print("Ending Program...Graph of posts with low, moderate, and high numbers of engaged users was created!")
            plt.show()
            break

        elif program_option == "avg likes":
            list_of_likes = [0, 0, 0, 0]
            list_of_averages = []
            count_photo = 0
            count_status = 0
            count_link = 0
            count_video = 0

            for i in range(len(facebook_data_list)):
                if facebook_data_list[i][type_of_post] == "Photo":
                    list_of_likes[0] += facebook_data_list[i][likes]
                    count_photo += 1
                elif facebook_data_list[i][type_of_post] == "Status":
                    list_of_likes[1] += facebook_data_list[i][likes]
                    count_status += 1
                elif facebook_data_list[i][type_of_post] == "Link":
                    list_of_likes[2] += facebook_data_list[i][likes]
                    count_link += 1
                elif facebook_data_list[i][type_of_post] == "Video":
                    list_of_likes[3] += facebook_data_list[i][likes]
                    count_video += 1

            try:
                list_of_averages.append(round(list_of_likes[0] / count_photo, 2))
                list_of_averages.append(round(list_of_likes[1] / count_status, 2))
                list_of_averages.append(round(list_of_likes[2] / count_link, 2))
                list_of_averages.append(round(list_of_likes[3] / count_video, 2))
            except ZeroDivisionError:
                print("There Was An Error Finding The Average, Division By 0 Not Allowed.")

            print("\nPhoto Posts Average Amount Of Likes:", list_of_averages[0])
            print("Status Posts Average Amount Of Likes:", list_of_averages[1])
            print("Link Posts Average Amount Of Likes:", list_of_averages[2])
            print("Video Posts Average Amount Of Likes:", list_of_averages[3])

            highest_likes = max(list_of_averages)
            highest_likes_index = list_of_averages.index(highest_likes)
            if highest_likes_index == 0:
                print("\nThe Post Type With The Highest Amount Of Likes on Average: Photos")
            elif highest_likes_index == 1:
                print("\nThe Post Type With The Highest Amount Of Likes on Average: Status")
            elif highest_likes_index == 2:
                print("\nThe Post Type With The Highest Amount Of Likes on Average: Link")
            if highest_likes_index == 3:
                print("\nThe Post Type With The Highest Amount Of Likes on Average: Video")

            continue_choice = input("\nWould you like to run this program again or end (choices: 'again' or 'end'): ")
            continue_choice = continue_choice.lower().strip()
            if continue_choice != "again":
                print("Ending Program...")
                continue_program = False


main()
