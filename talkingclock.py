class Solution:    
    def ClockTalker(self, input_time):
            #type input_time: string
            #return type: string
            
            #TODO: Write code below to return a string with the solution to the prompt.
            hour = int(timeOfDay[0] + timeOfDay[1])
            timeOfDay = input_time 
            amPm = ""
            answer = "It's "
            if hour >= 12: 
                 amPm = "pm"
            else:
                 amPm = "am"

            if int(timeOfDay[1]) == 1: 
                 answer += "one "
            elif int(timeOfDay[1]) == 2:
                 answer += "two "
            elif int(timeOfDay[1]) == 3:
                 answer += "three "
            elif int(timeOfDay[1]) == 4:
                 answer += "four "            
            elif int(timeOfDay[1]) == 5:
                 answer += "five "
            elif int(timeOfDay[1]) == 6:
                 answer += "six "  
            elif int(timeOfDay[1]) == 7:
                 answer += "seven "
            elif int(timeOfDay[1]) == 8:
                 answer += "eight "
            elif int(timeOfDay[1]) == 9:
                 answer += "nine "
            elif int(timeOfDay[0] + timeOfDay[1]) == 10: 
                 answer += "ten "
            elif int(timeOfDay[0] + timeOfDay[1]) == 11: 
                 answer += "eleven "
            elif int(timeOfDay[0] + timeOfDay[1]) == 12: 
                 answer += "twelve "
            minute = int(timeOfDay[2] + timeOfDay[3])

            if int(timeOfDay[2]) == 0: 
                 answer += "oh "
            elif int(timeOfDay[2] + timeOfDay[3]) == 10:
                 answer += "ten "
            elif int(timeOfDay[2] + timeOfDay[3]) == 11:
                 answer += "eleven "
            elif int(timeOfDay[2] + timeOfDay[3]) == 12:
                 answer += "twelve "
            elif int(timeOfDay[2] + timeOfDay[3]) == 13:
                 answer += "thirteen "
            elif int(timeOfDay[2] + timeOfDay[3]) == 14:
                 answer += "fourteen "
            elif int(timeOfDay[2] + timeOfDay[3]) == 15:
                 answer += "fifteen "
            elif int(timeOfDay[2] + timeOfDay[3]) == 16:
                 answer += "sixteen "
            elif int(timeOfDay[2] + timeOfDay[3]) == 17:
                 answer += "seventeen "
            elif int(timeOfDay[2] + timeOfDay[3]) == 18:
                 answer += "eighteen "
            elif int(timeOfDay[2] + timeOfDay[3]) == 19:
                 answer += "nineteen "

            if int(timeOfDay[2]) == 2 or int(timeOfDay[2] == 2 and timeOfDay[3] == 0): 
                 answer += "twenty "
            elif int(timeOfDay[2]) == 3 or int(timeOfDay[2] == 3 and timeOfDay[3] == 0): 
                 answer += "thirty "           
            elif int(timeOfDay[2]) == 4 or int(timeOfDay[2] == 4 and timeOfDay[3] == 0): 
                 answer += "fourty "
            elif int(timeOfDay[2]) == 5 or int(timeOfDay[2] == 5 and timeOfDay[3] == 0): 
                 answer += "fifty "
            elif int(timeOfDay[2]) == 6 or int(timeOfDay[2] == 6 and timeOfDay[3] == 0): 
                 answer += "sixty "
            elif int(timeOfDay[2]) == 7 or int(timeOfDay[2] == 7 and timeOfDay[3] == 0): 
                 answer += "seventy "
            elif int(timeOfDay[2]) == 8 or int(timeOfDay[2] == 8 and timeOfDay[3] == 0): 
                 answer += "eighty "
            elif int(timeOfDay[2]) == 9 or int(timeOfDay[2] == 9 and timeOfDay[3] == 0): 
                 answer += "ninty "

            if int(timeOfDay[3]) == 1: 
                 answer += "one "
            elif int(timeOfDay[3]) == 2:
                 answer += "two "
            elif int(timeOfDay[3]) == 3:
                 answer += "three "
            elif int(timeOfDay[3]) == 4:
                 answer += "four "            
            elif int(timeOfDay[3]) == 5:
                 answer += "five "
            elif int(timeOfDay[3]) == 6:
                 answer += "six "  
            elif int(timeOfDay[3]) == 7:
                 answer += "seven "
            elif int(timeOfDay[3]) == 8:
                 answer += "eight "
            elif int(timeOfDay[3]) == 9:
                 answer += "nine "


            answer += amPm

            print(answer)
            return answer 


            pass

def main():
     str1=input()
     tc1= Solution()
     ans=tc1.ClockTalker(str1)
     print(ans)
    
if __name__ == '__main__': 
    main()