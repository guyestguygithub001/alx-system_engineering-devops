# A puppet script that replaces an error in a file on a server,
# Assigned to fix a bad `phpp` extensions to `php` in WordPress file `wp-settings.php`,

exec { 'fix-wordpress':
  command => "/bin/sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin:/usr/bin:/bin',
}
