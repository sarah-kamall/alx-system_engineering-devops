# Define a file resource
file { '/tmp/school':
  ensure  => present,   # Ensure the file exists
  content => 'I love Puppet',   # Content of the file
  mode    => '0744',    # Permissions for the file
  owner   => 'www-data',    # Owner of the file
  group   => 'www-data',    # Group of the file
}
