# Details about the helper scripts in this folder:
### The scripts in the folder `helper_scripts` are helpful based on the
### load balancer project with `HAProxy`.
### This `AirBnB deploy static` project is a continuation of our:
+  0x0C. Web server
+  0x0F. Load balancer
+  0x10. HTTPS SSL
### projects.
### You dont have to install a new nginx server since it has already been
### installed and configured following the above projects.
###
### NOTE:If you should run the script `0-setup_web_static.sh` in the root
### repo of this project `AirBnB_clone_v2` You will end up destroying your
### configuration which is the reason i came up with these  helper scripts
### that will set ur nginx based on the requirements.
###
### The `0-setup_web_static.sh` in the folder `helper_scripts` will install
### and configure your server according to task requirements if not already
### installed.
### This will only configure the nginx according to requirements without
### any fresh installation if already installed.
### 
### NOTE:User should modify the line 20 of `0-setup_web_static.sh` in this
### folder `sed` command line based on the users existing configuration of
### `/etc/nginx/sites-enabled/default` file.
###
### For full unistallation of nginx, user can run the `unistall script`
###
### Readup the brief documentation in the scripts
 
