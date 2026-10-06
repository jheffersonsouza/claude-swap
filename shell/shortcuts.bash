# Short commands for claude-swap. Source this file from ~/.bashrc:
#
#   source /path/to/this/repo/shell/shortcuts.bash
#
#   cs                  open the dashboard
#   cs 3 | cs a@b.com   switch the default login to that account
#   cs -                switch back to the previous account
#   cs <command> ...    any other cswap command (status, list, add, auto...)
#   cr N [args...]      run account N in this terminal, sharing history and
#                       plugins; args go to claude (cr 2 --resume)
#   cr                  run the account mapped to the current directory
#
# cr needs --share-plugins, which upstream 0.26.0 does not have.

cs() {
  case "$1" in
    "") cswap ;;
    [0-9]*|*@*|-) cswap switch "$@" ;;
    *) cswap "$@" ;;
  esac
}

cr() {
  if [ $# -eq 0 ]; then
    cswap run --share-history --share-plugins
    return
  fi
  local account="$1"
  shift
  cswap run "$account" --share-history --share-plugins -- "$@"
}
