
# Internet Speed Test

This script uses the speedtest module to test the internet connection and write the results to a file. The script runs the test three times, and calculates the average download, upload, and ping values.

  

## Requirements

- Python 3.x

- The speedtest module (can be installed using pip install speedtest-cli)

  
  

## Usage

To run the script, simply run the main function:

    from speedtest_file import main    
    main()

This will run the internet speed test three times, and write the results to a file called file.txt. The file will contain the individual test results, followed by the average download, upload, and ping values.

## Output

The file.txt file will contain the following information:


    Test #1
    
    • Download: 10.00 Mb/s
    
    • Upload: 5.00 Mb/s
    
    • Ping: 10.00
    
      
    
    Test #2
    
    • Download: 20.00 Mb/s
    
    • Upload: 10.00 Mb/s
    
    • Ping: 15.00
    
      
    
    Test #3
    
    • Download: 30.00 Mb/s
    
    • Upload: 15.00 Mb/s
    
    • Ping: 20.00
    
      
    
    Average of three runs:
    
    • Download speed: 20.00 Mb/s
    
    • Upload speed: 10.00 Mb/s
    
    • Ping: 15.00

Each test result includes the test number, followed by the download, upload, and ping values. The final section of the file contains the average values for these metrics.