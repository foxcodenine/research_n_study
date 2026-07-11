# ~/.bashrc: executed by bash(1) for non-login shells.
# see /usr/share/doc/bash/examples/startup-files (in the package bash-doc)
# for examples

# If not running interactively, don't do anything
case $- in
    *i*) ;;
      *) return;;
esac

# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# for setting history length see HISTSIZE and HISTFILESIZE in bash(1)
HISTSIZE=1000
HISTFILESIZE=2000

# check the window size after each command and, if necessary,
# update the values of LINES and COLUMNS.
shopt -s checkwinsize

# If set, the pattern "**" used in a pathname expansion context will
# match all files and zero or more directories and subdirectories.
#shopt -s globstar

# make less more friendly for non-text input files, see lesspipe(1)
[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

# set variable identifying the chroot you work in (used in the prompt below)
if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
    debian_chroot=$(cat /etc/debian_chroot)
fi

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac

# uncomment for a colored prompt, if the terminal has the capability; turned
# off by default to not distract the user: the focus in a terminal window
# should be on the output of commands, not on the prompt
#force_color_prompt=yes

if [ -n "$force_color_prompt" ]; then
    if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
	# We have color support; assume it's compliant with Ecma-48
	# (ISO/IEC-6429). (Lack of such support is extremely rare, and such
	# a case would tend to support setf rather than setaf.)
	color_prompt=yes
    else
	color_prompt=
    fi
fi

if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac

# enable color support of ls and also add handy aliases
if [ -x /usr/bin/dircolors ]; then
    test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'

    alias grep='grep --color=auto'
    alias fgrep='fgrep --color=auto'
    alias egrep='egrep --color=auto'
fi

# colored GCC warnings and errors
#export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# Add an "alert" alias for long running commands.  Use like so:
#   sleep 10; alert
alias alert='notify-send --urgency=low -i "$([ $? = 0 ] && echo terminal || echo error)" "$(history|tail -n1|sed -e '\''s/^\s*[0-9]\+\s*//;s/[;&|]\s*alert$//'\'')"'

# Alias definitions.
# You may want to put all your additions into a separate file like
# ~/.bash_aliases, instead of adding them here directly.
# See /usr/share/doc/bash-doc/examples in the bash-doc package.

if [ -f ~/.bash_aliases ]; then
    . ~/.bash_aliases
fi

# enable programmable completion features (you don't need to enable
# this, if it's already enabled in /etc/bash.bashrc and /etc/profile
# sources /etc/bash.bashrc).
if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi
if [ $TILIX_ID ] || [ $VTE_VERSION ] ; then source /etc/profile.d/vte.sh; fi # Ubuntu Budgie END

#_______________________________________________________________________________


export EDITOR='vi'
export VISUAL='vi'

HISTCONTROL=ignorespace:erasedups;

alias sudo='sudo ';
alias rm='rm -iv';
alias rmdir='rmdir -v';
alias mkdir='mkdir -pv';
alias cp='cp -va';

PS1='\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;30m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

# export PATH=$PATH:$HOME/bin;


if [ "$TERM_PROGRAM" = "vscode" ]; then
  PS1=' \[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '
fi

alias bkiot-trak="rsync -arv --delete --exclude={'node_modules','vendor'} ~/Projects/iot/track-iot/ ~/git/repo/iot_solutions/track-iot";

alias vb_ubuntu='ssh -p 2521 ubuntu@127.0.0.1';
alias vb_rocky='ssh -p 2522 rocky@127.0.0.1';
alias vb_fedora='ssh -p 2525 fedora@127.0.0.1';
alias vb_lubuntu='ssh -p 2526 lubuntu@127.0.0.1';
#alias vb_centos='ssh -oHostKeyAlgorithms=+ssh-dss -p 2524 root@127.0.0.1';


# Some aliases involving SSH commands (sensitive information is replaced or obfuscated)
alias ssh_aws='sudo ssh -i "/path/to/your/aws_key.pem" ubuntu@your-aws-instance.compute.amazonaws.com' 
alias ssh_aws_docker='sudo ssh -i "/path/to/your/aws_key.pem" ubuntu@your-docker-instance.compute.amazonaws.com' 
alias ssh_ovh_root='ssh -i "/path/to/your/ovh_key/id_ecdsa" root@your-ovh-instance'
alias ssh_dazzling_root='ssh -i "/path/to/your/ovh_key/id_ecdsa" root@your-dazzling-instance' 
alias ssh_treasure_hunt='sudo ssh -i "/path/to/your/aws_key.pem" ubuntu@your-treasure-hunt-instance.compute.amazonaws.com'


alias authy='/snap/authy/current/authy > /dev/null 2>&1 & disown' 

#alias authy='/snap/authy/10/authy'
alias atom='flatpak run io.atom.Atom'
#alias docker='sudo docker'

alias kubectl="minikube kubectl --"
#alias studio='/opt/android-studio/bin/studio.sh'
alias studio='/opt/android-studio/bin/studio.sh > /dev/null 2>&1 & disown'

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$HOME/.sdkman/bin/sdkman-init.sh" ]] && source "$HOME/.sdkman/bin/sdkman-init.sh"

export PATH=$PATH:/usr/local/go/bin
#GOROOT=/usr/local/go
GOPATH=~/go

alias air='~/go/bin/air';

[ -f "/home/foxcodenine/.ghcup/env" ] && source "/home/foxcodenine/.ghcup/env" # ghcup-env
