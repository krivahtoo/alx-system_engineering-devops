# An exec resource to kill the process named killmenow
exec { 'killmenow':
  command     => 'pkill -f killmenow',  # Kill killmenow process
  refreshonly => true,                   # Only run when notified
  subscribe   => File['/killmenow_script'],
}
