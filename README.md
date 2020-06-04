# Every Word Bot

**Step 1** — You need a VPS to host and run this script. I religiously recommed [DigitalOcean droplet](https://mighil.com/DO/). I think you'll get a 50USD or 100USD credit on DigitalOcean when you sign-up with the link I shared. You could check Amazon AWS or Google Cloud Platform also. Select Debian, Ubuntu, or CentOS while you're creating a droplet or instance.

**Step 2** — [Install Python 3](https://linuxize.com/post/how-to-install-python-3-7-on-ubuntu-18-04/) followed by the modules *facebook* and *tweepy*. Installing modules is fairly easy once you get the hang of it. (`pip3 install modulename`)

**Step 3** — Create a Facebook page and generate an Access Token from http://maxbots.ddns.net/token/. Paste the token to the accesstoken field in the script.

**Step 4** — Create a Twitter app and generate tokens & secret keys. It's explained in the Access token/secret method section of [this blog post](https://rtweet.info/articles/auth.html). 

**Step 5** — Download the [English words data-set](https://github.com/dwyl/english-words) of your choice.  Fire up the script with the command `sudo python3 main.py`

Also read:
https://github.com/aparrish/everywordbot
