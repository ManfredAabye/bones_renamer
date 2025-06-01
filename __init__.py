import bpy
import logging
from . import boneMaps_renamer
from .boneMaps_renamer import *

# Set up logging
logger = logging.getLogger(__name__)

bl_info = {
    "name": "Bones Renamer",
    "author": "",
    "version": (1, 0),
    "blender": (4, 4, 0),
    "location": "View3D > Sidebar > Bones Renamer",
    "description": "Mass rename bones for armature conversion between formats",
    "warning": "",
    "wiki_url": "",
    "category": "Rigging",
}

# Define the enum items at module level
ORIGIN_TYPES = [
    ('mmd_english', "MMD English", "MikuMikuDance English bone names"),
    ('xna_lara', "XNALara", "XNALara bone names"),
    ('daz_poser', "DAZ/Poser", "DAZ/Poser bone names"),
    ('blender_rigify', "Rigify (Pre-Generate)", "Blender Rigify bones before generation"),
    ('sims_2', "Sims 2", "Sims 2 bone names"),
    ('motion_builder', "Motion Builder", "Motion Builder bone names"),
    ('3ds_max', "3ds Max", "3ds Max bone names"),
    ('bepu', "Bepu IK", "Bepu full body IK bone names"),
    ('mmd_japanese', "MMD Japanese", "MikuMikuDance Japanese bone names"),
    ('mmd_japaneseLR', "MMD Japanese (.L/.R)", "MMD Japanese bones with .L/.R suffixes"),
    ('opensim', "OpenSim", "OpenSimulator avatar bones"),
]

class BonesRenamerPanel(bpy.types.Panel):
    """Creates the Bones Renamer Panel in the 3D View Sidebar"""
    bl_label = "Bones Renamer"
    bl_idname = "OBJECT_PT_bones_renamer"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Rig"

    @classmethod
    def poll(cls, context):
        return context.object is not None and context.object.type == 'ARMATURE'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Mass Rename Bones", icon="ARMATURE_DATA")
        
        layout.prop(context.scene, "bones_renamer_origin_type")
        layout.prop(context.scene, "bones_renamer_destination_type")
        
        layout.operator("object.bones_renamer", text="Rename Bones")

def update_progress(wm, progress, total, message):
    """Safe progress update function"""
    if hasattr(wm, 'progress_begin'):
        if progress == 0:
            wm.progress_begin(0, total)
        wm.progress_update(progress)
        # Blender's progress system doesn't have progress_text in all versions

def main(context):
    """Main function that executes the bone renaming operations."""
    try:
        logger.info("Starting bone renaming process")
        
        if not context.object or context.object.type != 'ARMATURE':
            raise Exception("No armature selected")

        wm = context.window_manager
        total_steps = 4
        
        # Step 1: Prepare armature
        update_progress(wm, 0, total_steps, "Preparing armature...")
        use_international_fonts_display_names_bones()
        unhide_all_armatures()
        
        # Step 2: Rename main bones
        update_progress(wm, 1, total_steps, "Renaming main bones...")
        rename_bones(
            context.scene.bones_renamer_origin_type,
            context.scene.bones_renamer_destination_type
        )
        
        # Step 3: Rename finger bones
        update_progress(wm, 2, total_steps, "Renaming finger bones...")
        rename_finger_bones(
            context.scene.bones_renamer_origin_type,
            context.scene.bones_renamer_destination_type
        )
        
        # Step 4: Finalize
        update_progress(wm, 3, total_steps, "Finalizing...")
        bpy.ops.object.mode_set(mode='POSE')
        bpy.ops.pose.select_all(action='SELECT')
        
        # Finish progress
        if hasattr(wm, 'progress_begin'):
            wm.progress_end()

        logger.info("Bone renaming completed successfully")
        
    except Exception as e:
        logger.error(f"Error during bone renaming: {str(e)}", exc_info=True)
        raise
    finally:
        # Ensure progress is always ended
        if hasattr(wm, 'progress_end'):
            try:
                wm.progress_end()
            except:
                pass

class BonesRenamer(bpy.types.Operator):
    """Mass rename bones for armature conversion"""
    bl_idname = "object.bones_renamer"
    bl_label = "Bones Renamer"
    bl_options = {'REGISTER', 'UNDO'}
    bl_translation_context = '*'

    @classmethod
    def poll(cls, context):
        return (context.object is not None and 
                context.object.type == 'ARMATURE' and 
                context.object.mode == 'OBJECT')

    def execute(self, context):
        try:
            main(context)
            self.report({'INFO'}, "Bones renamed successfully")
            return {'FINISHED'}
        except Exception as e:
            self.report({'ERROR'}, f"Bone rename failed: {str(e)}")
            logger.error("Operator failed", exc_info=True)
            return {'CANCELLED'}

classes = (BonesRenamerPanel, BonesRenamer)

def register():
    """Register all classes and properties."""
    try:
        for cls in classes:
            bpy.utils.register_class(cls)
        
        bpy.types.Scene.bones_renamer_origin_type = bpy.props.EnumProperty(
            items=ORIGIN_TYPES,
            name="Source Rig Type",
            description="Select the source armature naming convention",
            default='mmd_japanese'
        )
        
        bpy.types.Scene.bones_renamer_destination_type = bpy.props.EnumProperty(
            items=ORIGIN_TYPES,
            name="Target Rig Type",
            description="Select the target armature naming convention",
            default='blender_rigify'
        )
        
    except Exception as e:
        logger.error(f"Registration failed: {str(e)}", exc_info=True)
        unregister()
        raise

def unregister():
    """Unregister all classes and clean up properties."""
    try:
        for cls in reversed(classes):
            bpy.utils.unregister_class(cls)
        
        del bpy.types.Scene.bones_renamer_origin_type
        del bpy.types.Scene.bones_renamer_destination_type
        
    except Exception as e:
        logger.error(f"Unregistration failed: {str(e)}", exc_info=True)

if __name__ == "__main__":
    register()