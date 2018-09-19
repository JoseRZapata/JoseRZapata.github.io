#!/usr/bin/env bash

# This script allows you to easily and quickly generate and deploy your website
# using Hugo to your personal GitHub Pages repository. This script requires a
# certain configuration, run the `setup.sh` script to configure this. See
# https://hjdskes.github.io/blog/deploying-hugo-on-personal-github-pages/index.html
# for more information.

# File copied from https://proquestionasker.github.io/blog/Making_Site/ tutorial
# on creating websites with blogdown, Hugo, and GitHub.

# Set the English locale for the `date` command.

# GitHub username.
USERNAME=JoseRZapata
# Name of the branch containing the Hugo source files.
SOURCE=source
# The commit message.

msg() {
    printf "\033[1;32m :: %s\n\033[0m" "$1"
}

msg "Pulling down the \`master\` branch into \`public\` to help avoid merge conflicts"
git subtree pull --prefix=public \
    https://github.com/$USERNAME/$USERNAME.github.io.git origin master -m "Merge origin master"

msg "Building the website"
hugo

msg "Pushing the updated \`public\` folder to the \`$SOURCE\` branch"
git add public
git commit -m "$MESSAGE"
git push origin "$SOURCE"

msg "Pushing the updated \`public\` folder to the \`master\` branch"
git subtree push --prefix=public \
    https://github.com/$USERNAME/$USERNAME.github.io.git master
