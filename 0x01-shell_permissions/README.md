0-iam_betty => changing user => su betty
1-who_am_i => getting the user => whoami
2-groups => getting user groups => groups
3-new_owner => changing owner => chown betty hello
4-empty => creating an empty file => touch hello
5-execute => changing owner to execute => chmod u+x hello
6-multiple_permissions => changing permissions => chmod 754 hello
7-everybody => changing permissions => chmod ugo+x hello
8-James_Bond => setting permissions => chmod 007 hello
9-John_Doe => setting permissions => chmod 753 hello
10-mirror_permissions => reference permissions => chmod --reference=olleh hello
11-directories_permissions => chmod sub directories => find . -type d -exec chmod 755 {} +
12-directory_permissions => create with permission => mkdir -m 751 my_dir
13-change_group => changing group for a file => chgrp school hello
100-change_owner_and_group => changing owner, group => chown -R vincent:staff *
101-symbolic_link_permissions => changing for symbolic => chown -R vincent:staff _hello
102-if_only => changing owner with condition => if[stat -c "%U" hello] then chown betty hello
