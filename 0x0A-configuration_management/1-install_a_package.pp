# install package flask
package { 'flask':
  ensure   => '2.1.0',  # Ensures that Flask is installed and the latest version is used
  provider => 'pip3',    # Specifies pip3 as the provider
}
