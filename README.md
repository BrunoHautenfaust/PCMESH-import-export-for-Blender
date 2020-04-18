# PCMESH-import-export-for-Blender
Import and export pcmesh files into Blender.

These scripts are specifically targeted at [Spider-man: The Movie](https://en.wikipedia.org/wiki/Spider-Man_(2002_video_game)).

They are a partial port of **Mario_Kart64n**'s maxscript which only imports PCMESH files into 3DS MAX 8.

PCMESH files contain geometry, texture, and bones data for a 3D object.

As it is a partial port, it only supports import of vertices and faces but exports only vertices. So no UV mapping, bones or weights.

*NOTE:* The import script, much like the original maxscript, works only for Character meshes.

Also, some vertices might look messed up but when exported, the object will look fine ingame.

If you want to import the mesh back into the game, you'll need SpiderMan: The Movie Game (2002) PKG Modding Tool.

## Usage
You must be familiar with Blender to use this.

Open Text Editor in Blender and paste the script you want to use. Change the filename variable's path to the file you want to edit.

Run the script, edit the mesh, and when ready run the export script.

## Images

![blender](https://github.com/BrunoHautenfaust/PCMESH-import-export-for-Blender/blob/master/images/blender.png "blender")
![punk-spidey](https://github.com/BrunoHautenfaust/PCMESH-import-export-for-Blender/blob/master/images/punk_spidey.png "punk-spidey")
