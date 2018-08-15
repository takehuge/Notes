from shelljob import job

jm = job.FileMonitor()
jm.run([
    ['ls', '-alR', '/usr/local'],
    'my_prog',
    'build output input',
])
