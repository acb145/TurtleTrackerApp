#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: John Fay (john.fay@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

# Copy and paste a line of data as the lineString variable value
lineString = "uid	tag_id	utc	lc	iq	lat1	lon1	lat2	lon2	nb_mes	big_nb_mes	best_level	pass_duration	nopc	calcul_freq	altitude"

# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()

# Assign variables to specfic items in the list
record_id = lineData[0]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[4]       # Observation Location Class
obs_lat = lineData[]     # Observation Latitude
obs_lon = lineData[]     # Observation Longitude

# Print information to the use
print (f"Record {recordID} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")