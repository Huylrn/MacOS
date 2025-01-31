# $$Tools for MacOs$$

<details>
<!-- head -->
<summary>Menu</summary>
<!-- body -->

- [Oh my zsh](#oh-my-zsh),
- [Brew](#brew)
- [Theme](#theme)
- [Autojump](#autojump)
- [zsh-autosuggestions](#zsh-autosuggestions)
- [zsh-syntax-highlighting](#zsh-syntax-highlighting)
- [zsh-autocomplete](#zsh-autocomplete)
- [Colorls](#colorls)
- [Issues](#issues)

</details>

---

# **Oh my zsh** 
>More information about **`Oh my zsh`** [*here.*](https://github.com/ohmyzsh/ohmyzsh#unattended-install)

- ### **install** 

	```sh
	sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
	```
# **Brew**
- ### **install**
  - **Step 1:**
	```sh
  	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	```
  - **Step 2:**
	- **Method 1**
	```sh
	echo "\n# Homebrew" >> ~/.zprofile &&
	echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile &&
	eval "$(/opt/homebrew/bin/brew shellenv)"
	```
	- **Method 2**
	```sh
	# This method will not be able to use the tab to completion the command.
	cd /opt/homebrew/bin/ &&
	PATH=$PATH:/opt/homebrew/bin &&
	cd ~ &&
	echo "\n# Homebrew" >> ~/.zshrc &&
	echo 'export PATH=$PATH:/opt/homebrew/bin' >> .zshrc 
	```
- ### **My Formulae && cask**

# **Theme**
***Requirement:*** `brew`[<sub>*§*</sub>](#brew)

### **1. Font**:
>More information about **`Hack Nerd fonts`** [*here.*](https://github.com/ryanoasis/nerd-fonts#option-4-homebrew-fonts)

- **First step:** *Install Hack nerd font.*
	```sh
	brew tap homebrew/cask-fonts
	brew install font-hack-nerd-font
	```
- **Next step:** *setup font.*
	> **open** `Terminal` -> `Settings` -> `Profiles` -> `Text` -> `Font` -> `Search`*(Hack Nerd Font)*  -> **Ok**

---
### **2. powerlevel10k**:
>More information about **`powerlevel10k`** [*here.*](https://github.com/romkatv/powerlevel10k#homebrew)

***Requirement:*** `brew`[<sub>*§*</sub>](#brew) 
- #### **install**:
	```sh
	brew install powerlevel10k
	echo "\n# Powerlevel 10k" >> ~/.zshrc
	echo 'source $(brew --prefix)/share/powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc
	```	

# **Autojump**
>More information about **`Autojump`** [*here.*](https://github.com/wting/autojump#manual)

***Requirement:***
-  `brew`[<sub>*§*</sub>](#brew)
-  `git`
### **Install**
- **Step 1:**
	```sh
	cd ~/.config/zsh &&
	git clone https://github.com/wting/autojump.git
	```
- **Step 2:**
	```sh
	cd ~/.config/zsh/autojump &&
	./install.py 			
	```
- **Step 3:**
	```sh
	echo '\n# autojump' >> ~/.zshrc
	echo '[[ -s /Users/huynguyen/.autojump/etc/profile.d/autojump.sh ]]' >> ~/.zshrc
	echo 'source /Users/huynguyen/.autojump/etc/profile.d/autojump.sh' >> ~/.zshrc
	echo "autoload -U compinit ; compinit" >> ~/.zshrc
	```
---

### **Uninstall**

```sh
cd ~/.config/zsh/autojump &&
./uninstall.py
```


# **zsh-autosuggestions**
>More information about **`zsh-autosuggestions`** [*here.*](https://github.com/zsh-users/zsh-autosuggestions)

***Requirement***: `git`
- ### Install
	```sh
	cd ~/.oh-my-zsh/custom/plugins &&
	git clone https://github.com/zsh-users/zsh-autosuggestions.git
	```		
// add zsh-autosuggestions to .zshrc


# **zsh-syntax-highlighting**
>More information about **`zsh-syntax-highlighting`** [*here.*](https://github.com/zsh-users/zsh-syntax-highlighting.git)

***Requirement***: `git`
- ### **Install**
	```sh
	cd ~/.oh-my-zsh/custom/plugins &&
	git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
	```	
// add zsh-syntax-highlighting to .zshrc


# **zsh-autocomplete**
>More information about **`zsh-autocomplete`** [*here.*](https://github.com/marlonrichert/zsh-autocomplete#manual-installation)

***Requirement***: `git`
- ### **Install**
	```sh
	cd ~/.oh-my-zsh/custom/plugins &&
	git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git
	```
// add zsh-autocomplete to .zshrc
- ### **Update**
	```sh
	% git -C ~autocomplete pull
	```

# **Colorls**
>More information about **`Colorls`** [*here.*](https://github.com/athityakumar/colorls#installation)

***Requirement***: 
- `Hack Nerd Font`[<sub>*§*</sub>](#1-font)
- `gem` ***(gem --version)***
### **Install**
```sh
sudo gem install colorls &&
echo "\n# Colors (icon for file and folder, similar as "ls" command)" >> ~/.zshrc
echo 'source $(dirname $(gem which colorls))/tab_complete.sh' >> ~/.zshrc
```

# **Issues**
> My issues is  [*here.*](Content/my_issues.md)
### **1. Code command for `Visual studio code`**

- #### install from `visual studio code`:
> `Shift+Command+p` *(MacOs)* -> `search`*(Shell Command: Install 'code' command in PATH)* -> **OK**.
>
>![Not found](https://i.stack.imgur.com/CZJGA.gif)


- #### more
	```sh
	echo "\n# code command - visual studio code" >> ~/.zshrc  
	echo 'export PATH="$PATH:/Applications/Visual\ Studio\ Code.app/Contents/Resources/app/bin"' >> ~/.zshrc
	```
	
### **2. Dock**
- Remove the timeout when bringing cursor to the dock so that the dock appears in **dock hiding mode**.
	```sh
	defaults write com.apple.dock autohide-delay -float 0 && killall Dock
	```
