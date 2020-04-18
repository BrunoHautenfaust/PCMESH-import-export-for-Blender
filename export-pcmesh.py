import struct
import bpy

'''
This script exports the vertices of an imported PCMESH object.
Manipulating the mesh vertices automatically scales the faces so no need to deal with them.
To use the script, change the filename with the absolute path to the PCMESH file you want to overwrite.
Backup your original one if needed.

IMPORTANT:
Keep the vertex count as is!
If you have more vertices, you'll have more data to write back to the file.
And at some point your added vertices might overwrite some other buffer (data region) resulting in a corrupted file.
Having less vertices also doesn't work. It breaks the mesh. Doesn't matter what you write to fill the remaining original vertex length.
Maybe it has something to do with faces.
'''

# Absolute path to PCMESH file
filename = 'D:\Folder\<SOMETHING>.PCMESH'

bpy.ops.object.mode_set(mode = 'EDIT')
bpy.ops.object.mode_set(mode = 'OBJECT')

with open(filename, 'r+b') as f:
    f.seek(20, 0)
    
    vertex_count = int.from_bytes(f.read(4), byteorder='little')
    vertex_offset = int.from_bytes(f.read(4), byteorder='little')

    export_obj = bpy.data.objects['pcmesh']
    
    i = 1
    f.seek(vertex_offset)
    while i <= vertex_count:
        f.write(struct.pack('<f', export_obj.data.vertices[i].co[0]))
        f.write(struct.pack('<f', export_obj.data.vertices[i].co[2]))
        f.write(struct.pack('<f', export_obj.data.vertices[i].co[1]))
        f.seek(36, 1)
        i+=1