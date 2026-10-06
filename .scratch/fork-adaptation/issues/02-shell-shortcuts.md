# Shell shortcuts `cs` and `cr`

Status: ready-for-agent

## What to do

Ship the two short commands from the original brief in this repo (for example `shell/shortcuts.bash`, sourced from `~/.bashrc`):

- `cs` alone opens the dashboard. `cs 3` or `cs user@example.com` runs `cswap switch`. Anything else passes through: `cs status`, `cs list`, `cs add`, and so on.
- `cr N [claude args]` runs `cswap run N --share-history -- [claude args]`, so every Parallel Instance sees the same Sessions. `cr` alone runs `cswap run --share-history`.

`cs` and `cr` were free on this machine on 2026-10-03.

Draft:

```bash
cs() {
  case "$1" in
    "") cswap ;;
    [0-9]*|*@*) cswap switch "$@" ;;
    *) cswap "$@" ;;
  esac
}
cr() {
  [ $# -eq 0 ] && { cswap run --share-history; return; }
  local who="$1"; shift
  cswap run "$who" --share-history -- "$@"
}
```
