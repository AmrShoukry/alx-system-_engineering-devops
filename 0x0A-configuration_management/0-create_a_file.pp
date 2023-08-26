# Creating a file
node default {
    file {'/tmp/school':
        ensure  => file,
        content => 'I love Puppet',
        owner   => 'www-data',
        group   => 'www-data',
        mode    => '0744',
        path    => '/tmp/school',
    }
}