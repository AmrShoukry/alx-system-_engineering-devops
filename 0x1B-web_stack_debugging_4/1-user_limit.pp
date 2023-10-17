# increase time limit for user

exec {'change-os-configuration-for-holberton-user':
    command => 'sed -i "s/4/4096/" /etc/security/limits.conf',
    path => '/bin'
}

exec {'change-os-configuration-for-holberton-user2':
    command => 'sed -i "s/5/4096/" /etc/security/limits.conf',
    path => '/bin',
    subscribe => Exec['change-os-configuration-for-holberton-user']
}
