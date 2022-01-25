### Viewing installed color schemes in Vim

-- 1. You can see the list of color schemes under /usr/share/vim/vimNN/colors

    $ ls -1 /usr/share/vim/vim81/colors/


-- 2. To change the default color scheme vi. Go to your home directory and create a .vimc file:

    $ cd ~
    $ vi .vimrc

-- 3. And insert the following (desecrt being the name of the color scheme):

    syntax on

    colorscheme desert

-- 4. You can also change the color scheme in vi by:

    <ESC>
    :colorscheme desert


-- 5. Add a new color scheme.
   Download scheme using wget 

    $ wget https://raw.githubusercontent.com/crusoexia/vim-monokai/master/colors/monokai.vim  .

Move it to /usr/share/vim/vimNN/colors  OR else (localy) by creating a ~/.vim/colors directoy and move there. 



