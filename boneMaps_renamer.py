import bpy

# Bone name mappings for various 3D software formats
# Format: [MMD English, XNALara, DAZ/Poser, Blender Rigify, Sims 2, Motion Builder, 3ds Max, Bepu, MMD Japanese, MMD Japanese LR, OpenSim]
# Version: 1.0.1 (Fixed missing bones and removed type_x)

BONE_NAMES_DICTIONARY = [
    # Root/Torso
    ("root", "root ground", "", "root", "auskel", "", "", "", "", "全ての親", "全ての親", "mPelvis"),
    ("neck", "head neck lower", "neck", "neck", "neck", "Neck", "Neck", "Neck", "neck", "首", "首", "mNeck"),
    ("head", "head neck upper", "head", "head", "head", "Head", "Head", "Head", "head", "頭", "頭", "mHead"),
    ("center", "root hips", "hip", 'hips', "root_rot", "Hips", "Hips", "Hip", "", "センター", "センター", "mPelvis"),
    
    # Spine (added missing spine bones)
    ("spine", "spine lower", "spine0", "spine", "spine0", "Spine", "Spine", "Spine0", "spine", "上半身", "上半身", "mSpine1"),
    ("spine1", "spine middle", "spine1", "spine.001", "spine1", "Spine1", "Spine1", "Spine1", "spine1", "上半身1", "上半身1", "mSpine2"),
    ("spine2", "spine upper", "spine2", "spine.002", "spine2", "Spine2", "Spine2", "Spine2", "spine2", "上半身2", "上半身2", "mSpine3"),
    ("chest", "chest", "chest", "chest", "chest", "Chest", "Chest", "Chest", "chest", "胸", "胸", "mSpine4"),
    ("upper body", "spine upper", "abdomen", "spine.003", "spine3", "chest", "Chest2", "Chest1", "upperbody", "上半身", "上半身", "mTorso"),
    ("upper body 2", "spine chest", "chest", "spine.004", "spine4", "Spine3", "Chest3", "Chest2", "upperbody2", "上半身3", "上半身3", "mChest"),
    ("lower body", "pelvis", "hip", "pelvis", "pelvis", "Pelvis", "Pelvis", "Hip", "lowerbody", "下半身", "下半身", "mPelvis"),

    # Left Arm
    ("shoulder_L", "arm left shoulder 1", "lCollar", "shoulder.L", "l_clavicle", "LeftShoulder", "LeftCollar", "Left Collar", 'shoulder.L', "左肩", "肩.L", "mCollarLeft"),
    ("arm_L", "arm left shoulder 2", "lShldr", "upper_arm.L", "l_upperarm", "LeftUpArm", "LeftShoulder", "Left Shoulder", 'uparm.L', "左腕", "腕.L", "mShoulderLeft"),
    ("elbow_L", "arm left elbow", "lForeArm", "forearm.L", "l_forearm", "LeftLowArm", "LeftElbow", "Left Forearm", 'loarm.L', "左ひじ", "ひじ.L", "mElbowLeft"),
    ("wrist_L", "arm left wrist", "lHand", "hand.L", "l_hand", "LeftHand", "LeftWrist", "Left Hand", 'finger3-1.L', "左手首", "手首.L", "mWristLeft"),

    # Right Arm
    ("shoulder_R", "arm right shoulder 1", "rCollar", "shoulder.R", "r_clavicle", "RightShoulder", "RightCollar", "Right Collar", 'shoulder.R', "右肩", "肩.R", "mCollarRight"),
    ("arm_R", "arm right shoulder 2", "rShldr", "upper_arm.R", "r_upperarm", "RightUpArm", "RightShoulder", "Right Shoulder", 'uparm.R', "右腕", "腕.R", "mShoulderRight"),
    ("elbow_R", "arm right elbow", "rForeArm", "forearm.R", "r_forearm", "RightLowArm", "RightElbow", "Right Forearm", 'loarm.R', "右ひじ", "ひじ.R", "mElbowRight"),
    ("wrist_R", "arm right wrist", "rHand", "hand.R", "r_hand", "RightHand", "RightWrist", "Right Hand", 'finger3-1.R', "右手首", "手首.R", "mWristRight"),

    # Left Leg
    ("leg_L", "leg left thigh", "lThigh", "thigh.L", "l_thigh", "LeftUpLeg", "LeftHip", "Left Thigh", 'upleg.L', "左足", "足.L", "mHipLeft"),
    ("knee_L", "leg left knee", "lShin", "shin.L", "l_calf", "LeftLowLeg", "LeftKnee", "Left Shin", 'loleg.L', "左ひざ", "ひざ.L", "mKneeLeft"),
    ("ankle_L", "leg left ankle", "lFoot", "foot.L", "l_foot", "LeftFoot", "LeftAnkle", "Left Foot", 'foot.L', "左足首", "足首.L", "mAnkleLeft"),

    # Right Leg
    ("leg_R", "leg right thigh", "rThigh", "thigh.R", "r_thigh", "RightUpLeg", "RightHip", "Right Thigh", 'upleg.R', "右足", "足.R", "mHipRight"),
    ("knee_R", "leg right knee", "rShin", "shin.R", "r_calf", "RightLowLeg", "RightKnee", "Right Shin", 'loleg.R', "右ひざ", "ひざ.R", "mKneeRight"),
    ("ankle_R", "leg right ankle", "rFoot", "foot.R", "r_foot", "RightFoot", "RightAnkle", "Right Foot", 'foot.R', "右足首", "足首.R", "mAnkleRight"),

    # Feet/Toes
    ("toe_L", "leg left toes", "lToe", "toe.L", "l_toe", 'LeftToeBase', "LeftToe", "Left Toe", 'toe1-1.L', "左つま先", "つま先.L", "mToeLeft"),
    ("toe_R", "leg right toes", "rToe", "toe.R", "r_toe", 'RightToeBase', "RightToe", "Right Toe", 'toe1-1.R', "右つま先", "つま先.R", "mToeRight"),

    # Eyes
    ("eye_L", "head eyeball left", "leftEye", "eye.L", "l_eye", "LeftEye", "LeftEye", "Left Eye", 'eye.L', "左目", "目.L", "mEyeLeft"),
    ("eye_R", "head eyeball right", "rightEye", "eye.R", "r_eye", "RightEye", "RightEye", "Right Eye", 'eye.R', "右目", "目.R", "mEyeRight"),

    # Face (added key face bones)
    ("jaw", "head jaw", "jaw", "jaw_master", "", "Jaw", "Jaw", "", "", "あご", "あご", "mFaceJaw"),
    ("tongue", "head tongue", "tongue", "tongue", "", "Tongue", "Tongue", "", "", "舌", "舌", "mFaceTongueBase"),
    
    # Tail (added missing tail bones)
    ("tail1", "tail 1", "tail1", "tail.001", "", "", "", "", "", "尾１", "尾１", "mTail1"),
    ("tail2", "tail 2", "tail2", "tail.002", "", "", "", "", "", "尾２", "尾２", "mTail2"),
    ("tail3", "tail 3", "tail3", "tail.003", "", "", "", "", "", "尾３", "尾３", "mTail3"),
    ("tail4", "tail 4", "tail4", "tail.004", "", "", "", "", "", "尾４", "尾４", "mTail4"),
    ("tail5", "tail 5", "tail5", "tail.005", "", "", "", "", "", "尾５", "尾５", "mTail5"),
    ("tail6", "tail 6", "tail6", "tail.006", "", "", "", "", "", "尾６", "尾６", "mTail6"),
]

FINGER_BONE_NAMES_DICTIONARY = [
    # Left Hand
    ("thumb1_L", "arm left finger 1b", "lThumb2", "thumb.02.L", "l_thumb1", 'LeftHandThumb2', 'LeftFinger01', 'finger1-3.L', "左親指１", "親指１.L", "mHandThumb1Left"),
    ("thumb2_L", "arm left finger 1c", "lThumb3", "thumb.03.L", "l_thumb2", 'LeftHandThumb3', 'LeftFinger02', 'finger1-4.L', "左親指２", "親指２.L", "mHandThumb2Left"),
    ("thumb3_L", "arm left finger 1d", "lThumb4", "thumb.04.L", "l_thumb3", 'LeftHandThumb4', 'LeftFinger03', 'finger1-5.L', "左親指３", "親指３.L", "mHandThumb3Left"),
    ("fore1_L", "arm left finger 2a", "lIndex1", "f_index.01.L", "l_index0", 'LeftHandIndex1', 'LeftFinger1', 'finger2-2.L', "左人指１", "人指１.L", "mHandIndex1Left"),
    ("fore2_L", "arm left finger 2b", "lIndex2", "f_index.02.L", "l_index1", 'LeftHandIndex2', 'LeftFinger11', 'finger2-3.L', "左人指２", "人指２.L", "mHandIndex2Left"),
    ("fore3_L", "arm left finger 2c", "lIndex3", "f_index.03.L", "l_index2", 'LeftHandIndex3', 'LeftFinger12', 'finger2-4.L', "左人指３", "人指３.L", "mHandIndex3Left"),
    ("middle1_L", "arm left finger 3a", "lMid1", "f_middle.01.L", "l_mid0", 'LeftHandMiddle1', 'LeftFinger2', 'finger3-2.L', "左中指１", "中指１.L", "mHandMiddle1Left"),
    ("middle2_L", "arm left finger 3b", "lMid2", "f_middle.02.L", "l_mid1", 'LeftHandMiddle2', 'LeftFinger21', 'finger3-3.L', "左中指２", "中指２.L", "mHandMiddle2Left"),
    ("middle3_L", "arm left finger 3c", "lMid3", "f_middle.03.L", "l_mid2", 'LeftHandMiddle3', 'LeftFinger22', 'finger3-4.L', "左中指３", "中指３.L", "mHandMiddle3Left"),
    ("third1_L", "arm left finger 4a", "lRing1", "f_ring.01.L", "l_ring0", 'LeftHandRing1', 'LeftFinger3', 'finger4-2.L', "左薬指１", "薬指１.L", "mHandRing1Left"),
    ("third2_L", "arm left finger 4b", "lRing2", "f_ring.02.L", "l_ring1", 'LeftHandRing2', 'LeftFinger31', 'finger4-3.L', "左薬指２", "薬指２.L", "mHandRing2Left"),
    ("third3_L", "arm left finger 4c", "lRing3", "f_ring.03.L", "l_ring2", 'LeftHandRing3', 'LeftFinger32', 'finger4-4.L', "左薬指３", "薬指３.L", "mHandRing3Left"),
    ("little1_L", "arm left finger 5a", "lPinky1", "f_pinky.01.L", "l_pinky0", 'LeftHandPinky1', 'LeftFinger4', 'finger5-2.L', "左小指１", "小指１.L", "mHandPinky1Left"),
    ("little2_L", "arm left finger 5b", "lPinky2", "f_pinky.02.L", "l_pinky1", 'LeftHandPinky2', 'LeftFinger41', 'finger5-3.L', "左小指２", "小指２.L", "mHandPinky2Left"),
    ("little3_L", "arm left finger 5c", "lPinky3", "f_pinky.03.L", "l_pinky2", 'LeftHandPinky3', 'LeftFinger42', 'finger5-4.L', "左小指３", "小指３.L", "mHandPinky3Left"),
    ("thumb0_L", "arm left finger 1a", "lThumb1", "thumb.01.L", "l_thumb0", 'LeftHandThumb1', 'LeftFinger0', 'finger1-2.L', "左親指0", "親指0.L", ""),

    # Right Hand
    ("thumb1_R", "arm right finger 1b", "rThumb2", "thumb.02.R", "r_thumb1", 'RightHandThumb2', 'RightFinger01', 'finger1-3.R', "右親指１", "親指１.R", "mHandThumb1Right"),
    ("thumb2_R", "arm right finger 1c", "rThumb3", "thumb.03.R", "r_thumb2", 'RightHandThumb3', 'RightFinger02', 'finger1-4.R', "右親指２", "親指２.R", "mHandThumb2Right"),
    ("thumb3_R", "arm right finger 1d", "rThumb4", "thumb.04.R", "r_thumb3", 'RightHandThumb4', 'RightFinger03', 'finger1-5.R', "右親指３", "親指３.R", "mHandThumb3Right"),
    ("fore1_R", "arm right finger 2a", "rIndex1", "f_index.01.R", "r_index0", 'RightHandIndex1', 'RightFinger1', 'finger2-2.R', "右人指１", "人指１.R", "mHandIndex1Right"),
    ("fore2_R", "arm right finger 2b", "rIndex2", "f_index.02.R", "r_index1", 'RightHandIndex2', 'RightFinger11', 'finger2-3.R', "右人指２", "人指２.R", "mHandIndex2Right"),
    ("fore3_R", "arm right finger 2c", "rIndex3", "f_index.03.R", "r_index2", 'RightHandIndex3', 'RightFinger12', 'finger2-4.R', "右人指３", "人指３.R", "mHandIndex3Right"),
    ("middle1_R", "arm right finger 3a", "rMid1", "f_middle.01.R", "r_mid0", 'RightHandMiddle1', 'RightFinger2', 'finger3-2.R', "右中指１", "中指１.R", "mHandMiddle1Right"),
    ("middle2_R", "arm right finger 3b", "rMid2", "f_middle.02.R", "r_mid1", 'RightHandMiddle2', 'RightFinger21', 'finger3-3.R', "右中指２", "中指２.R", "mHandMiddle2Right"),
    ("middle3_R", "arm right finger 3c", "rMid3", "f_middle.03.R", "r_mid2", 'RightHandMiddle3', 'RightFinger22', 'finger3-4.R', "右中指３", "中指３.R", "mHandMiddle3Right"),
    ("third1_R", "arm right finger 4a", "rRing1", "f_ring.01.R", "r_ring0", 'RightHandRing1', 'RightFinger3', 'finger4-2.R', "右薬指１", "薬指１.R", "mHandRing1Right"),
    ("third2_R", "arm right finger 4b", "rRing2", "f_ring.02.R", "r_ring1", 'RightHandRing2', 'RightFinger31', 'finger4-3.R', "右薬指２", "薬指２.R", "mHandRing2Right"),
    ("third3_R", "arm right finger 4c", "rRing3", "f_ring.03.R", "r_ring2", 'RightHandRing3', 'RightFinger32', 'finger4-4.R', "右薬指３", "薬指３.R", "mHandRing3Right"),
    ("little1_R", "arm right finger 5a", "rPinky1", "f_pinky.01.R", "r_pinky0", 'RightHandPinky1', 'RightFinger4', 'finger5-2.R', "右小指１", "小指１.R", "mHandPinky1Right"),
    ("little2_R", "arm right finger 5b", "rPinky2", "f_pinky.02.R", "r_pinky1", 'RightHandPinky2', 'RightFinger41', 'finger5-3.R', "右小指２", "小指２.R", "mHandPinky2Right"),
    ("little3_R", "arm right finger 5c", "rPinky3", "f_pinky.03.R", "r_pinky2", 'RightHandPinky3', 'RightFinger42', 'finger5-4.R', "右小指３", "小指３.R", "mHandPinky3Right"),
    ("thumb0_R", "arm right finger 1a", "rThumb1", "thumb.01.R", "r_thumb0", 'RightHandThumb1', 'RightFinger0', 'finger1-2.R', "右親指0", "親指0.R", ""),
]

def use_international_fonts_display_names_bones():
    """Enable international fonts and show bone names"""
    try:
        bpy.context.preferences.view.use_international_fonts = True
        if bpy.context.object and bpy.context.object.type == 'ARMATURE':
            bpy.context.object.data.show_names = True
    except AttributeError as e:
        print(f"Error in settings: {e}")

def unhide_all_armatures():
    """Unhide all armatures in the scene"""
    try:
        for o in bpy.context.scene.objects:
            if o.type == 'ARMATURE':
                o.hide_set(False)
    except Exception as e:
        print(f"Error showing armatures: {e}")

def rename_bones(boneMap1, boneMap2):
    """Mass rename bones between different naming conventions"""
    boneMaps = (
        'mmd_english', 'xna_lara', 'daz_poser', 'blender_rigify', 
        'sims_2', 'motion_builder', '3ds_max', 'bepu', 
        'mmd_japanese', 'mmd_japaneseLR', 'opensim'
    )
    
    try:
        boneMap1_index = boneMaps.index(boneMap1)
        boneMap2_index = boneMaps.index(boneMap2)
    except ValueError as e:
        print(f"Invalid bone map specified: {e}")
        return
    
    # Ensure we're in object mode
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE':
        for bone_entry in BONE_NAMES_DICTIONARY:
            src_name = bone_entry[boneMap1_index]
            tgt_name = bone_entry[boneMap2_index]
            
            if src_name and tgt_name and src_name in bpy.context.active_object.data.bones:
                try:
                    bpy.context.active_object.data.bones[src_name].name = tgt_name
                except Exception as e:
                    print(f"Error renaming {src_name} to {tgt_name}: {e}")

def rename_finger_bones(boneMap1, boneMap2):
    """Mass rename finger bones between different naming conventions"""
    boneMaps = (
        'mmd_english', 'xna_lara', 'daz_poser', 'blender_rigify', 
        'sims_2', 'motion_builder', '3ds_max', 'bepu', 
        'mmd_japanese', 'mmd_japaneseLR', 'opensim'
    )
    
    try:
        boneMap1_index = boneMaps.index(boneMap1)
        boneMap2_index = boneMaps.index(boneMap2)
    except ValueError as e:
        print(f"Invalid bone map specified: {e}")
        return
    
    # Ensure we're in object mode
    if bpy.context.active_object and bpy.context.active_object.mode != 'OBJECT':
        bpy.ops.object.mode_set(mode='OBJECT')
    
    if bpy.context.active_object and bpy.context.active_object.type == 'ARMATURE':
        for bone_entry in FINGER_BONE_NAMES_DICTIONARY:
            src_name = bone_entry[boneMap1_index]
            tgt_name = bone_entry[boneMap2_index]
            
            if src_name and tgt_name and src_name in bpy.context.active_object.data.bones:
                try:
                    bpy.context.active_object.data.bones[src_name].name = tgt_name
                except Exception as e:
                    print(f"Error renaming {src_name} to {tgt_name}: {e}")