# this script increases the amount of traffic on NGINX server can handle
# the script also Increases the ULIMIT of the default file

# Increase the ULIMIT val
file { 'fix-for-nginx':
  ensure  => 'file',
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
}

# Reload Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
