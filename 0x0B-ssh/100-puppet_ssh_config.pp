file { 'use the private key ~/.ssh/school':
  ensure  => file,
  path    => '/home/ubuntu/.ssh/config',
  owner   => 'ubuntu',
  content => "# SSH client configuration\n\n" .
    "IdentityFile ~/.ssh/school\n" .
    "PasswordAuthentication no\n",
}
