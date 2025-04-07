# Editor support for Spack config files

To get validation and autocompletion of Spack configuration files, enable an extension for the
YAML Language Server Protocol (LSP) in your editor of choice.

* **Visual Studio Code**: Install the [YAML Language Support extension by Red Hat][vsc].

[vsc]: https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml

Then add the following line at the top of your YAML file:

## Environments (spack.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/spack.json

spack:
    ...
```

## Packages (packages.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/packages.json

packages:
    ...
```

## Config (config.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/config.json

config:
    ...
```

## Modules (modules.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/modules.json

modules:
    ...
```

## Mirrors (mirrors.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/mirrors.json

mirrors:
    ...
```

## Concretizer (concretizer.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/concretizer.json

concretizer:
    ...
```

# CI (ci.yaml)

```yaml
# yaml-language-server: $schema=https://raw.githubusercontent.com/spack/schemas/refs/heads/main/schemas/ci.json

ci:
    ...
```
