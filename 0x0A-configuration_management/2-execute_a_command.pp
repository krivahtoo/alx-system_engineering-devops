# An exec resource to kill the process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',
}
