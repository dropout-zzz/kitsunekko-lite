kitsunekko-lite
===============
![](https://img.shields.io/github/repo-size/dropout-zzz/kitsunekko-lite?style=for-the-badge) ![](https://img.shields.io/github/directory-file-count/dropout-zzz/kitsunekko-lite?type=dir&style=for-the-badge&label=directories) ![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgithub.com%2Fdropout-zzz%2Fkitsunekko-lite%2Fraw%2Fmain%2Fstatistics.json&query=%24.nfiles&style=for-the-badge&label=files)

Yet another Kitsunekko mirror.
## Features
- Single copy of things.
- Frozen unless manually updated.
- Non-anime, boring things and kid stuffs not included.
## Example use cases
- Clone and grep for specific word, dialogue or expression.

> [!NOTE]
>
> If you load these subtitles for watching,
> be aware this repository may not have the latest or best options,
> if you're watching anime or if you couldn't find something,
> try with all aliases of show title and also check upstream sites.
## Inclusion policy
- No unofficial subs.
- Prefer `.ass` format when they include special SSA effects.
- Prefer filenames with original titles.
## Limitations
- I only include animes I had watched.
## Things to do when adding a new show
- Run `update_statistics.py` script once files added into Git and before committing. If someone forgot this, make a separate commit that updates just the `statistics.json` file.
- Check if files look good. Avoid including unofficial subs.
- If adding `.srt` subtitles, double check if there is `.ass` ones available.
## Acknowledgements
- Upstream: https://github.com/Ajatt-Tools/kitsunekko-mirror
- Original: https://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F
- Jimaku: https://jimaku.cc/
