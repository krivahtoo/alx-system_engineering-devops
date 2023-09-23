# create the file in /tmp/school
file { '/tmp/school':
  ensure  => file,          # Ensure it's a file
  mode    => '0744',       # Set permissions to 0744
  owner   => 'www-data',   # Set owner to www-data
  group   => 'www-data',   # Set group to www-data
  content => 'I love Puppet',  # Content of the file
}
