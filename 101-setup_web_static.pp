# puppet to config the server
exec { 'update server':
  command => 'sudo apt -y update',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  unless  => 'dpkg -l | grep -q nginx',
}

exec { 'upgrade server':
  command => 'sudo apt -y upgrade',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  unless  => 'dpkg -l | grep -q nginx',
}

package { 'nginx':
  ensure => installed,
}

file { '/data/web_static/releases/test/':
  ensure => 'directory',
}

file { '/data/web_static/shared/':
  ensure => 'directory',
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
',
}

file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
}

exec { 'change owner':
  command => 'sudo chown -R ubuntu:ubuntu /data/',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}

file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => '
    location /hbnb_static {
        alias /data/web_static/current/;
        # made by omar Id hmaid
    }',
}

exec { 'nginx':
  command => 'sudo service nginx restart',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}
