# Editor support for Spack config files

> [!TIP]
> The schemas from this repository are part of https://www.schemastore.org/.
> If your editor (or an extension) supports JSON Schema Store, validation and autocompletion of Spack configuration files should be **automatic** based on the filename or path (e.g. `spack.yaml` or `~/.spack/config.yaml`).

To get validation and autocompletion of Spack configuration files, enable an extension for the
YAML Language Server Protocol (LSP) in your editor of choice.

* **Visual Studio Code**: Install the [YAML Language Support extension by Red Hat][vsc].
* **Neovim**: Install [yaml-language-server][yamlls].
    <details>
    <summary>0.11.x and newer</summary>

    ```lua
    --- $XDG_CONFIG_HOME/nvim/lsp/yamlls.lua
    return {
      cmd = { "yaml-language-server", "--stdio" },
      filetypes = { "yaml", "yaml.docker-compose", "yaml.gitlab" },
      single_file_support = true,
      settings = {
        -- https://github.com/redhat-developer/vscode-redhat-telemetry#how-to-disable-telemetry-reporting
        redhat = { telemetry = { enabled = false } },
      },
    }

    --- $XDG_CONFIG_HOME/nvim/init.lua
    vim.lsp.enable("yamlls")
    
    -- Bootstrap lazy.nvim
    local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
    if not (vim.uv or vim.loop).fs_stat(lazypath) then
        local lazyrepo = "https://github.com/folke/lazy.nvim.git"
        local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
        if vim.v.shell_error ~= 0 then
            vim.api.nvim_echo({
                { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
                { out, "WarningMsg" },
                { "\nPress any key to exit..." },
            }, true, {})
            vim.fn.getchar()
            os.exit(1)
        end
    end
    vim.opt.rtp:prepend(lazypath)

    vim.g.mapleader = " "
    vim.g.maplocalleader = "\\"

    -- Setup lazy.nvim
    require("lazy").setup({
        spec = {
            -- For completions.
            -- See https://cmp.saghen.dev/ for more config options
            { "saghen/blink.cmp", opts = {} },
        },
        checker = { enabled = true },
    })
    ```
    </details>
    <details>
    <summary>0.10.x and older</summary>

    ```lua
    -- Bootstrap lazy.nvim
    local lazypath = vim.fn.stdpath("data") .. "/lazy/lazy.nvim"
    if not (vim.uv or vim.loop).fs_stat(lazypath) then
        local lazyrepo = "https://github.com/folke/lazy.nvim.git"
        local out = vim.fn.system({ "git", "clone", "--filter=blob:none", "--branch=stable", lazyrepo, lazypath })
        if vim.v.shell_error ~= 0 then
            vim.api.nvim_echo({
                { "Failed to clone lazy.nvim:\n", "ErrorMsg" },
                { out, "WarningMsg" },
                { "\nPress any key to exit..." },
            }, true, {})
            vim.fn.getchar()
            os.exit(1)
        end
    end
    vim.opt.rtp:prepend(lazypath)

    vim.g.mapleader = " "
    vim.g.maplocalleader = "\\"

    -- Setup lazy.nvim
    require("lazy").setup({
        spec = {
            {
              "neovim/nvim-lspconfig",
              config = function()
                local lspconfig = require("lspconfig")

                lspconfig.yamlls.setup({})
              end,
            }
            -- For completions.
            -- See https://cmp.saghen.dev/ for more config options
            { "saghen/blink.cmp", opts = {} },
        },
        checker = { enabled = true },
    })
    ```
    </details>

[vsc]: https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml
[yamlls]: https://github.com/redhat-developer/yaml-language-server

Optionally, add the following line at the top of your YAML file:

## Environments (spack.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/spack.json
```

## Packages (packages.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/packages.json
```

## Config (config.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/config.json
```

## Modules (modules.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/modules.json
```

## Mirrors (mirrors.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/mirrors.json
```

## Concretizer (concretizer.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/concretizer.json
```

## CI (ci.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/ci.json
```
