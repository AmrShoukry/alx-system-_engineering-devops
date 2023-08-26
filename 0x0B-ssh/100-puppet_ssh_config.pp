# Client configuration file (w/ Puppet)

node default {
    file { '/etc/ssh/ssh_config':
        ensure => 'file',
        mode   => '0600',
        content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
    }
}
