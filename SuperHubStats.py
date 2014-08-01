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

# Find the Upstream power levels
'''
<tr>
	<td class="title">Power Level (dBmV)</td>
	<td>41.00</td>
	<td>N/A</td>
	<td>N/A</td>
	<td>45.00</td>
</tr>
'''
us_power_label = up_soup.find(text="Power Level (dBmV)")
us_power_table = us_power_label.parent.parent
us_power = us_power_table.findAll('td')

# Currently, Virgin Media only uses US-1 and US-4. This may change in the future.
us1_power = us_power[1].text
us4_power = us_power[4].text

# Find Downstream levels
ds_power_label = down_soup.find(text="Power Level (dBmV)")
ds_power_table = ds_power_label.parent.parent
ds_power = ds_power_table.findAll('td')

# Currently, VM only uses 8 DS channels
ds1_power = ds_power[1].text
ds2_power = ds_power[2].text
ds3_power = ds_power[3].text
ds4_power = ds_power[4].text
ds5_power = ds_power[5].text
ds6_power = ds_power[6].text
ds7_power = ds_power[7].text
ds8_power = ds_power[8].text

ds_rx_label = down_soup.find(text="RxMER (dB)")
ds_rx_table = ds_rx_label.parent.parent
ds_rx = ds_rx_table.findAll('td')

ds1_rx = ds_rx[1].text
ds2_rx = ds_rx[2].text
ds3_rx = ds_rx[3].text
ds4_rx = ds_rx[4].text
ds5_rx = ds_rx[5].text
ds6_rx = ds_rx[6].text
ds7_rx = ds_rx[7].text
ds8_rx = ds_rx[8].text

# Append the details to the end of a .CSV file
with open('vm.csv', 'a') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([timestamp,us1_power,us4_power,ds1_power,ds2_power,ds3_power,ds4_power,ds5_power,ds6_power,ds7_power,ds8_power,ds1_rx,ds2_rx,ds3_rx,ds4_rx,ds5_rx,ds6_rx,ds7_rx,ds8_rx])

# All done. Bye-bye!
exit()