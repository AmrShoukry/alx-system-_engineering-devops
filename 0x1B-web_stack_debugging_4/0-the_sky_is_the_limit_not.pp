# increase time limit

exec {'fix--for-nginx':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path => '/bin'
}

exec { 'restart':
    command => 'service nginx restart',
    path => '/usr/sbin:/sbin:/usr/bin:/bin',
    subscribe => Exec['fix--for-nginx']
}
