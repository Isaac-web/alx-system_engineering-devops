#kill a process
exec {'killmenow':
  command => 'pkill -f killmenow'
}
