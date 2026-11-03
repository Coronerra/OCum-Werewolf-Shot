<div align="center">

# 🐺💦 OCum Werewolf Shot

**Makes OCum Ascended's cum shot come from the tip of the ABC werewolf cock, aimed along the shaft.**

`v1.0` · Skyrim SE 1.5.97 · ESL · by **That Guy (Coronerra)**

</div>

> 🔞 Adult content. For adults 18+ only.

## What it does
- OCum fires its shot from a node called `Urethra`, which it attaches to male actors through an armor addon. Normally that node hangs off `NPC Genitals06 [Gen06]`. The ABC werewolf animations don't move that bone, because the werewolf cock bends on the `WWD 1–9` bones. So the shot came from the wrong place, aimed the wrong way.
- This ESL adds a **WerewolfBeastRace-only** armor addon. Its mesh, `Meshes\OCum\UrethraNodeWerewolf.nif`, puts `Urethra` on ABC's tip bone **`WWD 9`**, 2 units out, firing **along the shaft**.
- It removes WerewolfBeastRace from OCum's own addon so the new one is used. Humans, elves, vampires and Vampire Lords are unchanged.
- **Werebears aren't covered**: they keep OCum's default (Gen06).
- No script changes. It works with plain OCum 4.1.1 and with the [OCum-Tull-Liquid-Softbody-Patch](https://github.com/Coronerra/OCum-Tull-Liquid-Softbody-Patch).

## ✅ Tested
Tested working on my modified **Nolvus 6.0.21** (Skyrim SE 1.5.97) with **ABC 3.31 Furry Works**.

## 📋 Requirements
- [OCum Ascended](https://www.nexusmods.com/skyrimspecialedition/mods/77506) **4.1.1** (`OCum.esp`)
- [OStim Standalone](https://www.nexusmods.com/skyrimspecialedition/mods/98163)
- [Animated Beasts Cocks (ABC)](https://www.loverslab.com/files/file/7556-animated-beasts-cocksabc-for-users-le-se/) (werewolf skeleton with the `WWD` bones; tested with 3.31 Furry Works)
- [OCreatures Reforged](https://www.patreon.com/LiraelAtelier) (creature scenes)
- **Recommended:** [OCum-Tull-Liquid-Softbody-Patch](https://github.com/Coronerra/OCum-Tull-Liquid-Softbody-Patch)

## 📦 Install (MO2)
1. Download `OCum-Werewolf-Shot_v1.0.zip` from [Releases](../../releases/latest). The archive root is `Data`.
2. Install it as a mod, anywhere **below OCum Ascended** in the left pane.
3. Plugin: `OCum_WerewolfUrethra.esp`, anywhere **after `OCum.esp`**. It's ESL-flagged, so it doesn't use a plugin slot.
4. Safe to add mid-save.

## 🛠️ Source
`tools/` has the Python scripts that built the plugin and mesh:
- `mkesl.py`: builds the plugin from OCum.esp
- `nif.py`: NIF reader and writer
- `tf.py`: reads the ABC skeleton transforms

## 🔗 Related
- 🐺 [Werewolf Overhaul: Proof of Concept](https://github.com/Coronerra/Werewolf-Overhaul-Proof-of-Concept)
- 💦 [OCum-Tull-Liquid-Softbody-Patch](https://github.com/Coronerra/OCum-Tull-Liquid-Softbody-Patch)
- 🌕 [Beast Aware](https://github.com/Coronerra/Beast-Aware)

## 🙏 Credits
- **Aietos**: OCum Ascended (the original records and the urethra node mesh this is based on)
- **ABC authors**: the werewolf skeleton and WWD bones
- **Lirael Atelier**: OCreatures Reforged
- **That Guy (Coronerra)**: this patch

My files are MIT-licensed (see [LICENSE](LICENSE)). The OCum-derived parts stay under OCum Ascended's permissions.

*Have fun and Happy Modding!*
