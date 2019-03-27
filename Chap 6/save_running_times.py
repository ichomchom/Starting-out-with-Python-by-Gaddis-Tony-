def main():
    #Get num of vids in the proj
    num_vids = int(input('How many videos are in the project? '))

    #Open the file to hold the running times.
    video_file = open('video_times.txt', 'w')

    #Get each vid's running time and write to file
    print('Enter the running times for each video.')
    for count in range(1, num_vids + 1):
        run_time = float(input('Video #' + str(count) + ': '))
        video_file.write(str(run_time) + '\n')

    #Close file
    video_file.close()
    print('The times have been saved to video_times.txt.')

main()
