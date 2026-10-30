# Part 2 - Delivarable

## 1. Git status and secret-file checks

Git status output provided for the project:

```text
warning: could not open directory 'Application Data/': Permission denied
warning: could not open directory 'Cookies/': Permission denied
warning: could not open directory 'Documents/My Music/': Permission denied
warning: could not open directory 'Documents/My Pictures/': Permission denied
warning: could not open directory 'Documents/My Videos/': Permission denied
warning: could not open directory 'Local Settings/': Permission denied
warning: could not open directory 'My Documents/': Permission denied
warning: could not open directory 'NetHood/': Permission denied
warning: could not open directory 'PrintHood/': Permission denied
warning: could not open directory 'Recent/': Permission denied
warning: could not open directory 'SendTo/': Permission denied
warning: could not open directory 'Start Menu/': Permission denied
warning: could not open directory 'Templates/': Permission denied
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../../../.anaconda/
        ../../../.antigravity/
        ../../../.bash_history
        ../../../.cache/
        ../../../.claude-server-commander/
        ../../../.codegpt/
        ../../../.codex/
        ../../../.conda/
        ../../../.continuum/
        ../../../.copilot/
        ../../../.cursor/
        ../../../.gemini/
        ../../../.gitconfig
        ../../../.ipython/
        ../../../.jupyter/
        ../../../.keras/
        ../../../.lesshst
        ../../../.local/
        ../../../.matplotlib/
        ../../../.viminfo
        ../../../.vscode-shared/
        ../../../.vscode/
        ../../../AppData/
        ../../../Contacts/
        ../../../CrossDevice/
        ../../../Downloads/
        ../../../Favorites/
        ../../../Links/
        ../../../Music/
        ../../../NTUSER.DAT
        ../../../NTUSER.DAT{6aede265-bd7e-11f0-9fd6-14b5cd51cd78}.TM.blf
        ../../../NTUSER.DAT{6aede265-bd7e-11f0-9fd6-14b5cd51cd78}.TM.blf.cnpf
        ../../../NTUSER.DAT{6aede265-bd7e-11f0-9fd6-14b5cd51cd78}.TMContainer00000000000000000001.regtrans-ms
        ../../../NTUSER.DAT{6aede265-bd7e-11f0-9fd6-14b5cd51cd78}.TMContainer00000000000000000001.regtrans-ms.cnpf
        ../../../NTUSER.DAT{6aede265-bd7e-11f0-9fd6-14b5cd51cd78}.TMContainer00000000000000000002.regtrans-ms
        ../../../NTUSER.DAT{6aede265-bd7e-11f0-9fd6-14b5cd51cd78}.TMContainer00000000000000000002.regtrans-ms.cnpf
        ../../
        ../../../PyCharmMiscProject/
        ../../../Saved Games/
        ../../../Searches/
        ../../../Videos/
        ../../../anaconda3/
        ../../../ntuser.dat.LOG1
        ../../../ntuser.dat.LOG2
        ../../../ntuser.ini

nothing added to commit but untracked files present (use "git add" to track)
```

This output does not establish that `.env` is ignored or that `.env.template` is tracked: Git is reporting untracked paths throughout the user profile, and the project directory is collapsed as `../../`. A tracked-file check for `.env.template` failed (`git ls-files --error-unmatch .env.template` reported that the path is not known to Git). The only `.gitignore` found is under `src/epita_group7/`, so it does not protect the root-level `.env`; the ignore check for `.env` could not be completed. Therefore, the requested confirmation is **not yet verified**; do not treat `.env` as safely omitted or `.env.template` as tracked until these checks are rerun from the intended repository root.

## 2. Redacted live API response

The API response contains no API key. The following is an abbreviated rendering of the supplied response; article details are shortened for readability:

```json
{
  "status": "LIVE_SUCCESS",
  "total_results": 38,
  "articles": [
    {
      "source": "The Wall Street Journal",
      "title": "Stock Market Today: Nasdaq Sinks 350 Points; Google's Tumble in Focus — Live Updates - WSJ",
      "publishedAt": "2026-10-29T18:25:12Z"
    },
    {
      "source": "NBC News",
      "title": "Alaska governor orders investigation into Peltola camp after report they recruited second Dan Sullivan - NBC News",
      "publishedAt": "2026-10-29T17:29:20Z"
    },
    {
      "source": "The Washington Post",
      "title": "As Trump derides judge again, officials say golf course will soon close",
      "publishedAt": "2026-10-29T17:26:48Z"
    }
  ]
}
```

The live response reported 38 results. The output shown above preserves the response status and result count and includes three representative article records; remaining article records and fields are omitted.

## 3. Why is storing secrets in environment variables superior to putting them in configuration files like config.json or settings.yaml? Give two security reasons.

1. *They keep secrets out of source control.*
2. *They support separate runtime config.*
