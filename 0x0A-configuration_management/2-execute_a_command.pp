# An exec resource to kill the process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  subscribe   => File['./killmenow'],
}
