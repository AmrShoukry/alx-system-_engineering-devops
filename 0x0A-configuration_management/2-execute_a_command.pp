# Kill a process
node default {
    exec {'kill_process':
        command => 'pkill -TERM killmenow',
        path    => ['/usr/bin', '/bin'],
    }
}
