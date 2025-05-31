# Blender Bone Renamer Add-on  
**Massenumbenennung von Knochen für Rig-Konvertierungen**

Es sind noch ein paar Fehler enthalten. There are still a few errors.

![Demo](https://github.com/ManfredAabye/bones_renamer/blob/master/Blender.jpg) *(Screenshot)* 

## 📋 Übersicht  
Dieses Add-on ermöglicht die **automatische Umbenennung von Armature-Knochen** zwischen verschiedenen 3D-Software-Standards. Ideal für:  
- Rigging-Wechsel (z.B. DAZ → Rigify)  
- Animationstransfer zwischen Formaten  
- Vorbereitung für Game-Engines  

## ✨ Features  
- Unterstützt **11+ Armature-Typen**  
- Inklusive **Finger- und Gesichtsknochen**  
- Blender 4.4+ kompatibel  
- Einfache Bedienung via Sidebar-Panel  

## 🛠 Unterstützte Systeme  
| Format            | Beispiel-Knochen       |  
|-------------------|------------------------|  
| **MMD (Englisch)**  | `shoulder_L`, `arm_L`  |  
| **XNALara**        | `arm left shoulder 1`  |  
| **DAZ/Poser**      | `lShldr`, `rThigh`     |  
| **Rigify (Pre-Gen)**| `upper_arm.L`          |  
| **OpenSim**        | `mShoulderLeft`        |  
| *...und 6 weitere* |                        |  

## 🚀 Installation  
1. Lade die neueste `.zip` von [Releases]() herunter  
2. In Blender:  
   ```
   Edit → Preferences → Add-ons → Install...  
   ```
3. Aktivieren unter **"Rigging: Bone Renamer"**

## 🖥 Bedienung  
1. Armature auswählen  
2. Quell- und Zielformat wählen:  
   ![Panel](https://via.placeholder.com/400x200?text=UI+Panel)  
3. **"Rename Bones"** klicken  

## 🌟 Anwendungsfälle  
- **OpenSim-Vorbereitung**:  
  ```DAZ → OpenSim``` (Automatische Umwandlung zu `mShoulderLeft` etc.)  
- **MMD zu Rigify**: Kompatibilität für Animationen  
- **Unity/Unreal Engine**: Standardisierung von Knochennamen  

## 📜 Lizenz  
**"Kein Stress, alles frei!"-Lizenz**  
- Kommerzielle Nutzung erlaubt  
- Keine Haftung  
- Bei Nutzung: Credits erwünscht (aber nicht verpflichtend)  

---

💡 **Tipp**: Für Gesichtsknochen (OpenSim) die [Avastar-Blender-Erweiterung](http://avastar.online) verwenden.  
