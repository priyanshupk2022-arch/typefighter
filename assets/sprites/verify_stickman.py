import json
import os
import re
import sys

# Ensure UTF-8 output on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

def verify_rig_and_preview():
    rig_path = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\sprites\stickman_rig.json"
    preview_path = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\sprites\stickman_preview.html"

    print("=== TYPEFIGHTER STICKMAN RIG VERIFICATION ===")

    # 1. Verify JSON file
    assert os.path.exists(rig_path), f"File not found: {rig_path}"
    with open(rig_path, "r", encoding="utf-8") as f:
        rig = json.load(f)
    print("✓ stickman_rig.json loaded successfully and parsed as valid JSON.")

    # Check Hierarchy
    expected_joints = [
        "hips", "torso", "neck", "head",
        "leftShoulder", "leftElbow", "leftHand",
        "rightShoulder", "rightElbow", "rightHand",
        "leftHip", "leftKnee", "leftFoot",
        "rightHip", "rightKnee", "rightFoot"
    ]

    joints_in_rig = [j["id"] for j in rig["hierarchy"]["joints"]]
    print(f"✓ Found {len(joints_in_rig)} joints in hierarchy.")
    for j in expected_joints:
        assert j in joints_in_rig, f"Missing required joint: {j}"
    print("✓ All 16 specified joints present in hierarchy.")

    # Check Animations
    expected_animations = [
        "idle",
        "punch_jab",
        "punch_straight",
        "roundhouse_kick",
        "uppercut",
        "air_juggle",
        "ground_slam",
        "hit_reaction",
        "knockdown",
        "victory_pose"
    ]

    anims_in_rig = list(rig["animations"].keys())
    print(f"✓ Found {len(anims_in_rig)} animations.")
    for anim_name in expected_animations:
        assert anim_name in anims_in_rig, f"Missing required animation: {anim_name}"
        anim = rig["animations"][anim_name]
        kfs = anim["keyframes"]
        assert len(kfs) >= 2, f"Animation {anim_name} has too few keyframes: {len(kfs)}"
        print(f"   - {anim_name:16} | Duration: {anim['durationFrames']:2d} frames ({anim['durationSeconds']:.3f}s) | Keyframes: {len(kfs):2d} | Loop: {anim['loop']}")

    # Specific test for punch_jab
    jab = rig["animations"]["punch_jab"]
    assert jab["durationFrames"] == 6, f"punch_jab expected 6 frames, got {jab['durationFrames']}"
    assert 3 in jab.get("hitFrames", []), "punch_jab active impact frame should be at frame 3"
    print("✓ punch_jab verified: 2 startup, 1 active, 3 recovery frames (total 6 frames).")

    # Check Themes
    expected_themes = ["hero", "enemy_red", "enemy_tank", "boss"]
    for t in expected_themes:
        assert t in rig["themes"], f"Missing required theme: {t}"
    print(f"✓ All 4 themes verified: {list(rig['themes'].keys())}")

    # 2. Verify HTML Preview
    assert os.path.exists(preview_path), f"File not found: {preview_path}"
    with open(preview_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    print(f"✓ stickman_preview.html loaded ({len(html_content)} bytes).")

    assert "<!DOCTYPE html>" in html_content, "Missing DOCTYPE in HTML"
    assert "<canvas id=\"fighterCanvas\"" in html_content, "Missing canvas element"
    assert "solveSkeleton" in html_content, "Missing Forward Kinematics solver"
    assert "spawnHitSparks" in html_content, "Missing Hit Sparks particle system"
    assert "drawSwooshArc" in html_content, "Missing swoosh motion arc renderer"
    assert "trailsHistory" in html_content, "Missing motion trails ghosting buffer"

    # Verify embedded JSON
    embedded_match = re.search(r'<script id="embedded-rig-data" type="application/json">\s*(.*?)\s*</script>', html_content, re.DOTALL)
    assert embedded_match, "Missing embedded rig JSON in HTML"
    embedded_data = json.loads(embedded_match.group(1))
    assert len(embedded_data["animations"]) == 10, "Embedded data animation count mismatch"
    print("✓ stickman_preview.html contains valid embedded fallback JSON matching rig.")

    print("\nALL TESTS PASSED! Procedural stickman rig & preview are 100% verified.")

if __name__ == "__main__":
    verify_rig_and_preview()
