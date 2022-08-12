import random
import os
from ssl import _create_default_https_context
from typing import Counter, Text 
from termcolor import colored
class NumberSevenError(Exception):
    pass


#clearing screen to help maintaining a clean output
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
#to end the programm
def end_program(n):
    end_count = n.count("end")
    back_count = n.count("back")
    if end_count >= 1:
        print(colored("End Detected!",'red',attrs=['bold']))
        final_answer = input(colored("do you wish to end the programm?[yes/no]","red"))
        if final_answer.lower() == 'yes':
            exit(colored("exiting ...",'green'))     
        else:
            pass
    elif back_count >= 1:
        main()
    
    


class Error(Exception):
    pass

#used in capital function
class WrongWord(Error):
    pass


class final_exam:
    """this class is made to run 10 of exercise programmes as methods"""

    def draw_menu(self):
        """option menu from which the user will select"""
        menu = """\n¸,ø¤º°`°º¤ø,¸¸,ø¤º°┌─────────── •✧✧• ───────────┐¸,ø¤º°`°º¤ø,¸¸,ø¤º°
                              1-MIN/MAX
                              2-CAPITAL
                              3-COPYFILE
                             4-TICTACTOE
                             5-FACTORIAL
                             6-WATER BILL
                            7-LOWER_UPPER
                            8-WORD FINDER                                          
                          9-CONVERT TO ASCII           
                         10-ORD-CHR CONVERTOR  
                    └─────────── •✧✧• ───────────┘
"""
        print(colored(menu,'cyan'))

    def factorial(self):
        """A method to calculate a numbers factorial value"""

        def fact(n):
            """Calculates the factorial of entered parameter"""
            fact_start = 1
            answer = 1
            while fact_start <= n:
                answer *= fact_start
                fact_start += 1
            return answer
        def main():
            #in the case of entering characters instead of numbers
            try:
                fact_number = input("Please enter a number:\n")
                end_program(fact_number.lower())
                fact_number = int(fact_number)
                if fact_number == 7:
                    raise NumberSevenError
                else:
                    print("Factorial answer is {}".format(fact(fact_number)))
            except NumberSevenError:
                print(colored("""ValueError\nnumber 7 is not allowed instead we will show you factorial of number 3.""",'red'))
                print("Factorial answer is {}.".format(fact(3)))
            except ValueError:
                print(colored("Entery Not Valid!!",'red',attrs=['bold']))
                main()
        main()


    def min_max(self):
        """"Method to find maximum and minimum values in a pre-made list."""
        comparison_list = [10, "15", 25, 40, 41,
                           50, "dfdfdf", 31, 48, 70,
                           55, 21, 34, 1, 4,
                           5, 16, 87, "end", 99]
        backup_list = []
        for value in comparison_list:
            try:
                int(value)
            except ValueError:
                print(colored("""Data Coruption!
            Deleting corupted data ...""","red",attrs=['bold']))
                backup_list.append(value)
                comparison_list.remove(value)
        counter = 0
        while counter < len(comparison_list) - 1:
            if int(comparison_list[counter]) > 50:
                print(colored("value beyond 50 detected!!",'red',attrs=['bold']))
                print(colored("Detected number is {}".format(comparison_list[counter]),'green'))
            if int(comparison_list[counter]) < int(comparison_list[counter + 1]):
                maximum_value = int(comparison_list[counter + 1])
            elif int(comparison_list[counter]) > int(comparison_list[counter + 1]):
                minimum_value = int(comparison_list[counter + 1])
            counter += 1
        maximum_value = colored(maximum_value,'yellow')
        minimum_value = colored(minimum_value,'yellow')

        print("minimum value is : {}".format(minimum_value))
        print("Maximum value is : {}".format(maximum_value))

    def capital(self):
        '''capitalizes all characters in a string'''
        def splitter(string, split_character):
            index_counter = -1
            index_start = 0
            split_string = []
            index_splitter_chr = []
            for strings in string:
                new_string = ""
                index_counter += 1
                if strings == split_character or index_counter == len(string) - 1:
                    index_splitter_chr += [index_counter]
                    while index_start <= index_counter:
                        new_string += string[index_start]
                        index_start += 1
                    split_string += [new_string]
                    index_start = index_counter + 1

            return split_string

        def change_first_chr(x):
            new_string_list = []
            final_string_list = []
            final_string = ""
            for strings in x:
                new_string = ""
                if 96 < ord(strings[0]) < 123:
                    new_string = chr(ord(strings[0]) - 32) + strings[1:]
                    new_string_list += [new_string, ""]
                else:
                    new_string_list += [strings]
            final_string_list += new_string_list[:len(new_string_list)]
            for strings in final_string_list:
                final_string += strings
            return final_string

        try:
            string = input("please enter a sentence\n")
            lowered = string.lower()
            end_program(lowered)
            free_count = lowered.count("free")
            counter = 0
            output = change_first_chr(splitter(string, " "))
            print("new sentence is:")
            print(output)
            if free_count >= 1:
                raise WrongWord
        except WrongWord:
            while counter < free_count:
                print(colored('Wrong word "Free" was used!!','red',attrs=['bold']))
                counter += 1

    def copyfile(self):

        def help(error_code):
            """This is a function to help user enter the file destination correctly."""
            if error_code == 1:
                print(colored("""If you are getting Errors maybe its because you are not entering the destination correctly
            here is an correct example of file location ===>""",'blue'),colored(" C:\\Users\\Administrator\\Desktop\\NewTextDocument.txt",'red',attrs=['bold']))
            elif error_code == 2:
                print(colored("If you are sseing this it means that your destination is not showing a file!",'blue'))
        
        def main():
            file_destination = input("please enter destination of the file you want to copy:\n")
            end_program(file_destination.lower())
            try:
                file_contents = ''
                f = open(file_destination, 'rb')
                file_contents = f.read()
                f.close()
                copy_destination = input("Please enter the destination you want to copy the file:\n")
                end_program(file_destination.lower())
                f = open(copy_destination, "wb")
                f.write(file_contents)
                f.close()
            except FileNotFoundError:
                help(1)
                main()
            except PermissionError:
                help(2)
                main()

        main()

    def find_the_word(self):

        def word_finder(a="python language tutorials by freezeman.",word = "freezeman"):

            def lower_case(a):
                lower_cased_sentence = ""
                for i in a:
                    if 65 <= ord(i) <= 90:
                        lower_cased_sentence += chr(ord(i) + 32)
                    else:
                        lower_cased_sentence += i
                return lower_cased_sentence

            index_counter = 0
            word_counter = 0
            start_index = 0
            start_index_list = []
            length = int(len(a))
            while index_counter < length:
                check_string = ""
                if a[index_counter] in [word[0].lower(),word[0].upper()]:
                    start_index = index_counter
                    check_string += a[index_counter:index_counter + 9:]
                    if lower_case(check_string) == word:
                        word_counter += 1
                        start_index_list += [start_index]
                        index_counter += 9 - 1
                    else:
                        index_counter += 1
                else:
                    index_counter += 1
            if word_counter >= 1:
                print("There are {} {} inside your sentence".format(word_counter,word))
                print("{} starting indexes are:".format(word), start_index_list, ".")
            else:
                print("no {} were found in your sentence".format(word))

        print(colored("Welocme to word finder ;)",'cyan'))
        word = input(colored("please enter the word you want to count in your sentence.\n",'magenta'))
        entery = input(colored("Please enter a sentence to find the {} inside.\n",'magenta'.format(word)))
        end_program(entery.lower())
        if len(entery) >= 10:
                word_finder(entery)
        else:
            word_finder()

    def lower_upper(self):
        def lower_upper_inner(n):
            reshte_jadid = ""
            for i in n:
                if 65 <= ord(i) <= 90:
                    reshte_jadid += chr(ord(i) + 32)
                elif 97 <= ord(i) <= 122:
                    reshte_jadid += chr(ord(i) - 32)
                elif i == " ":
                    reshte_jadid += " "
                else:
                    reshte_jadid += i
            return reshte_jadid

        n = input("Please enter a string to convert its lower and upper case letters:\n")
        end_program(n.lower())
        print(lower_upper_inner(n))

    def Water_Bill(self):
        inhabitants = {1: 's', 2: 3, 3: 3, 4: 2, 5: 2, 6: 1,7: 4, 8: 3}
        inhabitance_number = 0
        pop_key_list = []
        replacement_dict = {}
        while True:
            try:
                water_bill = input("Please enter the water bill cost:\t")
                end_program(water_bill.lower())
                water_bill = int(water_bill)
                break
            except ValueError:
                print(colored("Entered value was not defined!",'red',attrs=['bold']))
                self.water_bill()
        for key in inhabitants:
            try:
                int(inhabitants[key])
                inhabitance_number += inhabitants[key]
            except ValueError:
                print(colored("A NONE INTEGER TYPE VALUE DETECTED!",'magenta'))
                while True:
                    try:
                        replacement_value = int(input("Please enter inhabitants of {} unit :\n".format(key)))
                        pop_key_list += [key]
                        end_program(str(replacement_value).lower())
                        inhabitance_number += replacement_value
                        replacement_dict[key] = replacement_value
                        break
                    except ValueError:
                        print(colored("Entered value was not defined!",'red',attrs=['bold']))
        for key in pop_key_list:
            inhabitants.pop(key)
        for key in replacement_dict:
            inhabitants[key] = replacement_dict[key]
        cost_per_person = water_bill / inhabitance_number
        for key in inhabitants:
            value = inhabitants[key] * cost_per_person
            print("{} units share of water bill is:{}".format(key, value))

    def convert_to_ascii(self):
        def convertor(n):
            converted_string = ""
            x = len(n)-1
            count = 0
            for i in n:
                if i == " ":
                    converted_string += " "
                else:
                    converted_string += str(ord(i))
                if count != x and i != " ":
                    converted_string += "_"
                elif i == " ":
                    converted_string += " "
                elif count == x:
                    converted_string += ""
                count += 1
            return converted_string

        n = input("Please enter a sentence to return ascii values:\n")
        end_program(n.lower())
        print(convertor(n))

    def ord_chr_convertor(self):

        def ord_chr_changer(string):
            def my_ord(a):
                chr_list = []
                for char in a:
                    if char != " ":
                        chr_list += [ord(char)]
                return chr_list

            def my_chr(a):
                ord_list = []
                for num in a:
                    if num < 256:
                        ord_list += [chr(num)]
                    else:
                        ord_list += ["NONE"]
                return ord_list

            string_data = ""
            int_data = []
            index_counter = 0
            while index_counter < len(string):
                if string[index_counter] in "123456789":
                    if string[index_counter + 1] in "123456789":
                        if string[index_counter + 2] in "123456789":
                            int_data += [int(string[index_counter:index_counter + 3])]
                            index_counter += 3
                            continue
                        else:
                            int_data += [int(string[index_counter:index_counter + 2])]
                            index_counter += 2
                            continue
                    else:
                        int_data += [int(string[index_counter])]
                        index_counter += 2
                else:
                    string_data += string[index_counter]
                    index_counter += 1
            print(my_ord(string_data))
            print(my_chr(int_data))

        entery = input("Please enter a combined string of numbers and characters:\n")
        end_program(entery.lower())
        ord_chr_changer(entery)
    def tictactoe(self):
        class TicTacToe:
            def __init__(self):
                self.grid = {1:" 1",2:" 2",3:" 3",4:" 4",5:" 5",6:" 6",7:" 7",8:" 8",9:" 9"}
                self.win_condition = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
                self.valid_moves = [1,2,3,4,5,6,7,8,9]
                self.count = 0
            
            def play_mode(self):
                self.mode = ''
                while True:
                    n = input(colored("""
       ✘〇✘〇✘〇    ╔═══Please select a Play Mode═══╗     〇✘〇✘〇✘
                    ║⥺ ❶ Single                     ║
                    ║⥺ ❷ Multi                      ║
                    ╚═══════════════════════════════╝\n""",'cyan'))
                    x = n.lower()
                    end_program(x)
                    single_count = x.count('single')
                    multi_count = x.count('multi')
                    if n == '1' or single_count > 0:
                        self.mode = "SinglePlayer"
                        break
                    elif n == '2' or multi_count > 0:
                        self.mode = "MultiPlayer"
                        break
                    else:
                        print(colored("Play Mode Unsopported!",'red',attrs=['bold']))
                        continue
                clear_screen()
                


            def draw_grid(self):

                print(self.grid[1]," |",self.grid[2]," |",self.grid[3])
                print("───","┼","───","┼","───")
                print(self.grid[4]," |",self.grid[5]," |",self.grid[6])
                print("───","┼","───","┼","───")
                print(self.grid[7]," |",self.grid[8]," |",self.grid[9])

            def player_one(self):
                print("Player One (✘)")
                try:
                    while True:
                        self.draw_grid()
                        i = input("Please enter a block number from 1 to 9 :\n")
                        end_program(i.lower())
                        i = int(i)
                        if i not in self.valid_moves:
                            print(colored("The Block you have choosen is occupied!\nEnter Again!",'red',attrs=['bold']))
                            continue
                        else:
                            self.valid_moves.remove(i)
                            self.grid[i] = colored(" ✘",'red')
                            self.count += 1
                            self.win_check()
                            break
                except ValueError:
                    print(colored("Entery not valid!",'red',attrs=['bold']))
                    self.player_one()

            def player_two(self):
                print("Player two (〇)")
                try:
                    while True:
                        self.draw_grid()
                        i = input("Please enter a block number from 1 to 9 :\n")
                        end_program(i.lower())
                        i = int(i)
                        if i not in self.valid_moves:
                            print(colored("The Block you have choosen is occupied!\nEnter Again!",'red',attrs=['bold']))
                            continue
                        else:
                            self.valid_moves.remove(i)
                            self.grid[i] = colored("〇",'blue')
                            self.count += 1
                            self.win_check()
                            break
                except ValueError:
                    print(colored("Entery not valid!",'red',attrs=['bold']))
                    self.player_two()

            def replay(self):
                while True:
                    play_again = input("Do you want to play again?[Y/N]")
                    end_program(play_again.lower())
                    if play_again.lower() == 'y':
                        self.valid_moves = [1,2,3,4,5,6,7,8,9]
                        self.grid = {1:"  ",2:"  ",3:"  ",4:"  ",5:"  ",6:"  ",7:"  ",8:"  ",9:"  "}
                        self.count = 0
                        self.run()
                    elif play_again.lower() == 'n':
                        print(colored("Bye Bye!",'green',attrs=['bold']))
                        main()
                    else:
                        print("Unknown answer!")


            def AI_player(self):
                valid_moves = self.valid_moves
                i = random.sample(valid_moves,1)
                self.grid[i[0]] = colored("〇",'blue')
                valid_moves.remove(i[0])
                self.count += 1
                self.win_check()
                print("AI Player has choosen {} Block.".format(i))

            def win_check(self):
                counter = 0
                for i in self.win_condition:
                    if self.grid[i[0]] == self.grid[i[1]] == self.grid[i[2]] == colored(" ✘",'red'):
                        print(colored("Player one wins!!",'magenta'))
                        self.replay()
                    if self.grid[i[0]] == self.grid[i[1]] == self.grid[i[2]] == colored("〇",'blue') and self.mode == "SinglePlayer":
                        print(colored("AI wins!!",'cyan'))
                        self.replay()
                    elif self.grid[i[0]] == self.grid[i[1]] == self.grid[i[2]] == colored("〇",'blue') and self.mode == "MultiPlayer":
                        print(colored("Player two wins!!",'green'))
                        self.replay()
                    elif self.count == 9 and counter >= 7:
                        print(colored("DRAW!!!",'yellow'))
                        self.replay()
                    counter += 1

            def run(self):
                self.play_mode()
                if self.mode == "SinglePlayer":
                    self.single_play()
                else:
                    self.multi_player()

            def single_play(self):
                while True:
                    self.player_one()
                    clear_screen()
                    self.AI_player()

            def multi_player(self):
                while True:
                    self.player_one()
                    clear_screen()
                    self.player_two()
                    clear_screen()
        a = TicTacToe()
        a.run()
def main():
    app = final_exam()
    print(colored("WELCOME TO MY PROGRAM!\n",'green'),colored("TYPE IN ANY COMBINATION OF",'blue') ,colored('"END"','red',attrs=['bold']), colored("TO END THE PROGRAM!",'blue') )
    print(colored(" TYPE IN",'blue'),colored('"BACK"','magenta'),colored("TO RETURN TO MENU.",'blue'))
    while True:
        app.draw_menu()
        i = input("Please select a program by number.\n")
        end_program(i.lower())
        if i == '5':
            clear_screen()
            print(colored("This program caculates a number\'s factorial value.",'magenta'))
            app.factorial()
        elif i == '1':
            clear_screen()
            print(colored("This program finds minimum and maximum values in a pre-made list.",'magenta'))
            app.min_max()
        elif i == '2':
            clear_screen()
            print(colored("This program changes first letter of every word to uppercase.",'magenta'))
            app.capital()
        elif i == '3':
            clear_screen()
            print(colored("This program copies a file to a preferred destination",'magenta'))
            app.copyfile()
        elif i == '4':
            clear_screen()
            print(colored("""This program is TicTacToe game with two playmodes
            select one of the options to play!""",'magenta'))
            app.tictactoe()
        elif i == '8':
            clear_screen()
            app.find_the_word()
        elif i == '7':
            clear_screen()
            print(colored("This program converts lowercase letters to uppercase and uppercase to lowercase.",'magenta'))
            app.lower_upper()
        elif i == '6':
            clear_screen()
            print(colored("This programm caculates every units share of water bill.",'magenta'))
            app.Water_Bill()
        elif i == '9':
            clear_screen()
            print(colored("This program turns every letter into ASCII number and shows them in this format(97_89_90_ 50_10_20.)",'magenta'))
            app.convert_to_ascii()
        elif i == '10':
            clear_screen()
            print(colored("This program turnes numbers up to three digits into letters and letters into ASCII numbers.",'magenta'))
            app.ord_chr_convertor()
        else:
            clear_screen()
            print(colored("NOT A VALID NUMBER!!",'blue'))
            continue
main()