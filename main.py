# build a program that will auto detect key words (specific words) that have to deal with frustration
# Then when a string is inserted, it will scan and if more than x amount of words are present,
# Try using OOP

negative_words = ["bad", "negative", "terrible", "horrible", "worse", "worst"]  # all trigger words
email_body = []  # Every word in email
matched_words = []  # Every word in email body and in negative word .append here

def scan_text(email):   #need to scan every word in self.emailbody
    email_text = email  # what ever is passed into parameter = email_text
    words = email_text.split()  # what ever is in email_text as parameter is split in a list as WORD
    email_body.extend(words)
    #print(email_body)

    for i in email_body:
        if i in negative_words:
            print(f"We have a match: {i} ")
            matched_words.append(i)
        else:
            pass

    print("all words in match: ")
    print(matched_words) #prints all words in match which is stored in a database.


scan_text("") #insert text to scan here

 #insert any text here. The system will analyze it.


# if any(x in negative_words for x in email_body):
#       print("Match")
# else:
#       print("No Match")

# Next Tasks:
