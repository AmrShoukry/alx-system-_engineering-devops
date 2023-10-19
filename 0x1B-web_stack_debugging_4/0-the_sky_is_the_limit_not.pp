# increase time limit

# fix waiting time 
exec {'fix--for-nginx':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path => '/bin'
}

# restarting nginx
exec { 'restart':
    command => 'service nginx restart',
    path => '/usr/sbin:/sbin:/usr/bin:/bin',
    subscribe => Exec['fix--for-nginx']
}
