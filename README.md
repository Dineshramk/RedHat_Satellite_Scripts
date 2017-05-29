# RedHat_Satellite_Scripts
Scripts for RedHat Satellite API

You can use these scripts to control your RedHat Satellite 5.7 through command line.

1. add_systems_in_ssm.py - This is used to create a new System Group in Satellite and add a list of systems to it
2. clear_failed_actions.py - This is used to archive and delete the failed actions under Schedule Tab in Satellite, which doesn't have any In-Progress Systems.
3. get_system_channels.py - This is used to get the Base Channel and all the Child Channels of a list of Systems.
4. get_system_details.py - This is used to get all the details of the system provided.
5. get_system_groups.py - This is used to get the System Groups, where the server is part of
