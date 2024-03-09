# Install the Apache module (if not already installed)
class { 'apache': }

# Define your virtual host configuration
apache::vhost { 'mywebsite':
  port    => '80',
  docroot => '/var/www/html',  # Adjust as needed
  servername => 'mywebsite.com',  # Replace with your domain
}

# Ensure Apache is running
service { 'apache2':
  ensure => 'running',
  enable => true,
}

