0-current-working_directory => used for printing the current path => pwd
1-listit => used for printing the content of the file => ls
2-bring_me_home => used for navigating to the home root => cd /root
3-listfiles => used for listing files in a long format => ls -l
4-listmorefiles => Listing hidden & non-hidden files with long format => ls -al
5-listfilesdigitonly => displaying user, group IDs as digits along => ls -aln
6-firstdirectory => making directory in tmp => mkdir /tmp/my_first_directory
7-movethatfile => specific location => mv /tmp/betty /tmp/my_first_directory
8-firstdelete => delete a specific file => rm /tmp/my_first_directory/betty
9-firstdirdeletion => delete a specific dir => rm -r /tmp/my_first_directory
10-back => go back to previous step => cd -
11-lists => list different folders => ls . .. /boot -al
12-file_type => get the file type => file /tmp/iamafile
13-symbolic_link => creating a shortcut => ln -s /bin/ls __ls_
14-copy_html => copying html files to its parent => cp *.html ..
100-lets_move => moving all files beginning with uppercase => mv [[:upper:]] /tmp/u_
101-clean_emacs => deleting files ending with ~ => rm *~
102-tree => creating nested folders => mkdir -p welcome/to/school
