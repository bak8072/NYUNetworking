# welcome_assignment_answers
# Input - All eight questions given in the assignment.
# Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    # The student doesn't have to follow the skeleton for this assignment.
    #    #Another way to implement is using a "case" statements similar to C.

    global answer
    if question == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is it possible to decode a message without a key? - Yes/No":
        answer = "No"
    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question == "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use " + \
            "MD5 hash generator and use the answer in your code":
        answer = 'b21bed4510d4c731cf6a8afe2c2bc071'
    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "Yes"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? -" + \
            " The answer should be a numeric number":
        answer = "4"
    elif question == "What layer of the TCP/IP model the protocol TCP belongs to? -" + \
            "The answer should be a numeric number":
        answer = "3"
    return answer


# Complete all the questions.


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
