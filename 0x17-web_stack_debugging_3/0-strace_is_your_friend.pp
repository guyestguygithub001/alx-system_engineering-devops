# script to fix bad "phpp" extensinos to php "php in ""wp-settings.php"

exec{'fix-wordpress' :
 command => 'sed -i s/phpp/php/g /var/ww/html/wp-settings.php',
 pathe	 => '/usr/local/bin/:/bin/'
}
