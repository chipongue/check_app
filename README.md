# check_app
Programs or applications are executable files that are responsible for performing predefined tasks. On the Linux platforms these files exist the hundreds, and can vary from each new update or installation, and are distributed across multiple directors, making your control untrivial.

These files are responsible for executing any task that is scheduled, controlling them is crucial to ensuring that the computer works within the expected pattern.

This Nagios plugin monitors the main principals where the executable files are stored, you can optionally be the user to define the principals that you want to monitor in accordance with your system's interests and configuration, by ticking the critical state whenever the new application is installed on the monitored board, the main objective is to have a control of the files that you install. It stores the list of programs in a file, which in case of the program has been legitimately installed, the administrator only needs to erase it.

Mandatory arguments: The following argument must be specified when the module is executed:
-p or – path used to specify the board or full path of the board to be monitored.

Optional arguments: The following arguments are optionally invoked, as user needs:
-V or – version used to query the module version.
-A or – author used to query the author's data.

Command-Line Execution example

./check_app.py -p /usr/bin/,/sbin/,/usr/sbin/,/bin/,/usr/local/bin/

