print("Please think of a number between 0 and 100!");
num = 100;
inp='h';
highlimit=100;
lowlimit=0;
while (inp not in ['c','C'] ):
        print("Is your secret number " + str(int((highlimit+lowlimit)/2)) +"?");
        inp = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.");
        
        if inp in ['l','L']: 
                          num += int((highlimit+lowlimit)/2)                         
                          lowlimit=int((highlimit+lowlimit)/2); 
                        
                        
        else:
            if inp in ['h','H']:
                              
                              num+= int((highlimit+lowlimit)/2)
                              highlimit=int((highlimit+lowlimit)/2);
                            
            else:
                if inp in ['c','C']:
                        print("Game over. Your secret number was " + str(int((highlimit+lowlimit)/2)))
                        quit
                        
                else:
                    print('Sorry, I did not understand your input.')
                    
                
