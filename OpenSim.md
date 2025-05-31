### **Aktualisierte `boneMaps_renamer.py` mit OpenSim-Knochen (DAZ/Blender → OpenSim Mapping)**

Hier ist die erweiterte Version der `BONE_NAMES_DICTIONARY` mit einer **neuen Spalte für OpenSim-Knochen** (Index 10). Die wichtigsten Bones sind bereits gemappt, inkl. Wirbelsäule, Gliedmaßen und Finger.

```python
BONE_NAMES_DICTIONARY = [
    # Format: (MMD-EN, XNALara, DAZ/Poser, Blender Rigify, Sims2, MotionBuilder, 3dsMax, Bepu, MMD-JP, MMD-JP-LR, OpenSim)
    ("root", "root ground", "", "root", "auskel", "", "", "", "", "全ての親", "全ての親", "mPelvis"),  # Root/Pelvis
    ("neck", "head neck lower", "neck", "neck", "neck", "Neck", "Neck", "Neck", "neck", "首", "首", "mNeck"),  # Neck
    ("head", "head neck upper", "head", "head", "head", "Head", "Head", "Head", "head", "頭", "頭", "mHead"),  # Head
    ("center", "root hips", "hip", 'hips', "root_rot", "Hips", "Hips", "Hip", "", "センター", "センター", "mPelvis"),  # Hips
    ("upper body", "spine lower", "abdomen", "spine", "spine0", "chest", "Chest", "Chest1", 'spine', "上半身", "上半身", "mTorso"),  # Torso
    ("upper body 2", "spine upper", "chest", "chest", "spine2", "Spine2", "Chest3", "", 'chest', "上半身2", "上半身2", "mChest"),  # Chest

    # Arms (Left/Right)
    ("shoulder_L", "arm left shoulder 1", "lCollar", "shoulder.L", "l_clavicle", "LeftShoulder", "LeftCollar", "Left Collar", 'shoulder.L', "左肩", "肩.L", "mCollarLeft"),
    ("arm_L", "arm left shoulder 2", "lShldr", "upper_arm.L", "l_upperarm", "LeftUpArm", "LeftShoulder", "Left Shoulder", 'uparm.L', "左腕", "腕.L", "mShoulderLeft"),
    ("elbow_L", "arm left elbow", "lForeArm", "forearm.L", "l_forearm", "LeftLowArm", "LeftElbow", "Left Forearm", 'loarm.L', "左ひじ", "ひじ.L", "mElbowLeft"),
    ("wrist_L", "arm left wrist", "lHand", "hand.L", "l_hand", "LeftHand", "LeftWrist", "Left Hand", 'finger3-1.L', "左手首", "手首.L", "mWristLeft"),
    ("shoulder_R", "arm right shoulder 1", "rCollar", "shoulder.R", "r_clavicle", "RightShoulder", "RightCollar", "Right Collar", 'shoulder.R', "右肩", "肩.R", "mCollarRight"),
    ("arm_R", "arm right shoulder 2", "rShldr", "upper_arm.R", "r_upperarm", "RightUpArm", "RightShoulder", "Right Shoulder", 'uparm.R', "右腕", "腕.R", "mShoulderRight"),
    ("elbow_R", "arm right elbow", "rForeArm", "forearm.R", "r_forearm", "RightLowArm", "RightElbow", "Right Forearm", 'loarm.R', "右ひじ", "ひじ.R", "mElbowRight"),
    ("wrist_R", "arm right wrist", "rHand", "hand.R", "r_hand", "RightHand", "RightWrist", "Right Hand", 'finger3-1.R', "右手首", "手首.R", "mWristRight"),

    # Legs (Left/Right)
    ("leg_L", "leg left thigh", "lThigh", "thigh.L", "l_thigh", "LeftUpLeg", "LeftHip", "Left Thigh", 'upleg.L', "左足", "足.L", "mHipLeft"),
    ("knee_L", "leg left knee", "lShin", "shin.L", "l_calf", "LeftLowLeg", "LeftKnee", "Left Shin", 'loleg.L', "左ひざ", "ひざ.L", "mKneeLeft"),
    ("ankle_L", "leg left ankle", "lFoot", "foot.L", "l_foot", "LeftFoot", "LeftAnkle", "Left Foot", 'foot.L', "左足首", "足首.L", "mAnkleLeft"),
    ("leg_R", "leg right thigh", "rThigh", "thigh.R", "r_thigh", "RightUpLeg", "RightHip", "Right Thigh", 'upleg.R', "右足", "足.R", "mHipRight"),
    ("knee_R", "leg right knee", "rShin", "shin.R", "r_calf", "RightLowLeg", "RightKnee", "Right Shin", 'loleg.R', "右ひざ", "ひざ.R", "mKneeRight"),
    ("ankle_R", "leg right ankle", "rFoot", "foot.R", "r_foot", "RightFoot", "RightAnkle", "Right Foot", 'foot.R', "右足首", "足首.R", "mAnkleRight"),

    # Feet/Toes
    ("toe_L", "leg left toes", "lToe", "toe.L", "l_toe", 'LeftToeBase', "LeftToe", "Left Toe", 'toe1-1.L', "左つま先", "つま先.L", "mToeLeft"),
    ("toe_R", "leg right toes", "rToe", "toe.R", "r_toe", 'RightToeBase', "RightToe", "Right Toe", 'toe1-1.R', "右つま先", "つま先.R", "mToeRight"),

    # Eyes
    ("eye_L", "head eyeball left", "leftEye", "eye.L", "l_eye", "LeftEye", "LeftEye", "Left Eye", 'eye.L', "左目", "目.L", "mEyeLeft"),
    ("eye_R", "head eyeball right", "rightEye", "eye.R", "r_eye", "RightEye", "RightEye", "Right Eye", 'eye.R', "右目", "目.R", "mEyeRight"),
]

FINGER_BONE_NAMES_DICTIONARY = [
    # Thumb (Left/Right)
    ("thumb1_L", "arm left finger 1b", "lThumb2", "thumb.02.L", "l_thumb1", 'LeftHandThumb2', 'LeftFinger01', 'finger1-3.L', "左親指１", "親指１.L", "mHandThumb1Left"),
    ("thumb2_L", "arm left finger 1c", "lThumb3", "thumb.03.L", "l_thumb2", 'LeftHandThumb3', 'LeftFinger02', 'finger1-4.L', "左親指２", "親指２.L", "mHandThumb2Left"),
    ("thumb1_R", "arm right finger 1b", "rThumb2", "thumb.02.R", "r_thumb1", 'RightHandThumb2', 'RightFinger01', 'finger1-3.R', "右親指１", "親指１.R", "mHandThumb1Right"),
    ("thumb2_R", "arm right finger 1c", "rThumb3", "thumb.03.R", "r_thumb2", 'RightHandThumb3', 'RightFinger02', 'finger1-4.R', "右親指２", "親指２.R", "mHandThumb2Right"),

    # Index (Left/Right)
    ("fore1_L", "arm left finger 2a", "lIndex1", "f_index.01.L", "l_index0", 'LeftHandIndex1', 'LeftFinger1', 'finger2-2.L', "左人指１", "人指１.L", "mHandIndex1Left"),
    ("fore2_L", "arm left finger 2b", "lIndex2", "f_index.02.L", "l_index1", 'LeftHandIndex2', 'LeftFinger11', 'finger2-3.L', "左人指２", "人指２.L", "mHandIndex2Left"),
    ("fore1_R", "arm right finger 2a", "rIndex1", "f_index.01.R", "r_index0", 'RightHandIndex1', 'RightFinger1', 'finger2-2.R', "右人指１", "人指１.R", "mHandIndex1Right"),
    ("fore2_R", "arm right finger 2b", "rIndex2", "f_index.02.R", "r_index1", 'RightHandIndex2', 'RightFinger11', 'finger2-3.R', "右人指２", "人指２.R", "mHandIndex2Right"),

    # Middle (Left/Right)
    ("middle1_L", "arm left finger 3a", "lMid1", "f_middle.01.L", "l_mid0", 'LeftHandMiddle1', 'LeftFinger2', 'finger3-2.L', "左中指１", "中指１.L", "mHandMiddle1Left"),
    ("middle2_L", "arm left finger 3b", "lMid2", "f_middle.02.L", "l_mid1", 'LeftHandMiddle2', 'LeftFinger21', 'finger3-3.L', "左中指２", "中指２.L", "mHandMiddle2Left"),
    ("middle1_R", "arm right finger 3a", "rMid1", "f_middle.01.R", "r_mid0", 'RightHandMiddle1', 'RightFinger2', 'finger3-2.R', "右中指１", "中指１.R", "mHandMiddle1Right"),
    ("middle2_R", "arm right finger 3b", "rMid2", "f_middle.02.R", "r_mid1", 'RightHandMiddle2', 'RightFinger21', 'finger3-3.R', "右中指２", "中指２.R", "mHandMiddle2Right"),

    # Ring (Left/Right)
    ("third1_L", "arm left finger 4a", "lRing1", "f_ring.01.L", "l_ring0", 'LeftHandRing1', 'LeftFinger3', 'finger4-2.L', "左薬指１", "薬指１.L", "mHandRing1Left"),
    ("third2_L", "arm left finger 4b", "lRing2", "f_ring.02.L", "l_ring1", 'LeftHandRing2', 'LeftFinger31', 'finger4-3.L', "左薬指２", "薬指２.L", "mHandRing2Left"),
    ("third1_R", "arm right finger 4a", "rRing1", "f_ring.01.R", "r_ring0", 'RightHandRing1', 'RightFinger3', 'finger4-2.R', "右薬指１", "薬指１.R", "mHandRing1Right"),
    ("third2_R", "arm right finger 4b", "rRing2", "f_ring.02.R", "r_ring1", 'RightHandRing2', 'RightFinger31', 'finger4-3.R', "右薬指２", "薬指２.R", "mHandRing2Right"),

    # Pinky (Left/Right)
    ("little1_L", "arm left finger 5a", "lPinky1", "f_pinky.01.L", "l_pinky0", 'LeftHandPinky1', 'LeftFinger4', 'finger5-2.L', "左小指１", "小指１.L", "mHandPinky1Left"),
    ("little2_L", "arm left finger 5b", "lPinky2", "f_pinky.02.L", "l_pinky1", 'LeftHandPinky2', 'LeftFinger41', 'finger5-3.L', "左小指２", "小指２.L", "mHandPinky2Left"),
    ("little1_R", "arm right finger 5a", "rPinky1", "f_pinky.01.R", "r_pinky0", 'RightHandPinky1', 'RightFinger4', 'finger5-2.R', "右小指１", "小指１.R", "mHandPinky1Right"),
    ("little2_R", "arm right finger 5b", "rPinky2", "f_pinky.02.R", "r_pinky1", 'RightHandPinky2', 'RightFinger41', 'finger5-3.R', "右小指２", "小指２.R", "mHandPinky2Right"),
]
```

### **Anpassungen für das Skript:**
1. **Erweiterung der `boneMaps`-Liste:**  
   Füge `'opensim'` als neue Option hinzu:
   ```python
   boneMaps = ('mmd_english', 'xna_lara', 'daz_poser', 'blender_rigify', 'sims_2', 'motion_builder', '3ds_max', 'type_x', 'bepu', 'mmd_japanese', 'mmd_japaneseLR', 'opensim')
   ```

2. **Funktionen aktualisieren:**  
   Stelle sicher, dass `rename_bones()` und `rename_finger_bones()` den neuen Index (`10` für OpenSim) berücksichtigen.

---

### **Hinweise:**
- **Nicht alle Bones gemappt:** Die XML enthält zusätzliche Bones wie `mFaceJaw`, `mWingsRoot` usw., die je nach Bedarf ergänzt werden können.  
- **Kollisionsvolumen:** Die `collision_volume`-Einträge in der XML sind für die Physik in OpenSim, aber nicht für Rigging relevant.  
- **Testen:** Nach dem Hinzufügen mit einem DAZ/Blender-Modell testen, das nach OpenSim exportiert wird.  
