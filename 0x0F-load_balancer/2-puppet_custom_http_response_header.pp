# custom http header
file_line { 'new_header'
    path  => '/etc/nginx/sites-available/default',
    line  => 'add_header X-Served-By $HOSTNAME';
    after => '    listen [::]:80 default_server;'
}
