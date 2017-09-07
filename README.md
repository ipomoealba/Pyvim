Pyvim - More Easy use vim in python  
======
##### it is my vim settings for python programming

Install 
--------
```shell
wget clone https://raw.githubusercontent.com/ipomoealba/Pyvim/master/.vimrc ~/.vimrc
``` 

and just open your terminal, enter `vim` and wait for it 
At the end, you should read [this](https://github.com/Valloric/YouCompleteMe) too choose what kinds of language you want to support autocomplete and install packages
for example:
if I want to support all C-family languages, I just enter 

```shell
cd ~/.vim/plugged/YouCompleteMe
./install.py --clang-completer
```
if you get an error message like this 
>fatal: destination path '/home/iotbigdata/.vimrc' already exists and is not an empty directory.

can try to copy and paste this code in your terminal to back up the original .vimrc file 


```shell
mv .vimrc .vimrc_old 
```

How to Use?
----------
### [YouComplete Me](https://github.com/Valloric/YouCompleteMe)
Default install all language as it support.
If you have any problem, just see here. 

### [Emmet](https://docs.emmet.io)
```
<C-e>
```

### Others
#### Save file as sudo 
```
w!!
```
### KeyMaps

#### Global Mode
* Search File \(Crtlp\)
`,e`
* Comment \(NerdCommenter\)
`<leader>cc` 
* Fold Code 
`<space>`
* Task List
`<F2>`
* Open NerdTree
`<F3>`
* Open Taglist
`<F4>`
* Auto Format 
`<F6>`

#### Python Mode
* Run Python 
`<F9>`
* Run Python in Debug mode \(pdb\)
`<F10>`
* Go to Command 
`,d`
* Usage Command 
`,o`

> There is a lot of keymaps in my settings, but I lazy to breakdown all. Just see the ~/.vimrc file. :P


Installed Packeges
------------------

* Ctags
Plug 'vim-scripts/taglist.vim'
* Plugins from github repos:
Plug 'Chiel92/vim-autoformat'
Plug 'nathanaelkane/vim-indent-guides'
* Override configs by directory
Plug 'arielrossanigo/dir-configs-override.vim'
* Better file browser
Plug 'scrooloose/nerdtree'
* Code commenter
Plug 'scrooloose/nerdcommenter'
* Class/module browser
Plug 'majutsushi/tagbar'
* Code and files fuzzy finder
Plug 'ctrlpvim/ctrlp.vim'
* Extension to ctrlp, for fuzzy command finder
Plug 'fisadev/vim-ctrlp-cmdpalette'
Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
Plug 'junegunn/fzf.vim'
* Task List 
Plug 'vim-scripts/TaskList.vim'
* Zen coding
Plug 'mattn/emmet-vim'
* Git integration
Plug 'motemen/git-vim'
* Tab list panel
Plug 'kien/tabman.vim'
* Airline
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
* darcula theme
Plug 'dracula/vim'
* Terminal Vim with 256 colors colorscheme
Plug 'fisadev/fisa-vim-colorscheme'
* Surround
Plug 'tpope/vim-surround'
* Indent text object
Plug 'michaeljsmith/vim-indent-object'
* Python autocompletion, go to definition.
Plug 'davidhalter/jedi-vim'
Plug 'SirVer/ultisnips'
* Snippets manager (SnipMate), dependencies, and snippets repo
Plug 'MarcWeber/vim-addon-mw-utils'
Plug 'tomtom/tlib_vim'
Plug 'honza/vim-snippets'
Plug 'garbas/vim-snipmate'
* Git/mercurial/others diff icons on the side of the file lines
Plug 'mhinz/vim-signify'
* Automatically sort python imports
Plug 'fisadev/vim-isort'
* Drag visual blocks arround
Plug 'fisadev/dragvisuals.vim'
* Window chooser
Plug 't9md/vim-choosewin'
* Python and other languages code checker
Plug 'scrooloose/syntastic'
* Ack code search (requires ack installed in the system)
Plug 'mileszs/ack.vim'
* gitgutter
Plug 'airblade/vim-gitgutter'
* csv.vim
Plug 'chrisbra/csv.vim'
* Folder
Plug 'tmhedberg/SimpylFold'
* vim pep8
Plug 'tell-k/vim-autopep8'
* css highlight
Plug 'hail2u/vim-css3-syntax'
* css color visualization
Plug 'ap/vim-css-color'
* js highlight
Plug 'pangloss/vim-javascript'
* html5 complete
Plug 'othree/html5.vim'
* auto pairs
Plug 'jiangmiao/auto-pairs'
* auto complete
Plug 'Valloric/YouCompleteMe'
* animate when vim start
Plug 'mhinz/vim-startify'
* YAPF formatter for Python
Plug 'pignacio/vim-yapf-format'
* Search results counter
Plug 'vim-scripts/IndexedSearch'
* XML/HTML tags navigation
Plug 'vim-scripts/matchit.zip'
* Gvim colorscheme
Plug 'vim-scripts/Wombat'
* Yank history navigation
Plug 'vim-scripts/YankRing.vim'
Maybe need to install 
---------------------
> Powerline fonts [https://github.com/powerline/fonts](https://github.com/powerline/fonts) <br>
> Ctags [http://ctags.sourceforge.net](http://ctags.sourceforge.net)



Reference
---------
> YouComplete Me [https://github.com/Valloric/YouCompleteMe](https://github.com/Valloric/YouCompleteMe)<br>
> Awesome Vim [https://github.com/amix/vimrc](https://github.com/amix/vimrc)<br>
> Fisa vim config [https://github.com/fisadev/fisa-vim-config/](https://github.com/fisadev/fisa-vim-config/)<br>

