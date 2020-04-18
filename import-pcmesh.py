import struct
import bpy

'''
This script is a partial port of Mario_Kart64n's maxscript.
It imports character PCMESH files into Blender and creates vertices and faces only.
To use it, change the filename with the absolute path to the PCMESH file you want to import.
'''

# Absolute path to PCMESH file
filename = 'D:\Folder\<SOMETHING>.PCMESH'

# Build faces coordinates
def triangle_strip(count):
    fa = None
    fb = None
    fc = None
    face_flip = True
    face_reset = True
    face_add = 1
    x=1
    while x<= count:
        x+=1
        if (face_reset):
            x+=2
            face_reset = False
            face_flip = False
            fa = (struct.unpack('<H', f.read(2)))[0] + face_add
            tfa = (struct.unpack('<H', f.read(2)))[0] + face_add
            fb = (struct.unpack('<H', f.read(2)))[0] + face_add
            tfb = (struct.unpack('<H', f.read(2)))[0] + face_add
            fc = (struct.unpack('<H', f.read(2)))[0] + face_add
            tfc = (struct.unpack('<H', f.read(2)))[0] + face_add
            if (face_flip):
                faces.append((fa,fc,fb))
                face_flip = False
            else:
                faces.append((fa,fb,fc))
                face_flip = True
        else:
            fa = fb
            fb = fc
            fc = struct.unpack('<H', f.read(2))[0]
            tfa = tfb
            tfb = tfc
            tfc = (struct.unpack('<H', f.read(2)))[0]
            if (fc != 65535 and tfc != 65535):  # 65535 = 0xFFFF
                fc += face_add
                tfc += face_add
                if (face_flip):
                    faces.append((fa,fc,fb))
                    face_flip = False
                else:
                    faces.append((fa,fb,fc))
                    face_flip = True					
            else:
                face_reset = True

mesh = bpy.data.meshes.new('pcmesh')
obj = bpy.data.objects.new(mesh.name, mesh)
col = bpy.data.collections.get('Collection')
col.objects.link(obj)

with open(filename, 'rb') as f:
    f.seek(20, 0)
    
    vertex_count = int.from_bytes(f.read(4), byteorder='little')
    vertex_offset = int.from_bytes(f.read(4), byteorder='little')
    tvertex_count = int.from_bytes(f.read(4), byteorder='little')
    tvertex_offset = int.from_bytes(f.read(4), byteorder='little')
    face_count = int.from_bytes(f.read(4), byteorder='little')
    face_offset = int.from_bytes(f.read(4), byteorder='little')

    verts = []
    faces = []
    
    i = 1
    f.seek(vertex_offset)
    while i <= vertex_count:
        [vx] = struct.unpack('<f', f.read(4))
        [vy] = struct.unpack('<f', f.read(4))
        [vz] = struct.unpack('<f', f.read(4))
        
        verts.append((vx, vz, vy))
        f.seek(36, 1)
        i+=1
    
    f.seek(face_offset)
    triangle_strip(face_count)

verts.insert(0, verts[0])	# We duplicate the first vertex because faces array does not reference a vertex with index 0
mesh.from_pydata(vertices=verts, edges=[], faces=faces)