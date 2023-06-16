# Lurifos-Terminal
My Personal Linux discord presence discord presence.

# How To Use 
Creat your on app at [dev portal](https://discord.com/developers/applications/) or you can use mine `1117851631929802792`
- Run the main.py manually or by creating a systemd service (lurifosterm.service)
- Edit /tmp/lurifosterm/config.json
  You can directly edit to change the presence or integrate it with your own script (like this one extension that I make to integrate it with nvim)

# Neovim (NvChad) Integration
For nvchad integration, you can add [languages.json](https://github.com/BlueBeret/nvchad-custom/blob/main/languages.json) and [lurifosterm.lua](https://github.com/BlueBeret/nvchad-custom/blob/main/lurifosterm.lua) to your custom folder. Then add these code to your custom init.lua
```
vim.cmd([[
  augroup MyAutoCmds
    autocmd!
    autocmd VimEnter * lua require("custom.lurifosterm").initPresenceLoop()
    autocmd VimLeave * lua require("custom.lurifosterm").stopPresenceLoop()
  augroup END
]])
```
#### More example and better documentation comming soon
