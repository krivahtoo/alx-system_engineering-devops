include stdlib
file_line { 'use the private key ~/.ssh/school':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}

file_line { 'refuse to authenticate using a password':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
