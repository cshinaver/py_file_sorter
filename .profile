#For updating from synced dropbox profile
alias updateProfile="cat ~/.profile.backup > .profile; cat ~/Dropbox/Preferences/.profile >> ~/.profile; source ~/.profile"

# Set architecture flags
export ARCHFLAGS="-arch x86_64"
# Ensure user-installed binaries take precedence
export PATH=/usr/local/bin:$PATH
# Load .bashrc if it exists
test -f ~/.profile && source ~/.profile
export PATH=/usr/local/bin:$PATH
