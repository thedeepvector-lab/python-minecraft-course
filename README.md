# Learn Python by Building Your Own Minecraft World

Code for the YouTube series. One folder per episode. One rule: we never place a block by hand.

## Setup (covered in Episode 2)

1. **Minecraft Java Edition** 1.21.x
2. **Java 21** – https://adoptium.net
3. **Paper server** 1.21.x – https://papermc.io/downloads
4. **mcpq plugin** 2.3 – https://github.com/mcpq/mcpq-plugin (put the `.jar` in `server/plugins/`)
5. **Python 3.10+**, then:

```
pip install mcpq
```

In `server.properties`, set `gamemode=creative` and `level-type=minecraft\:flat` before the first start.
Start the server, join `localhost` from Multiplayer → Direct Connection, then run any script:

```
python episode-02/stairs.py
```

## Episodes

| # | Episode | Files |
|---|---|---|
| 1 | Python meets Minecraft | `episode-01/hello.py` |
| 2 | Connect Python to Minecraft | `episode-02/hello.py`, `axes.py`, `tower.py`, `stairs.py` |
| 3–10 | Coming soon | |

## Troubleshooting

- **Connection error** – the server isn't running, or the mcpq plugin isn't in `plugins/`.
- **Nothing appears** – you must be logged in to the server; scripts build next to the player.
- **Built in the wrong place** – remember `Vec3(x, y, z)`: `y` is height.

---
NOT AN OFFICIAL MINECRAFT PRODUCT. NOT APPROVED BY OR ASSOCIATED WITH MOJANG OR MICROSOFT.
