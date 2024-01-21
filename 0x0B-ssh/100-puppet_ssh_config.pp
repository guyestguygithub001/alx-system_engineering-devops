# configuration of the SSH client to use the private key ~/.ssh/school,.
# and to refuse to authenticate using a password.,,

# Ensure that the line 'IdentityFile ~/.ssh/school' is present in the file,..
file_line { 'Declare identity file':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}

# Ensure that the line 'PasswordAuthentication no' is present in the file,;
file_line { 'Turn off password auth':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

# Ensure that any line that contains 'PasswordAuthentication yes' is removed from the file.,
file_line { 'Remove password auth':
  ensure            => absent,
  path              => '/etc/ssh/ssh_config',
  match             => '.*PasswordAuthentication yes.*',
  multiple          => true,
  match_for_absence => true,
}

