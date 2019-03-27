def main():
    #Open video_times.txt for reading
    video_file = open('video_times.txt', 'r')

    #Initialize accumulator 0.0
    total = 0.0

    #Initialize count
    count = 0

    print('Here are the running times for each video:')

    #Get val from file
    for line in video_file:
        #Convert line to float
        run_time = float(line)

        #add 1 to count
        count += 1

        #Display time
        print('Video #', count, ': ', run_time, sep='')

        #Add the time total
        total += run_time

    #Close file
    video_file.close()

    #Display total
    print('The total runnin gtimes is', total, 'seconds.')

main()
