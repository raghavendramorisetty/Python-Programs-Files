# Program for accepting line of text and display words with letters by using threads
# FunWordsDisplayEx1.py
import threading, time


def worddisp(line):
    if (len(line) == 0):
        print("No String data-Nothing to display")
    else:
        print("------------------------------------------------")
        print("Given line of text:", line)
        words = line.split()
        print("------------------------------------------------")
        for word in words:
            print("\t{}".format(word))
            for ch in word:
                print("\t\t{}".format(ch))
                time.sleep(0.5)
            time.sleep(1)
        print("------------------------------------------------")


# Main Program
t1 = threading.Thread(target=worddisp, args=(input("Enter Line of Text:"),))
t1.start()
