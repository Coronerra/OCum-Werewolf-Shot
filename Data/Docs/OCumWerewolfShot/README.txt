OCum Werewolf Shot v1.0 - That Guy (Coronerra)
Makes OCum Ascended's cum-shot effect come from the ABC werewolf's cock tip.

What it does
- OCum fires its shot from a node named "Urethra" that it equips on male actors
  (ocumurnode = ARMO OCumUrethraNodeSOS). Normally that node hangs off "NPC Genitals06 [Gen06]",
  which ABC's werewolf animations don't move (the werewolf cock bends on the WWD 1-9 bones).
- This ESL adds a werewolf-only armor addon (WerewolfBeastRace) whose mesh,
  Meshes\OCum\UrethraNodeWerewolf.nif, parents Urethra to ABC's tip bone "WWD 9", 2 units out
  along the shaft, firing along the shaft (+X of the WWD bones).
- It removes WerewolfBeastRace from OCum's own addon so the new one is used. Humans, elves,
  vampires and the Vampire Lord are unchanged. Werebears are unchanged (they still use Gen06).
- No script changes: works with OCum 4.1.1 and with "OCum TL SceneFix + GT Softbody Merge".

Requires: OCum Ascended 4.1.1 (OCum.esp), OStim Standalone, ABC (werewolf skeleton with WWD bones),
OCreatures Reforged.

Install (MO2): install the zip as a mod, anywhere below "OCum Ascended". Plugin: OCum_WerewolfUrethra.esp
anywhere after OCum.esp (ESL, no slot used).

Tested working on a modified Nolvus 6.0.21 (Skyrim SE 1.5.97) with ABC 3.31 Furry Works.
