# custom http header

$content = "
server {
    error_page 404 /custom404.html;
    location = /custom404.html {
        root /usr/share/nginx/html;
        internal;
    }

	listen 80 default_server;
	listen [::]:80 default_server;

    add_header X-Served-By ${::hostname};

	root /var/www/html;
	index index.html index.htm index.nginx-debian.html;

	server_name _;

    location /redirect_me {
        rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    }

	location / {
		try_files $uri $uri/ =404;
	}
}
"

exec { 'apt-get update -y':
    command => 'apt-get update -y',
    path    => '/usr/bin:/usr/sbin',
}

package { 'nginx':
    ensure  => 'installed',
    require => Exec['apt-get update -y'],
}

file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => $content,
    require => Package['nginx'],
}

service { 'nginx':
    ensure  => 'running',
    require => File['/etc/nginx/sites-available/default']
}
