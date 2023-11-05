function check(){
    if [ -f $(which brew) ]; then
        return 0
    else
        return 1
    fi
}

function brewInstall(){
     $(brew install $@)
    if [ $? -eq 0 ]; then 
        printf "Thank You! / Cam On!"
    else 
        printf "You should try running the command agian!"
    fi
    return 0
}

color(){
    printf "$(tput setaf $1)${@:2} $(tput sgr0)"
    return
}

# input from autotoolbrew.py
$@

