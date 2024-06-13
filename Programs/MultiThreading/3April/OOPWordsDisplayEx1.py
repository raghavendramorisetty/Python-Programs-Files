# Program for accepting line of text and display words with letters by using threads
# OOPWordsDisplayEx1.py
import threading, time


class WordDisp:
    def __init__(self, line):
        self.line = line

    def worddisp(self):
        if (len(self.line) == 0):
            print("No String data-Nothing to display")
        else:
            print("------------------------------------------------")
            print("Given line of text:", self.line)
            words = self.line.split()
            print("------------------------------------------------")
            for word in words:
                print("\t{}".format(word))
                for ch in word:
                    print("\t\t{}".format(ch))
                    time.sleep(0.5)
                time.sleep(1)
            print("------------------------------------------------")


# Main Program
t1 = threading.Thread(target=WordDisp(input("Enter Line of Text:")).worddisp)
t1.start()