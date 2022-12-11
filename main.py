import speedtest

def test():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def main():
    download_speeds = []
    upload_speeds = []
    ping_values = []
    
    with open('file.txt', 'w') as f:
        for i in range(3):
            # Print a progress message
            print('Making test #{}'.format(i+1))
            
            # Run the internet speed test and get the download, upload, and ping values
            d, u, p = test()
            
            # Add the values to the corresponding lists
            download_speeds.append(d)
            upload_speeds.append(u)
            ping_values.append(p)
            
            # Write the results to the file
            f.write('Test #{}\n'.format(i+1))
            f.write('\u2022 Download: {:.2f} Mb/s\n'.format(d / 1048576))
            f.write('\u2022 Upload: {:.2f} Mb/s\n'.format(u / 1048576))
            f.write('\u2022 Ping: {}\n\n'.format(p))

            
        # Writes the average download, upload, and ping values to the file
        download_avg = sum(download_speeds) / len(download_speeds)
        upload_avg = sum(upload_speeds) / len(upload_speeds)
        ping_avg = sum(ping_values) / len(ping_values)
        
        # Print the average values
        f.write("Average of three runs:\n")
        f.write("\u2022 Download speed: {:.2f} Mb/s\n".format(download_avg / 1048576))
        f.write("\u2022 Upload speed: {:.2f} Mb/s\n".format(upload_avg / 1048576))
        f.write("\u2022 Ping: {:.2f}".format(ping_avg))



main()