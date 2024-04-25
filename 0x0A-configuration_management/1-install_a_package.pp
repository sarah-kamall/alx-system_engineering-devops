# install package flask
# install flask
package { 'Flask':
  ensure   => '2.1.0',    # Ensures Flask version 2.1.0 is installed
  provider => 'pip3',     # Specifies pip3 as the provider
}