#
# ~/.zshrc.d/90-aliases.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

if [[ $EUID -ne 0 ]]; then
    alias sudo='sudo ' # needed for using aliases with sudo
fi
alias ls='ls -h --color=auto --group-directories-first'
alias ll='ls -la'
alias mynload='nload -t 1000 -i 500 -o 100 -u K'
alias whereami='pwd'
alias nano='nano -cw'
alias rm='rm -i'
alias mv='mv -i'
alias cp='cp -i'
alias xkill='xkill -button 1'
alias home='cd ~/'
alias ..='cd ..'
alias gst='git status -u'
alias less='less -iMW'
alias amiinscreen='echo $STY'
alias fuck='sudo $(fc -ln -1)'
alias bpython='clear && bpython'
alias pa='pacaur'
alias radio='~/scripts/radio/radio.sh'
alias syncit='~/scripts/syncit/syncit.sh'
alias cal='cal -m'
alias seconds='while true; do; date +"%H:%m:%S"; sleep 1; done'
alias dotdrop='eval $(cat ~/dotfiles/env.defaults ~/dotfiles/.env | grep -v "^#") ~/dotfiles/dotdrop.sh'
alias worms='worms -d 40 -l 16 -n 6'
{%@@ if profile == "fuckup" @@%}
alias janosch='~/scripts/wrapper.sh --both gcompris --disable-quit --disable-config --profile janosch-profil'
alias gphoto-capture='echo "gphoto2 --capture-image-and-download --interval 20 --filename image%5n.%C"'
alias ffmpeg-convert='echo "ffmpeg -f image2 -i image%5d.jpg -vf scale=-1:1080 -qscale 1 output.mkv (-qscale can be a value 1-31 (best-worst))"'
{%@@ endif @@%}
if which docker > /dev/null 2>&1; then
    alias docker-cleanup='docker rm -v $(docker ps -a -q -f status=exited) && docker rmi $(docker images -f "dangling=true" -q)'
    alias djoin='cont=$(docker ps --format="{{.ID}}" | head -n 1) && docker exec -it "$cont" bash'
fi
if which tremc > /dev/null 2>&1; then
    alias bt='tremc'
fi