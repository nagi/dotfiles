#
# ~/.zshrc.d/35-less.zsh
# {{@@ env['dotdrop_warning'] @@}}
#

# enable syntax highlight in less
if [[ -f /usr/bin/src-hilite-lesspipe.sh ]]; then
    export LESSOPEN="| /usr/bin/src-hilite-lesspipe.sh %s"
fi

# default less options
export LESS='-i -M -R -S -W -z-4'