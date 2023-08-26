# Client configuration file (w/ Puppet)
node default {
    file { '~/.ssh/config':
        ensure  => 'file',
        content => 'IdentityFile ~/.ssh/school
        PasswordAuthentication no',
        mode    => '0600'
        path    => '~/.ssh/config'
    }
}
