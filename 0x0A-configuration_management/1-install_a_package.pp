# Install a package
node default {
    package {'python3-flask':
        ensure => 'installed',
    }
}
