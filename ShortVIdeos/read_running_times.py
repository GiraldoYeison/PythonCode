""" 
Name: Yeison Giraldo
Date: 1/25/24
Program: 
Description:

 
""" 
# this program the values in the video_times.txt
#file and calculates their total.

def main():
        
    #open the video_times.txt file for reading
    video_file = open('video_times.txt', 'r')
    
    #Initialize an accumulator to 0.0
    total = 0.0
    
    #Initialize a variable to keep count of the videos
    count = 0
    
    print('Here are the running times for each video: ')
    
    #Get the values from the file and total them.
    for line in video_file:
        #convert a line to a float
        run_time = float(line)
        
        #add 1 to the count variable.
        count +=1
        
        #Display the time.
        print('Video #', count, ': ', run_time, sep='')
        
        #add the time to total.
        total += run_time
        
    #close the file
    video_file.close()
    
    #Display the total of the running times.
    print(f'The total running times is {total} seconds. ')
    
#call the main function
if __name__ == '__main__':
    main()
