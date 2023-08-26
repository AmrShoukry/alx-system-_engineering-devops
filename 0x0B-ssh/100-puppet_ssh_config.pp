# Client configuration file (w/ Puppet)

include stdlib

node default {
    file_line { 'Identity':
        ensure  => 'present',
        line    => 'IdentityFile ~/.ssh/school',
        path    => '~/.ssh/config'
    }

    file_line { 'password_off':
        ensure  => 'present',
        line    => 'PasswordAuthentication no',
        path    => '~/.ssh/config'
    }

}
