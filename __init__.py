import bpy
from . import boneMaps_renamer
from .boneMaps_renamer import *

bl_info = {
    "name": "Bones Renamer",
    "author": "",
    "version": (1, 0),
    "blender": (4, 4, 0),  # Aktualisiert für Blender 4.4
    "location": "View3D > Sidebar > Bones Renamer",
    "description": "Mass rename bones for armature conversion between formats",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging",  # Besser passende Kategorie
}

class BonesRenamerPanel(bpy.types.Panel):
    """Creates the Bones Renamer Panel in the 3D View Sidebar"""
    bl_label = "Bones Renamer"
    bl_idname = "OBJECT_PT_bones_renamer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"  # Geändert von "TOOLS" zu "UI" (Blender 2.8+)
    bl_category = "Rig"    # Passender Tab-Name

    def draw(self, context):
        layout = self.layout
        layout.label(text="Mass Rename Bones", icon="ARMATURE_DATA")
        
        # Dropdown-Menüs für Quell-/Ziel-Rigs
        layout.prop(context.scene, "Origin_Armature_Type")
        layout.prop(context.scene, "Destination_Armature_Type")
        
        # Umbenennungs-Button
        layout.operator("object.bones_renamer", text="Rename Bones")

def main(context):
    use_international_fonts_display_names_bones()
    unhide_all_armatures()
    rename_bones(
        bpy.context.scene.Origin_Armature_Type,
        bpy.context.scene.Destination_Armature_Type
    )
    rename_finger_bones(
        bpy.context.scene.Origin_Armature_Type,
        bpy.context.scene.Destination_Armature_Type
    )
    bpy.ops.object.mode_set(mode='POSE')
    bpy.ops.pose.select_all(action='SELECT')

class BonesRenamer(bpy.types.Operator):
    """Mass rename bones for armature conversion"""
    bl_idname = "object.bones_renamer"
    bl_label = "Bones Renamer"
    bl_options = {'REGISTER', 'UNDO'}

    # Dropdown-Optionen für Quell-Rig
    origin_types = [
        ('mmd_english', 'MMD English', 'MikuMikuDance English bone names'),
        ('xna_lara', 'XNALara', 'XNALara bone names'),
        ('daz_poser', 'DAZ/Poser', 'DAZ/Poser bone names'),
        ('blender_rigify', 'Rigify (Pre-Generate)', 'Blender Rigify bones before generation'),
        ('sims_2', 'Sims 2', 'Sims 2 bone names'),
        ('motion_builder', 'Motion Builder', 'Motion Builder bone names'),
        ('3ds_max', '3ds Max', '3ds Max bone names'),
        ('bepu', 'Bepu IK', 'Bepu full body IK bone names'),
        ('mmd_japanese', 'MMD Japanese', 'MikuMikuDance Japanese bone names'),
        ('mmd_japaneseLR', 'MMD Japanese (.L/.R)', 'MMD Japanese bones with .L/.R suffixes'),
        ('opensim', 'OpenSim', 'OpenSimulator avatar bones'),  # Neu hinzugefügt
    ]

    # Dropdown-Optionen für Ziel-Rig (gleiche wie oben)
    bpy.types.Scene.Origin_Armature_Type = bpy.props.EnumProperty(
        items=origin_types,
        name="Source Rig Type",
        default='mmd_japanese'
    )

    bpy.types.Scene.Destination_Armature_Type = bpy.props.EnumProperty(
        items=origin_types,  # Nutzt dieselbe Liste
        name="Target Rig Type",
        default='blender_rigify'
    )

    def execute(self, context):
        main(context)
        return {'FINISHED'}

# Registrierung für Blender 4.4 (ohne veraltetes register_module)
classes = (BonesRenamerPanel, BonesRenamer)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
