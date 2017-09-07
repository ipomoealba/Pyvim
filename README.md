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

Maybe need to install 
---------------------
> Powerline fonts [https://github.com/powerline/fonts](https://github.com/powerline/fonts) <br>
> Ctags [http://ctags.sourceforge.net](http://ctags.sourceforge.net)



Reference
---------
> YouComplete Me [https://github.com/Valloric/YouCompleteMe](https://github.com/Valloric/YouCompleteMe)<br>
> Awesome Vim [https://github.com/amix/vimrc](https://github.com/amix/vimrc)<br>
> Fisa vim config [https://github.com/fisadev/fisa-vim-config/](https://github.com/fisadev/fisa-vim-config/)<br>

