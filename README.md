Pyvim - More Easy use vim in python  
======
it is my vim settings for python programming

Install 
--------
```shell
wget clone https://raw.githubusercontent.com/ipomoealba/Pyvim/master/.vimrc ~/.vimrc
``` 

and just open your terminal, enter `vim` and wait for it <br> 
At the end, you should read [this](https://github.com/Valloric/YouCompleteMe) to choose what kinds of language supporting autocomplete in your vim 
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
 'vim-scripts/taglist.vim'
* ins from github repos:
 'Chiel92/vim-autoformat'
 'nathanaelkane/vim-indent-guides'
* Override configs by directory
 'arielrossanigo/dir-configs-override.vim'
* Better file browser
 'scrooloose/nerdtree'
* Code commenter
 'scrooloose/nerdcommenter'
* Class/module browser
 'majutsushi/tagbar'
* Code and files fuzzy finder
 'ctrlpvim/ctrlp.vim'
* Extension to ctrlp, for fuzzy command finder
 'fisadev/vim-ctrlp-cmdpalette'
 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }
 'junegunn/fzf.vim'
* Task List 
 'vim-scripts/TaskList.vim'
* Zen coding
 'mattn/emmet-vim'
* Git integration
 'motemen/git-vim'
* Tab list panel
 'kien/tabman.vim'
* Airline
 'vim-airline/vim-airline'
 'vim-airline/vim-airline-themes'
* darcula theme
 'dracula/vim'
* Terminal Vim with 256 colors colorscheme
 'fisadev/fisa-vim-colorscheme'
* Surround
 'tpope/vim-surround'
* Indent text object
 'michaeljsmith/vim-indent-object'
* Python autocompletion, go to definition.
 'davidhalter/jedi-vim'
 'SirVer/ultisnips'
* Snippets manager (SnipMate), dependencies, and snippets repo
 'MarcWeber/vim-addon-mw-utils'
 'tomtom/tlib_vim'
 'honza/vim-snippets'
 'garbas/vim-snipmate'
* Git/mercurial/others diff icons on the side of the file lines
 'mhinz/vim-signify'
* Automatically sort python imports
 'fisadev/vim-isort'
* Drag visual blocks arround
 'fisadev/dragvisuals.vim'
* Window chooser
 't9md/vim-choosewin'
* Python and other languages code checker
 'scrooloose/syntastic'
* Ack code search (requires ack installed in the system)
 'mileszs/ack.vim'
* gitgutter
 'airblade/vim-gitgutter'
* csv.vim
 'chrisbra/csv.vim'
* Folder
 'tmhedberg/SimpylFold'
* vim pep8
 'tell-k/vim-autopep8'
* css highlight
 'hail2u/vim-css3-syntax'
* css color visualization
 'ap/vim-css-color'
* js highlight
 'pangloss/vim-javascript'
* html5 complete
 'othree/html5.vim'
* auto pairs
 'jiangmiao/auto-pairs'
* auto complete
 'Valloric/YouCompleteMe'
* animate when vim start
 'mhinz/vim-startify'
* YAPF formatter for Python
 'pignacio/vim-yapf-format'
* Search results counter
 'vim-scripts/IndexedSearch'
* XML/HTML tags navigation
 'vim-scripts/matchit.zip'
* Gvim colorscheme
 'vim-scripts/Wombat'
* Yank history navigation
 'vim-scripts/YankRing.vim'


Maybe need to install 
---------------------
> Powerline fonts [https://github.com/powerline/fonts](https://github.com/powerline/fonts) <br>
> Ctags [http://ctags.sourceforge.net](http://ctags.sourceforge.net)



Reference
---------
> YouComplete Me [https://github.com/Valloric/YouCompleteMe](https://github.com/Valloric/YouCompleteMe)<br>
> Awesome Vim [https://github.com/amix/vimrc](https://github.com/amix/vimrc)<br>
> Fisa vim config [https://github.com/fisadev/fisa-vim-config/](https://github.com/fisadev/fisa-vim-config/)<br>

