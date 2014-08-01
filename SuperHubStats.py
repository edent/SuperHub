from bs4 import BeautifulSoup
import urllib2
import csv
import datetime
import time

# This script reads statistics from a VirginMedia SuperHub2 / 2ac
# It will save into a .CSV file the following information
#   * Upstream power levels
#   * Downstream power levels
#   * Downstream SNR
# Requires http://www.crummy.com/software/BeautifulSoup/

# A timestamp
timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

# The default SuperHub IP address.
SuperHubIP = "http://192.168.0.1/"

# Fetch the HTML pages
upstream   = urllib2.urlopen(SuperHubIP + "cgi-bin/VmRouterStatusUpstreamCfgCgi")
downstream = urllib2.urlopen(SuperHubIP + "cgi-bin/VmRouterStatusDownstreamCfgCgi")

# Parse them
up_soup = BeautifulSoup(upstream.read())
down_soup = BeautifulSoup(downstream.read())

# A particularly lazy way to find the Upstream power levels
all_us_td = up_soup.find_all('td')

# Currently, Virgin Media only uses US-1 and US-4. This may change in the future.
us1_power = all_us_td[36].text
us4_power = all_us_td[39].text

# Again, lazy way to find Downstream levels
all_ds_td = down_soup.find_all('td')

# Currently, VM only uses 8 DS channels
ds1_power = all_ds_td[55].text
ds2_power = all_ds_td[56].text
ds3_power = all_ds_td[57].text
ds4_power = all_ds_td[58].text
ds5_power = all_ds_td[59].text
ds6_power = all_ds_td[60].text
ds7_power = all_ds_td[61].text
ds8_power = all_ds_td[62].text

ds1_rx = all_ds_td[64].text
ds2_rx = all_ds_td[65].text
ds3_rx = all_ds_td[66].text
ds4_rx = all_ds_td[67].text
ds5_rx = all_ds_td[68].text
ds6_rx = all_ds_td[69].text
ds7_rx = all_ds_td[70].text
ds8_rx = all_ds_td[71].text

# Append the details to the end of a .CSV file
with open('vm.csv', 'a') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([timestamp,us1_power,us4_power,ds1_power,ds2_power,ds3_power,ds4_power,ds5_power,ds6_power,ds7_power,ds8_power,ds1_rx,ds2_rx,ds3_rx,ds4_rx,ds5_rx,ds6_rx,ds7_rx,ds8_rx])

# All done. Bye-bye!
exit()