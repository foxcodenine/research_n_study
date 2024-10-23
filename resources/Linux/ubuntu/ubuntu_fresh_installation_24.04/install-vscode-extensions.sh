#!/bin/bash

# List of VSCode extensions to install
extensions=(
1natsu.insert-br-tag
amiralizadeh9480.laravel-extra-intellisense
bmewburn.vscode-intelephense-client
bradlc.vscode-tailwindcss
casualjim.gotemplate
codingyu.laravel-goto-view
cweijan.dbclient-jdbc
cweijan.vscode-mysql-client2
dakshmiglani.hex-to-rgba
diogogmt.jet
eamodio.gitlens
formulahendry.auto-rename-tag
golang.go
greven.umbra
hollowtree.vue-snippets
humao.rest-client
mariorodeghiero.vue-theme
mrmlnc.vscode-apache
ms-azuretools.vscode-docker
ms-kubernetes-tools.vscode-kubernetes-tools
onecentlin.laravel-blade
onecentlin.laravel5-snippets
phproberto.vscode-php-getters-setters
redhat.vscode-xml
redhat.vscode-yaml
ritwickdey.liveserver
ryannaddy.laravel-artisan
sdras.vue-vscode-snippets
shadowblood.tailwind-moon
shd101wyy.markdown-preview-enhanced
shufo.vscode-blade-formatter
silasnevstad.gpthelper
stkb.rewrap
txpipe.aiken
vincaslt.highlight-matching-tag
vue.volar
wayou.vscode-icons-mac
wayou.vscode-todo-highlight
zxh404.vscode-proto3
)

# Loop through the list and install each extension
for extension in "${extensions[@]}"
do
  echo "Installing $extension..."
  code --install-extension $extension
done

echo "All extensions installed!"
