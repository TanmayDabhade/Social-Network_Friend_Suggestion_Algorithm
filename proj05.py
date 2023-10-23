# Uncomment the following lines if you run the optional run_file tests locally
# so the input shows up in the output file. DO NOT uncomment these lines
#
# import sys
# def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str

# Computer Project 5
# Algorithm
#   1. Ask user to input a file name
#   2. Open the file
#   3. Read the file
#   4. Create a list of lists
#   5. Create a function to calculate the number of common friends between two lists
#   6. Create a function to calculate the similarity scores
#   7. Create a function to recommend a friend for a user
#   8. Ask user to input an integer between 0 and the length of the list - 1
#   9. Print the suggested friend for the user
#   10. Ask user if they want to continue
#   11. If yes, repeat step 8
#   12. If no, end the program

'''This program will read in a file containing a social network and
    recommend a friend for a user based on the similarity of their
    network.'''

def open_file():
    '''This function will ask the user to input a file name and open the file.
    If the file doesn't exist it will ask the user to input a new file name.
    The try/except method is used to catch the FileNotFoundError.
    This function will return the file object.'''
    file_name = input("Enter a filename: ")
    while True:
        try:
            file_o = open(file_name, 'r')
            return file_o
        except FileNotFoundError:
            print("Error in filename.")
            file_name = input("Enter a filename: ")



def read_file(fp):
    '''This function will read the file and create a list of lists of the network data provided by the user input.
    this function will return the list of lists.'''
    n = int(fp.readline())
    network_list = [[] for fp in range(n)]
    for line in fp:
        u,v = line.split()
        u = int(u)
        v = int(v)
        network_list[u].append(v)
        network_list[v].append(u)
    return network_list


def num_in_common_between_lists(list1, list2):
    '''This function will calculate the number of common friends between two lists.
    and return the number of common friends by incrementing 1 to the count variable for each common friend.
    This function uses the for loop to iterate through the first list and then finds whether the index in the first
    list exists in the second list. If the index exists the count variable will be incremented by 1. if not the loop
    will continue to the next index in the first list.'''
    count = 0
    for i in list1:
        if i in list2:
            count += 1
    return count



def calc_similarity_scores(network_list):
    '''This function will calculate the similarity scores between each pair of users.
    This function will return a list of lists of the similarity scores.
    This function uses the for loop to iterate through the network list and append an empty list to the sim_matrix list.
    Then it uses another for loop to iterate through the network list again and append the number of common friends
    between the two lists to the empty list in the similarity matrix list.
    Then it returns the similarity matrix list refered here as sim_matrix. The sim_matrix list consists of the indexes
    and corresponding lists of common friend counts between the two lists.'''
    sim_matrix = []
    for i in range(len(network_list)):
        sim_matrix.append([])
        for j in range(len(network_list)):
            sim_matrix[i].append(num_in_common_between_lists(network_list[i],network_list[j]))
    return sim_matrix



def recommend(user_id, network_list, sim_matrix):
    '''This function will recommend a friend for a user based on the similarity of their network.
    This function will return the index of the user with the highest similarity score.
    This function uses the for loop to iterate through the similarity matrix list and find the index of the highest
    similarity score. It also uses the if statement to check if the index is not the user_id and not in the user's
    friends list. If the index is not the user_id and not in the user's friends list, it will check if the similarity
    score is greater than the current similarity score. If it is, it will replace the current similarity score with
    the new similarity score. If it is not, it will continue to the next index in the similarity matrix list.
    Then it will return the index of the user with the highest similarity score.'''
    user_id = int(user_id)
    score = sim_matrix[user_id]
    user_friends = network_list[user_id]
    sim_matrix = -1
    max = -1
    for i, sim_score in enumerate(score):
        if i not in user_friends and i != user_id:
            if sim_score > sim_matrix:
                sim_matrix = sim_score
                max = i
            elif sim_score == sim_matrix:
                if i < max:
                    max = i
    return max


def main():
    # by convention "main" doesn't need a docstring
    print("Facebook friend recommendation.\n")
    fp = open_file()                 #used to open the file
    network_list = read_file(fp)     #used to read the file
    sim_matrix = calc_similarity_scores(network_list)  #used to calculate the similarity scores
    while True:                        #used for asking user input for user_id if the previous input is not an integer
        user_id = input("\nEnter an integer in the range 0 to {}: ".format(len(network_list) - 1))
        try:                                              #used to check for user_id inputs which are not integers
            user_id = int(user_id)                       #used to convert the user_id input to an integer
            if user_id < 0 or user_id > len(network_list) - 1:      #used to check for user_id inputs
                                                                    # which are not in the range
                raise ValueError                                    #raises ValueError if the user_id is not in range
            rec_friend = recommend(user_id, network_list, sim_matrix) #used to recommend a friend for the user
            print("\nThe suggested friend for {} is {}".format(user_id, rec_friend)) #used to print the suggested friend
            continue_permission = input("Do you want to continue (yes/no)? ")
            if continue_permission.lower() == 'yes':                #used to check if the user wants to continue
                continue
            else:
                break
        except ValueError:                               #used to catch the ValueError
            print("\nError: input must be an int between 0 and {}".format(len(network_list) - 1))


if __name__ == "__main__":
    main()

