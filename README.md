# Elden Ring: light-attack DPS for every weapon, from game data

Sustained light-attack DPS for every melee weapon and infusion in Elden Ring (Shadow of the Erdtree included):
1H R1, 2H R1 and powerstance L1 chains, with the stat spread that maximises each one, against a flat defense or
against real bosses with their HP, defenses, absorption, bleed and frost.

Everything about the game comes from the game files: attack and cancel frames from `c0000.anibnd` (TAE), motion
values and hitboxes from `BehaviorParam_PC` / `AtkParam_Pc`, weapon numbers from `EquipParamWeapon` and
`ReinforceParamWeapon`, bosses from `NpcParam` and `SpEffectParam`. Nothing is written to the game folder.

**Interactive calculator:** [heyobi.github.io/er-frame-dps](https://heyobi.github.io/er-frame-dps/) (starting
class, rune level and Vigor/Mind/Endurance in, best spread per weapon out; pick a boss for bleed, frost and time to
kill; click a weapon for its attack chain and DPS by rune level).

Same idea for Dark Souls III: [heyobi/ds3-frame-dps](https://github.com/heyobi/ds3-frame-dps).

**Status:** the model matches a reference calculator on attack rating and matches the wiki on hit counts where I
could check, but none of it has been timed in game yet. Corrections and in-game tests are very welcome.

## Headline result

| # | Weapon | Infusion | Move | DPS | Hits per step | Str/Dex/Int/Fai/Arc |
|---|---|---|---|---|---|---|
| 1 | [Claws of Night](https://eldenring.wiki.fextralife.com/Claws+of+Night) | Standard | 2H R1 | 1,432 | 2-1-2-1-2-2 | 10/89/10/10/10 |
| 2 | [Venomous Fang](https://eldenring.wiki.fextralife.com/Venomous+Fang) | Heavy | 2H R1 | 1,142 | 2-1-2-1-2-2 | 89/10/10/10/10 |
| 3 | [Dane's Footwork](https://eldenring.wiki.fextralife.com/Dane's+Footwork) | Heavy | 2H R1 | 1,142 | 4-4-3-2-3-2 | 89/10/10/10/10 |
| 4 | [Bloodhound Claws](https://eldenring.wiki.fextralife.com/Bloodhound+Claws) | Heavy | 2H R1 | 1,080 | 2-1-2-1-2-2 | 84/15/10/10/10 |
| 5 | [Hookclaws](https://eldenring.wiki.fextralife.com/Hookclaws) | Keen | 2H R1 | 1,060 | 2-1-2-1-2-2 | 10/89/10/10/10 |
| 6 | [Bloodfiend's Fork](https://eldenring.wiki.fextralife.com/Bloodfiend's+Fork) | Flame Art | Powerstance L1 | 1,055 | 2-2-2 | 14/10/10/80/15 |
| 7 | [Dryleaf Arts](https://eldenring.wiki.fextralife.com/Dryleaf+Arts) | Heavy | 2H R1 | 1,043 | 2-4-3-2-3-2 | 89/10/10/10/10 |
| 8 | [Raptor Talons](https://eldenring.wiki.fextralife.com/Raptor+Talons) | Keen | 2H R1 | 1,036 | 2-1-2-1-2-2 | 10/89/10/10/10 |
| 9 | [Curseblade's Cirque](https://eldenring.wiki.fextralife.com/Curseblade's+Cirque) | Standard | 2H R1 | 1,036 | 2-2-2-1-2-2 | 19/80/10/10/10 |
| 10 | [Cross-Naginata](https://eldenring.wiki.fextralife.com/Cross-Naginata) | Keen | Powerstance L1 | 1,021 | 2-2-2 | 19/80/10/10/10 |
| 11 | [Sword Lance](https://eldenring.wiki.fextralife.com/Sword+Lance) | Heavy | Powerstance L1 | 1,015 | 2-2-2 | 88/11/10/10/10 |
| 12 | [Bandit's Curved Sword](https://eldenring.wiki.fextralife.com/Bandit's+Curved+Sword) | Keen | Powerstance L1 | 998 | 2-2-2-2 | 19/80/10/10/10 |
| 13 | [Beastman's Curved Sword](https://eldenring.wiki.fextralife.com/Beastman's+Curved+Sword) | Heavy | Powerstance L1 | 997 | 2-2-2-2 | 88/11/10/10/10 |
| 14 | [Backhand Blade](https://eldenring.wiki.fextralife.com/Backhand+Blade) | Lightning | 2H R1 | 987 | 2-2-2-1-2-2 | 10/89/10/10/10 |
| 15 | [Warped Axe](https://eldenring.wiki.fextralife.com/Warped+Axe) | Heavy | 2H R1 | 981 | 1-1-1-1-1 | 89/10/10/10/10 |
| 16 | [Clayman's Harpoon](https://eldenring.wiki.fextralife.com/Clayman's+Harpoon) | Magic | Powerstance L1 | 971 | 2-2-2 | 12/10/87/10/10 |
| 17 | [Grossmesser](https://eldenring.wiki.fextralife.com/Grossmesser) | Heavy | Powerstance L1 | 970 | 2-2-2-2 | 87/12/10/10/10 |
| 18 | [Bolt of Gransax](https://eldenring.wiki.fextralife.com/Bolt+of+Gransax) | Standard | Powerstance L1 | 967 | 2-2-2 | 20/79/10/10/10 |
| 19 | [Mantis Blade](https://eldenring.wiki.fextralife.com/Mantis+Blade) | Keen | Powerstance L1 | 945 | 2-2-2-2 | 19/80/10/10/10 |
| 20 | [Falchion](https://eldenring.wiki.fextralife.com/Falchion) | Heavy | Powerstance L1 | 941 | 2-2-2-2 | 86/13/10/10/10 |

Every weapon is at max upgrade (+25, or +10 for somber weapons), no buffs, no talismans. Starting from Wretch (all
stats 10) at rune level 150 with 60 Vigor, 15 Mind and 25 Endurance leaves 79 points for Str/Dex/Int/Fai/Arc, and
each weapon gets the spread that is best for it. "Hits per step" lists how many hits each step of the chain lands.

![Top 15 weapons against flat defense 130](results/top15_flat.png)

## Against bosses

The same search, but the target is a real boss: its HP, defense and absorption per damage type (with the area
scaling it has in game), its bleed and frost resistance, how much that resistance grows after each proc, and its
own bleed and frost damage rates. DPS here means HP divided by time to kill, so status procs count.

**Malenia, Blade of Miquella**. 18,473 HP. Bleed 421, frost 306 (buildup to the first proc, area scaling included).

| # | Weapon | Infusion | Move | DPS | Time to kill | Bleed DPS | Frost DPS | Str/Dex/Int/Fai/Arc |
|---|---|---|---|---|---|---|---|---|
| 1 | [Hookclaws](https://eldenring.wiki.fextralife.com/Hookclaws) | Cold | 2H R1 | 1,778 | 10.4 s | 387 | 506 | 10/79/20/10/10 |
| 2 | [Bloodhound Claws](https://eldenring.wiki.fextralife.com/Bloodhound+Claws) | Cold | 2H R1 | 1,778 | 10.4 s | 387 | 506 | 51/36/22/10/10 |
| 3 | [Raptor Talons](https://eldenring.wiki.fextralife.com/Raptor+Talons) | Cold | 2H R1 | 1,773 | 10.4 s | 386 | 505 | 10/79/20/10/10 |
| 4 | [Claws of Night](https://eldenring.wiki.fextralife.com/Claws+of+Night) | Standard | 2H R1 | 1,603 | 11.5 s | 349 |  | 10/89/10/10/10 |
| 5 | [Cross-Naginata](https://eldenring.wiki.fextralife.com/Cross-Naginata) | Cold | Powerstance L1 | 1,482 | 12.5 s | 322 | 316 | 16/73/20/10/10 |

**Promised Consort Radahn**. 46,134 HP. Bleed 734, frost 734 (buildup to the first proc, area scaling included).

| # | Weapon | Infusion | Move | DPS | Time to kill | Bleed DPS | Frost DPS | Str/Dex/Int/Fai/Arc |
|---|---|---|---|---|---|---|---|---|
| 1 | [Cross-Naginata](https://eldenring.wiki.fextralife.com/Cross-Naginata) | Cold | Powerstance L1 | 1,245 | 37.1 s | 246 | 244 | 16/73/20/10/10 |
| 2 | [Spiked Spear](https://eldenring.wiki.fextralife.com/Spiked+Spear) | Cold | Powerstance L1 | 1,179 | 39.1 s | 233 | 308 | 45/44/20/10/10 |
| 3 | [Bloodhound Claws](https://eldenring.wiki.fextralife.com/Bloodhound+Claws) | Cold | 2H R1 | 1,176 | 39.2 s | 233 | 308 | 47/23/39/10/10 |
| 4 | [Hookclaws](https://eldenring.wiki.fextralife.com/Hookclaws) | Cold | 2H R1 | 1,165 | 39.6 s | 230 | 381 | 10/79/20/10/10 |
| 5 | [Raptor Talons](https://eldenring.wiki.fextralife.com/Raptor+Talons) | Cold | 2H R1 | 1,165 | 39.6 s | 230 | 381 | 10/58/41/10/10 |

**Messmer**. 38,982 HP. Bleed 435, frost 316 (buildup to the first proc, area scaling included).

| # | Weapon | Infusion | Move | DPS | Time to kill | Bleed DPS | Frost DPS | Str/Dex/Int/Fai/Arc |
|---|---|---|---|---|---|---|---|---|
| 1 | [Hookclaws](https://eldenring.wiki.fextralife.com/Hookclaws) | Cold | 2H R1 | 1,869 | 20.9 s | 371 | 612 | 10/79/20/10/10 |
| 2 | [Bloodhound Claws](https://eldenring.wiki.fextralife.com/Bloodhound+Claws) | Cold | 2H R1 | 1,869 | 20.9 s | 371 | 612 | 52/37/20/10/10 |
| 3 | [Raptor Talons](https://eldenring.wiki.fextralife.com/Raptor+Talons) | Cold | 2H R1 | 1,869 | 20.9 s | 371 | 612 | 10/79/20/10/10 |
| 4 | [Claws of Night](https://eldenring.wiki.fextralife.com/Claws+of+Night) | Standard | 2H R1 | 1,740 | 22.4 s | 518 |  | 10/89/10/10/10 |
| 5 | [Venomous Fang](https://eldenring.wiki.fextralife.com/Venomous+Fang) | Cold | 2H R1 | 1,556 | 25.1 s |  | 510 | 35/54/20/10/10 |

**Mohg, Lord of Blood**. 18,389 HP. Bleed 291, frost 654 (buildup to the first proc, area scaling included).

| # | Weapon | Infusion | Move | DPS | Time to kill | Bleed DPS | Frost DPS | Str/Dex/Int/Fai/Arc |
|---|---|---|---|---|---|---|---|---|
| 1 | [Claws of Night](https://eldenring.wiki.fextralife.com/Claws+of+Night) | Standard | 2H R1 | 1,501 | 12.3 s | 350 |  | 10/89/10/10/10 |
| 2 | [Bloodhound Claws](https://eldenring.wiki.fextralife.com/Bloodhound+Claws) | Occult | 2H R1 | 1,360 | 13.5 s | 423 |  | 14/15/10/10/80 |
| 3 | [Hookclaws](https://eldenring.wiki.fextralife.com/Hookclaws) | Cold | 2H R1 | 1,335 | 13.8 s | 311 | 190 | 10/79/20/10/10 |
| 4 | [Raptor Talons](https://eldenring.wiki.fextralife.com/Raptor+Talons) | Cold | 2H R1 | 1,316 | 14.0 s | 307 | 187 | 10/79/20/10/10 |
| 5 | [Cross-Naginata](https://eldenring.wiki.fextralife.com/Cross-Naginata) | Occult | Powerstance L1 | 1,266 | 14.5 s | 393 |  | 16/20/10/10/73 |

Full tables for these and other bosses: [`results/rankings.md`](results/rankings.md), or pick any of 27 bosses in the calculator.

## Method

**Attack chains.** Each light-attack step is an animation in the weapon class's TAE (`a<2000 + wepmotionCategory>`,
checking the weapon's special category first). 1H R1 starts at animation 30000, 2H R1 at 32000 and powerstance /
dual L1 at 34000, one animation per step (+10). A step lasts until its first R1-cancel flag (TAE flag 4 or 115),
the first frame the next attack can start; the chain loops after its last step. DPS = damage of the whole chain
divided by its length at 60 fps.

**Hits.** Every `AttackBehavior` event that starts before the cancel is a hit window, with its behavior judge id
pointing into `BehaviorParam_PC` → `AtkParam_Pc` for motion values and attack type. Windows of the same hand that
touch or overlap are phases of one swing and count once (the strongest phase); different hands, or windows separated
in time, count separately. Light greatswords also carry stamina-free 99x hitboxes; they are dropped because the
wiki's hit counts (5th light attack hits twice, 3rd dual attack 3 times, 4th dual attack 4 times) only come out
right without them.

**Attack rating.** Base damage × upgrade rate × (1 + Σ scaling × stat curve), using `AttackElementCorrectParam`
for which stat scales which element and `CalcCorrectGraph` for the curves. Two-handing multiplies Strength by 1.5,
except on paired weapons. An unmet requirement gives −40% on every element that stat scales (and on bleed for
Arcane). `tools/validate_ar.py` compares this with
[ThomasJClark's Elden Ring weapon calculator](https://github.com/ThomasJClark/elden-ring-weapon-calculator) on 2400
random weapon / stat / upgrade cases: every melee weapon matches within 0.6 AR, and bleed and frost buildup match too.
(Bows differ because that calculator always two-hands them; this model leaves bows out.)

**Damage.** Each element goes through the usual Souls attack/defense curve against the target's defense, times
the target's absorption for that damage type (standard, slash, strike, pierce, magic, fire, lightning, holy).
The curve is the community-derived formula; it is not stored in the game data.

**Bleed and frost.** Buildup per hit comes from the weapon's status SpEffect at its upgrade level, with Arcane
scaling where the weapon has it. Proc damage comes from the same SpEffect: bleed 15% of max HP + 100, frost 10% + 30,
and frostbite makes the target take 20% more damage for 30 s (all read from `SpEffectParam`). A boss's resistance
rises after each proc by its `ResistCorrectParam` row, and its bleed / frost damage rate scales the proc. Time to
kill is an event simulation of direct damage plus procs.

**Stat search.** Requirements first, then one point at a time to whichever stat raises direct DPS most per point
(looking 1 to 20 points ahead so slow-starting curves are not skipped). Against a boss, bleed weapons then move
points into Arcane while that kills faster.

## What is not in the model

Buildup decay (so frost may look a bit better than it is against bosses you cannot hit constantly), stamina,
poise and stagger, buffs and talismans, weapon skills, heavy and running attacks, poison / rot / sleep / madness,
upgrade levels below max (calculator), and in-game timing tests. Powerstance assumes two copies of the weapon;
some unique weapons only have one per playthrough (paired weapons need just one).

## Files

| Path | What it is |
|---|---|
| `tools/er_extract.py` + `er_keys.json` | Read-only extractor for the encrypted archives (`Data0-3`, `DLC`), e.g. `/chr/c0000.anibnd.dcx` |
| `krak/` | Tiny Rust wrapper around the `oozextract` crate to decompress Oodle Kraken DCX files |
| `tools/er_regulation.py` | Decrypts `regulation.bin` and writes every `.param` |
| `tools/er_load.py` | Params + TAE → `er.pkl` (uses `param_reader.py` with Paramdex layouts and the TAE / BND reader in `ds3_frames.py`) |
| `tools/er_model.py` | Attack rating, chains, hit grouping, bosses, status, time-to-kill simulation |
| `tools/er_rank.py` | Stat search for every weapon / infusion / move; writes the markdown tables |
| `tools/export_web.py` | Builds `docs/data.json` for the calculator |
| `tools/validate_ar.py` + `validate_ar_ref.ts` | AR check against the reference calculator |
| `docs/` | The calculator (static page; `docs/calc.js` is the same model in JavaScript) |
| `results/` | Generated tables and chart |

## Reproduce

```sh
# 1. game files (read-only)
python3 tools/er_extract.py "<steam>/ELDEN RING/Game" er_files /chr/c0000.anibnd.dcx
(cd krak && cargo build --release)
krak/target/release/krak er_files/<Archive>__chr__c0000.anibnd.dcx er_files/c0000.anibnd   # the DLC__ copy if there are two
python3 tools/er_regulation.py "<steam>/ELDEN RING/Game/regulation.bin" er_files
# 2. model
git clone https://github.com/soulsmods/Paramdex
export ER_FILES=er_files PARAMDEX_ER=Paramdex/ER
python3 tools/er_load.py
python3 tools/er_rank.py --budget 79 "Malenia, Blade of Miquella" > results/rankings.md
python3 tools/export_web.py --out docs/data.json
```

## Credits

Param layouts from [Paramdex](https://github.com/soulsmods/Paramdex), archive keys from UXM Selective Unpacker,
file formats from SoulsFormats, AR reference from ThomasJClark's calculator, hit counts cross-checked against
[eldenring.wiki.gg](https://eldenring.wiki.gg/wiki/Light_Greatswords).

MIT license.
