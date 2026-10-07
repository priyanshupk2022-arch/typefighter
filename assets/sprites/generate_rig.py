import json
import os
import math

def build_stickman_rig():
    rig = {
        "metadata": {
            "name": "TypeFighter Procedural Stickman Skeletal Rig",
            "version": "1.0.0",
            "author": "Stickman Animation Engineer",
            "targetFPS": 60,
            "description": "Procedural 16-joint skeletal animation rig with keyframe martial arts animations, hitboxes, motion trails, and color themes."
        },
        "dimensions": {
            "canvasHeight": 140,
            "headRadius": 14,
            "torsoLength": 40,
            "neckLength": 10,
            "shoulderWidth": 16,
            "upperArmLength": 26,
            "forearmLength": 24,
            "handLength": 7,
            "hipWidth": 16,
            "thighLength": 32,
            "shinLength": 30,
            "footLength": 12,
            "defaultLineWidth": 5
        },
        "hierarchy": {
            "root": "hips",
            "joints": [
                {
                    "id": "hips",
                    "name": "Hips",
                    "parent": None,
                    "description": "Pelvic root joint. Master translation and tilt anchor."
                },
                {
                    "id": "torso",
                    "name": "Torso",
                    "parent": "hips",
                    "length": 40,
                    "description": "Main spine / torso column extending upward from hips."
                },
                {
                    "id": "neck",
                    "name": "Neck",
                    "parent": "torso",
                    "length": 10,
                    "description": "Neck joint linking upper torso to head."
                },
                {
                    "id": "head",
                    "name": "Head",
                    "parent": "neck",
                    "length": 16,
                    "radius": 14,
                    "description": "Head skull with directional eye visor and combat headband."
                },
                {
                    "id": "leftShoulder",
                    "name": "Left Shoulder",
                    "parent": "torso",
                    "offset": [-8, -36],
                    "length": 26,
                    "description": "Left shoulder / upper arm joint (front lead arm)."
                },
                {
                    "id": "leftElbow",
                    "name": "Left Elbow",
                    "parent": "leftShoulder",
                    "length": 24,
                    "description": "Left forearm hinge."
                },
                {
                    "id": "leftHand",
                    "name": "Left Hand",
                    "parent": "leftElbow",
                    "length": 7,
                    "description": "Left fist / striking end-effector."
                },
                {
                    "id": "rightShoulder",
                    "name": "Right Shoulder",
                    "parent": "torso",
                    "offset": [8, -36],
                    "length": 26,
                    "description": "Right shoulder / upper arm joint (rear power arm)."
                },
                {
                    "id": "rightElbow",
                    "name": "Right Elbow",
                    "parent": "rightShoulder",
                    "length": 24,
                    "description": "Right forearm hinge."
                },
                {
                    "id": "rightHand",
                    "name": "Right Hand",
                    "parent": "rightElbow",
                    "length": 7,
                    "description": "Right fist / striking end-effector."
                },
                {
                    "id": "leftHip",
                    "name": "Left Hip",
                    "parent": "hips",
                    "offset": [-8, 0],
                    "length": 32,
                    "description": "Left hip / thigh joint (lead leg)."
                },
                {
                    "id": "leftKnee",
                    "name": "Left Knee",
                    "parent": "leftHip",
                    "length": 30,
                    "description": "Left knee hinge / lower leg."
                },
                {
                    "id": "leftFoot",
                    "name": "Left Foot",
                    "parent": "leftKnee",
                    "length": 12,
                    "description": "Left foot / ankle ground contact."
                },
                {
                    "id": "rightHip",
                    "name": "Right Hip",
                    "parent": "hips",
                    "offset": [8, 0],
                    "length": 32,
                    "description": "Right hip / thigh joint (rear power leg)."
                },
                {
                    "id": "rightKnee",
                    "name": "Right Knee",
                    "parent": "rightHip",
                    "length": 30,
                    "description": "Right knee hinge / lower leg."
                },
                {
                    "id": "rightFoot",
                    "name": "Right Foot",
                    "parent": "rightKnee",
                    "length": 12,
                    "description": "Right foot / ankle ground contact."
                }
            ]
        },
        "themes": {
            "hero": {
                "id": "hero",
                "name": "Hero Cyan Glow",
                "primary": "#00f0ff",
                "secondary": "#0088ff",
                "glow": "rgba(0, 240, 255, 0.8)",
                "glowSize": 18,
                "jointFill": "#ffffff",
                "headFill": "#001a2c",
                "eyeColor": "#00ffff",
                "lineWidth": 5.0,
                "trailColor": "rgba(0, 240, 255, 0.35)",
                "sparkColors": ["#00f0ff", "#ffffff", "#7df9ff", "#00aaff"],
                "auraColor": "rgba(0, 240, 255, 0.25)",
                "impactRingColor": "#00f0ff"
            },
            "enemy_red": {
                "id": "enemy_red",
                "name": "Enemy Red",
                "primary": "#ff2244",
                "secondary": "#ff5500",
                "glow": "rgba(255, 34, 68, 0.85)",
                "glowSize": 18,
                "jointFill": "#ffffff",
                "headFill": "#2c0008",
                "eyeColor": "#ffea00",
                "lineWidth": 5.0,
                "trailColor": "rgba(255, 34, 68, 0.35)",
                "sparkColors": ["#ff2244", "#ff8800", "#ffff44", "#ffffff"],
                "auraColor": "rgba(255, 34, 68, 0.25)",
                "impactRingColor": "#ff2244"
            },
            "enemy_tank": {
                "id": "enemy_tank",
                "name": "Enemy Green Tank",
                "primary": "#00ff66",
                "secondary": "#059669",
                "glow": "rgba(0, 255, 102, 0.8)",
                "glowSize": 24,
                "jointFill": "#ffffff",
                "headFill": "#002611",
                "eyeColor": "#dcfce7",
                "lineWidth": 7.5,
                "trailColor": "rgba(0, 255, 102, 0.35)",
                "sparkColors": ["#00ff66", "#86efac", "#ffffff", "#047857"],
                "auraColor": "rgba(0, 255, 102, 0.25)",
                "impactRingColor": "#00ff66"
            },
            "boss": {
                "id": "boss",
                "name": "Boss Dark Red",
                "primary": "#990022",
                "secondary": "#ff0055",
                "glow": "rgba(255, 0, 85, 0.95)",
                "glowSize": 26,
                "jointFill": "#ff3366",
                "headFill": "#180005",
                "eyeColor": "#ff0033",
                "lineWidth": 6.5,
                "trailColor": "rgba(153, 0, 34, 0.45)",
                "sparkColors": ["#ff0055", "#990022", "#ff3366", "#ffffff"],
                "auraColor": "rgba(255, 0, 85, 0.35)",
                "impactRingColor": "#ff0055"
            }
        },
        "animations": {}
    }

    # Helper function to generate clean keyframe pose
    def make_kf(frame, time_val, root_x, root_y, torso, neck, head,
                l_sh, l_el, l_hd, r_sh, r_el, r_hd,
                l_hp, l_kn, l_ft, r_hp, r_kn, r_ft,
                hips_rot=0, fx=None):
        return {
            "frame": frame,
            "time": round(time_val, 4),
            "rootOffset": {"x": root_x, "y": root_y, "rotation": hips_rot},
            "angles": {
                "torso": torso,
                "neck": neck,
                "head": head,
                "leftShoulder": l_sh,
                "leftElbow": l_el,
                "leftHand": l_hd,
                "rightShoulder": r_sh,
                "rightElbow": r_el,
                "rightHand": r_hd,
                "leftHip": l_hp,
                "leftKnee": l_kn,
                "leftFoot": l_ft,
                "rightHip": r_hp,
                "rightKnee": r_kn,
                "rightFoot": r_ft
            },
            "fx": fx or {}
        }

    # 1. IDLE (Breathing cycle, bobbing torso, relaxed guard stance)
    # 60 frames = 1.0s loop
    idle_kfs = []
    # 5 keyframes for smooth sine interpolation
    for i, (f, t, bob, sway) in enumerate([
        (0,  0.0,    0.0,  5.0),
        (15, 0.25,  -3.5,  3.5),
        (30, 0.5,    0.0,  5.0),
        (45, 0.75,   3.0,  6.5),
        (60, 1.0,    0.0,  5.0)
    ]):
        idle_kfs.append(make_kf(
            frame=f, time_val=t,
            root_x=0, root_y=bob,
            torso=sway, neck=-2, head=-1,
            l_sh=36 + sway*0.5, l_el=76, l_hd=10,
            r_sh=18 + sway*0.3, r_el=86, r_hd=12,
            l_hp=16, l_kn=24, l_ft=-4,
            r_hp=-16, r_kn=20, r_ft=-2
        ))

    rig["animations"]["idle"] = {
        "name": "idle",
        "displayName": "Combat Idle",
        "category": "Stance",
        "durationFrames": 60,
        "durationSeconds": 1.0,
        "fps": 60,
        "loop": True,
        "description": "Breathing cycle with rhythmic torso bobbing and relaxed martial arts guard.",
        "keyframes": idle_kfs
    }

    # 2. PUNCH_JAB: lightning-fast left jab (startup 2 frames, active 1 frame, recovery 3 frames = 6 frames total)
    jab_kfs = [
        # Frame 0: Stance ready
        make_kf(0, 0.0, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2),
        # Frame 2: Startup (coil back, sink hips)
        make_kf(2, 2/60, -3, 1, 2, -1, 0, 18, 98, 15, 20, 88, 14, 14, 26, -3, -14, 22, -1),
        # Frame 3: Active (lightning strike! Fully extended left jab)
        make_kf(3, 3/60, 16, -1, 12, -4, -3, 90, 0, -4, 24, 94, 15, 22, 18, -6, -24, 16, -4,
                fx={"impact": True, "joint": "leftHand", "sparkSize": 1.0, "trail": True, "swoosh": "jab"}),
        # Frame 4: Recovery 1 (rapid retraction starts)
        make_kf(4, 4/60, 10, 0, 9, -3, -2, 65, 40, 5, 22, 90, 14, 19, 21, -5, -20, 18, -3),
        # Frame 5: Recovery 2 (folding arm back towards face)
        make_kf(5, 5/60, 4, 0, 6, -2, -1, 46, 68, 8, 19, 87, 13, 17, 23, -4, -17, 19, -2),
        # Frame 6: Recovery 3 (reset to guard)
        make_kf(6, 6/60, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2)
    ]
    rig["animations"]["punch_jab"] = {
        "name": "punch_jab",
        "displayName": "Lightning Left Jab",
        "category": "Attack",
        "durationFrames": 6,
        "durationSeconds": 0.1,
        "fps": 60,
        "loop": False,
        "hitFrames": [3],
        "description": "Lightning-fast left jab with 2 startup frames, 1 active impact frame, and 3 recovery frames.",
        "keyframes": jab_kfs
    }

    # 3. PUNCH_STRAIGHT: powerful right cross with hip rotation (14 frames)
    straight_kfs = [
        # Frame 0: Stance ready
        make_kf(0, 0.0, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2),
        # Frame 2: Torso coils back, rear shoulder loads
        make_kf(2, 2/60, -4, 1, -2, 0, 1, 40, 80, 12, 5, 95, 14, 14, 26, -3, -18, 24, 0),
        # Frame 4: Max windup, heel raises, hip rotates back
        make_kf(4, 4/60, -8, 2, -10, 2, 3, 44, 86, 14, -20, 112, 16, 12, 28, -2, -22, 28, 5, hips_rot=-8),
        # Frame 6: Core explodes forward, hip whips clockwise
        make_kf(6, 6/60, 14, -1, 12, -4, -2, 32, 92, 10, 65, 36, 4, 20, 20, -6, -26, 14, -6, hips_rot=12),
        # Frame 7: Active Impact! Full right cross extension with complete kinetic drive
        make_kf(7, 7/60, 28, 0, 22, -6, -4, 24, 98, 10, 94, 2, -3, 26, 16, -8, -32, 10, -8, hips_rot=22,
                fx={"impact": True, "joint": "rightHand", "sparkSize": 1.4, "trail": True, "swoosh": "cross", "screenShake": 4}),
        # Frame 9: Hold follow-through / heavy kinetic shock
        make_kf(9, 9/60, 24, 0, 19, -5, -3, 26, 96, 10, 90, 8, 0, 24, 18, -7, -30, 12, -7, hips_rot=18),
        # Frame 11: Retraction begins
        make_kf(11, 11/60, 14, 1, 12, -3, -2, 30, 88, 10, 54, 52, 6, 20, 21, -6, -22, 16, -5, hips_rot=8),
        # Frame 14: Recover back to guard
        make_kf(14, 14/60, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2, hips_rot=0)
    ]
    rig["animations"]["punch_straight"] = {
        "name": "punch_straight",
        "displayName": "Heavy Right Cross",
        "category": "Attack",
        "durationFrames": 14,
        "durationSeconds": 0.233,
        "fps": 60,
        "loop": False,
        "hitFrames": [7],
        "description": "Powerful right cross driving kinetic force through hip rotation and lead foot plant.",
        "keyframes": straight_kfs
    }

    # 4. ROUNDHOUSE_KICK: spinning roundhouse kick with swoosh arc (24 frames)
    roundhouse_kfs = [
        # Frame 0: Stance ready
        make_kf(0, 0.0, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2),
        # Frame 4: Windup / Chamber right leg high tight
        make_kf(4, 4/60, 4, -4, -8, 2, 2, 45, 60, 0, -10, 95, 10, -6, 20, -2, 78, 120, 20, hips_rot=-15),
        # Frame 7: Pivot on standing foot, torso leans back to counterbalance
        make_kf(7, 7/60, 8, -6, -20, 5, 4, 55, 45, -5, -30, 80, 5, -12, 16, 0, 96, 70, 15, hips_rot=25),
        # Frame 9: Active Strike! Leg whips fully extended in high horizontal arc with swoosh!
        make_kf(9, 9/60, 16, -6, -28, 8, 6, 65, 30, -10, -45, 65, 0, -16, 14, 0, 112, 2, 18, hips_rot=55,
                fx={"impact": True, "joint": "rightFoot", "sparkSize": 1.6, "trail": True, "swoosh": "roundhouse_arc", "screenShake": 5}),
        # Frame 12: Arc completion / follow-through slicing forward
        make_kf(12, 12/60, 14, -4, -22, 6, 4, 58, 40, -5, -35, 75, 5, -14, 16, 0, 98, 22, 14, hips_rot=45),
        # Frame 16: Retract & re-chamber leg
        make_kf(16, 16/60, 10, -2, -10, 3, 2, 48, 55, 5, -15, 85, 8, -8, 20, -2, 55, 80, 10, hips_rot=20),
        # Frame 20: Stepping foot down to canvas
        make_kf(20, 20/60, 4, 1, -2, 0, 0, 40, 70, 8, 5, 88, 10, 4, 24, -3, 10, 45, 0, hips_rot=6),
        # Frame 24: Land cleanly back in ready guard
        make_kf(24, 24/60, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2, hips_rot=0)
    ]
    rig["animations"]["roundhouse_kick"] = {
        "name": "roundhouse_kick",
        "displayName": "Spinning Roundhouse Kick",
        "category": "Attack",
        "durationFrames": 24,
        "durationSeconds": 0.4,
        "fps": 60,
        "loop": False,
        "hitFrames": [9],
        "description": "Explosive spinning roundhouse kick with high-speed swoosh arc and counterbalance lean.",
        "keyframes": roundhouse_kfs
    }

    # 5. UPPERCUT: rising uppercut that launches enemies into the air (20 frames)
    uppercut_kfs = [
        # Frame 0: Stance ready
        make_kf(0, 0.0, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2),
        # Frame 3: Deep crouch / duck down, right arm coils low
        make_kf(3, 3/60, 4, 18, 16, -4, -3, 40, 82, 10, -35, 115, 15, 24, 52, 6, -10, 48, 4),
        # Frame 6: Kinetic launch! Feet leave floor, right fist drives upward
        make_kf(6, 6/60, 10, -12, 2, -2, 5, 30, 86, 10, 45, 75, 10, 12, 28, -2, -8, 26, -2),
        # Frame 8: Active Apex Strike! RISING UPPERCUT launches player into air!
        make_kf(8, 8/60, 14, -36, -14, 12, 18, 18, 92, 10, 142, 18, 8, 4, 12, 0, -4, 14, 0,
                fx={"impact": True, "joint": "rightHand", "sparkSize": 1.5, "trail": True, "swoosh": "uppercut_vertical", "screenShake": 6, "launchVertical": True}),
        # Frame 11: Airborne hang at apex
        make_kf(11, 11/60, 12, -42, -10, 10, 15, 22, 88, 10, 138, 22, 10, 6, 15, 0, -6, 16, 0),
        # Frame 15: Descending back down towards canvas
        make_kf(15, 15/60, 6, -14, -2, 2, 4, 32, 78, 10, 75, 60, 10, 12, 22, -2, -12, 20, -2),
        # Frame 18: Touchdown impact absorption with bent knees
        make_kf(18, 18/60, 2, 8, 8, -3, -2, 38, 76, 10, 28, 82, 12, 20, 36, 2, -18, 30, 0),
        # Frame 20: Reset to stance
        make_kf(20, 20/60, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2)
    ]
    rig["animations"]["uppercut"] = {
        "name": "uppercut",
        "displayName": "Rising Dragon Uppercut",
        "category": "Attack",
        "durationFrames": 20,
        "durationSeconds": 0.333,
        "fps": 60,
        "loop": False,
        "hitFrames": [8],
        "description": "Rising vertical uppercut exploding skyward from a deep crouch, launching targets upward.",
        "keyframes": uppercut_kfs
    }

    # 6. AIR_JUGGLE: rapid aerial kick combo in mid-air (32 frames)
    juggle_kfs = [
        # Frame 0: Aerial hover ready
        make_kf(0, 0.0, 0, -42, -5, 2, 3, 30, 80, 10, 20, 85, 12, 20, 45, 5, -15, 40, 0),
        # Frame 4: Strike 1 - Left snap kick in mid-air
        make_kf(4, 4/60, 6, -45, -18, 6, 6, 45, 65, 0, 10, 95, 10, 108, 4, 12, -22, 50, 0,
                fx={"impact": True, "joint": "leftFoot", "sparkSize": 1.1, "trail": True, "swoosh": "juggle_1"}),
        # Frame 8: Twist & switch chamber
        make_kf(8, 8/60, 4, -44, 8, -2, 2, 25, 85, 10, -10, 90, 10, 35, 75, 10, 45, 80, 15, hips_rot=15),
        # Frame 12: Strike 2 - Right spinning roundhouse in air
        make_kf(12, 12/60, 10, -46, -14, 8, 8, 40, 70, 0, -35, 75, 5, -20, 55, 0, 118, 2, 16, hips_rot=45,
                fx={"impact": True, "joint": "rightFoot", "sparkSize": 1.2, "trail": True, "swoosh": "juggle_2"}),
        # Frame 17: Inverted aerial chamber
        make_kf(17, 17/60, 6, -43, 14, -4, 2, 20, 88, 10, 20, 85, 10, 65, 70, 10, -10, 60, 5, hips_rot=-10),
        # Frame 22: Strike 3 - Left downward heel strike
        make_kf(22, 22/60, 8, -44, -20, 8, 6, 50, 50, -5, 15, 88, 10, 85, 6, -8, -25, 48, 0,
                fx={"impact": True, "joint": "leftFoot", "sparkSize": 1.2, "trail": True, "swoosh": "juggle_3"}),
        # Frame 27: Strike 4 - Devastating double kick burst finisher
        make_kf(27, 27/60, 14, -45, -25, 10, 8, 60, 40, -10, -40, 65, 0, 95, 2, 10, 105, 5, 12, hips_rot=30,
                fx={"impact": True, "joint": "rightFoot", "sparkSize": 1.5, "trail": True, "swoosh": "juggle_finisher", "screenShake": 5}),
        # Frame 32: Reset ready for descent
        make_kf(32, 32/60, 0, -42, -5, 2, 3, 30, 80, 10, 20, 85, 12, 20, 45, 5, -15, 40, 0)
    ]
    rig["animations"]["air_juggle"] = {
        "name": "air_juggle",
        "displayName": "Aerial Flurry Juggle",
        "category": "Aerial",
        "durationFrames": 32,
        "durationSeconds": 0.533,
        "fps": 60,
        "loop": False,
        "hitFrames": [4, 12, 22, 27],
        "description": "Rapid aerial kick combo executed in mid-air keeping airborne opponents juggled.",
        "keyframes": juggle_kfs
    }

    # 7. GROUND_SLAM: devastating downward axe kick / slam (28 frames)
    slam_kfs = [
        # Frame 0: Stance ready
        make_kf(0, 0.0, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2),
        # Frame 5: Vault high into air
        make_kf(5, 5/60, 6, -50, -12, 4, 6, 45, 65, 0, -20, 85, 10, -10, 30, 0, 60, 90, 15),
        # Frame 9: High Axe Chamber - right leg reaches skyward over head!
        make_kf(9, 9/60, 10, -56, -26, 10, 12, 60, 45, -5, -35, 75, 5, -20, 25, 0, 155, 0, 20,
                fx={"trail": True, "swoosh": "slam_charge"}),
        # Frame 13: Diving downward with extreme acceleration
        make_kf(13, 13/60, 12, -12, 10, -4, 0, 35, 75, 10, 10, 90, 10, 15, 35, 2, 85, 5, 10,
                fx={"trail": True}),
        # Frame 15: CRASH SLAM! Heel smashes into floor! Earth-shattering shockwave!
        make_kf(15, 15/60, 14, 12, 32, -8, -6, 25, 95, 10, -10, 100, 10, 35, 75, 15, 25, 8, 4,
                fx={"impact": True, "joint": "rightFoot", "sparkSize": 2.0, "trail": True, "swoosh": "axe_slam", "screenShake": 10, "groundShockwave": True}),
        # Frame 19: Impact compression hold
        make_kf(19, 19/60, 12, 10, 28, -6, -5, 28, 90, 10, -5, 95, 10, 32, 68, 12, 22, 12, 2),
        # Frame 24: Pushing up from low impact crouch
        make_kf(24, 24/60, 5, 4, 12, -3, -2, 34, 80, 10, 12, 88, 12, 22, 38, 0, -6, 30, -1),
        # Frame 28: Return to guard stance
        make_kf(28, 28/60, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2)
    ]
    rig["animations"]["ground_slam"] = {
        "name": "ground_slam",
        "displayName": "Meteor Axe Slam",
        "category": "Heavy Attack",
        "durationFrames": 28,
        "durationSeconds": 0.466,
        "fps": 60,
        "loop": False,
        "hitFrames": [15],
        "description": "Devastating downward axe kick slamming from maximum altitude into the canvas with expanding shockwave.",
        "keyframes": slam_kfs
    }

    # 8. HIT_REACTION: head snapback and body recoil when damaged (16 frames)
    hit_kfs = [
        # Frame 0: Stance ready
        make_kf(0, 0.0, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2),
        # Frame 2: Violence of impact! Head snaps back, spine curves back, arms flung open
        make_kf(2, 2/60, -20, -4, -25, -28, -36, -20, 60, 20, -32, 65, 22, 8, 38, 8, -28, 35, 6,
                fx={"hitFlinch": True, "flashRed": True, "screenShake": 4}),
        # Frame 5: Recoil peak & stagger backward
        make_kf(5, 5/60, -32, 2, -18, -16, -20, -10, 72, 15, -22, 75, 18, 2, 44, 12, -22, 42, 8),
        # Frame 9: Stumble recovery / balance check
        make_kf(9, 9/60, -26, 1, -6, -4, -5, 15, 82, 12, 0, 82, 14, 10, 32, 2, -18, 28, 2),
        # Frame 13: Centering weight back onto balls of feet
        make_kf(13, 13/60, -12, 0, 2, -2, -2, 28, 78, 10, 12, 85, 12, 14, 26, -2, -16, 22, 0),
        # Frame 16: Return to guard stance
        make_kf(16, 16/60, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2)
    ]
    rig["animations"]["hit_reaction"] = {
        "name": "hit_reaction",
        "displayName": "Impact Recoil",
        "category": "Damage Reaction",
        "durationFrames": 16,
        "durationSeconds": 0.266,
        "fps": 60,
        "loop": False,
        "hitFrames": [2],
        "description": "Head snapback and body recoil with backward stumble upon taking damage.",
        "keyframes": hit_kfs
    }

    # 9. KNOCKDOWN: falling backward and hitting the canvas floor (38 frames)
    knockdown_kfs = [
        # Frame 0: Hit start
        make_kf(0, 0.0, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2),
        # Frame 4: Launched off feet backward
        make_kf(4, 4/60, -24, -14, -36, -30, -32, -25, 50, 15, -35, 55, 15, 25, 30, 0, 10, 25, 0),
        # Frame 8: Flying horizontally through air
        make_kf(8, 8/60, -52, -8, -65, -15, -15, -45, 35, 10, -50, 40, 10, 45, 20, -5, 30, 15, -5),
        # Frame 12: SLAM ON CANVAS! Back and shoulders crash into mat
        make_kf(12, 12/60, -70, 42, -88, 10, 15, -80, 20, 0, -75, 25, 0, 35, 10, 0, 20, 10, 0,
                fx={"impact": True, "joint": "torso", "groundShockwave": True, "screenShake": 7, "dustPuff": True}),
        # Frame 16: Head bounce off canvas
        make_kf(16, 16/60, -75, 44, -86, 20, 25, -75, 25, 0, -70, 30, 0, 20, 15, 0, 10, 15, 0),
        # Frame 22: Limbs settle flat on the floor
        make_kf(22, 22/60, -78, 46, -90, 0, 0, -85, 10, 0, -80, 15, 0, 5, 5, 0, 0, 5, 0),
        # Frame 30: Breathing faintly while downed
        make_kf(30, 30/60, -78, 45, -89, 0, 0, -85, 10, 0, -80, 15, 0, 5, 5, 0, 0, 5, 0),
        # Frame 38: Rested down
        make_kf(38, 38/60, -78, 46, -90, 0, 0, -85, 10, 0, -80, 15, 0, 5, 5, 0, 0, 5, 0)
    ]
    rig["animations"]["knockdown"] = {
        "name": "knockdown",
        "displayName": "Canvas Knockdown",
        "category": "Damage Reaction",
        "durationFrames": 38,
        "durationSeconds": 0.633,
        "fps": 60,
        "loop": False,
        "hitFrames": [12],
        "description": "Devastating knockdown blowing fighter off feet, crashing back-first onto the canvas with head bounce.",
        "keyframes": knockdown_kfs
    }

    # 10. VICTORY_POSE: high fist pump with glowing aura (48 frames loop)
    victory_kfs = [
        # Frame 0: Transition from stance
        make_kf(0, 0.0, 0, 0, 5, -2, -1, 36, 76, 10, 18, 86, 12, 16, 24, -4, -16, 20, -2),
        # Frame 8: Plants feet wide into champion stance
        make_kf(8, 8/60, 0, 2, 2, 0, 5, 10, 90, 15, 5, 90, 15, 12, 16, 0, -14, 16, 0),
        # Frame 16: Drives right fist high skyward!
        make_kf(16, 16/60, 0, -2, 8, 8, 16, -15, 105, 18, 165, 10, 0, 15, 12, 0, -18, 14, 0,
                fx={"auraActive": True, "victoryShine": True, "sparkBurst": True}),
        # Frame 28: Chest puffed high, radiant fist pumping
        make_kf(28, 28/60, 0, -4, 10, 10, 20, -18, 110, 20, 168, 8, 0, 16, 10, 0, -20, 12, 0,
                fx={"auraActive": True, "auraPulse": 1.2}),
        # Frame 40: Gentle breath at apex
        make_kf(40, 40/60, 0, -2, 8, 8, 18, -15, 105, 18, 164, 12, 0, 15, 12, 0, -18, 14, 0,
                fx={"auraActive": True, "auraPulse": 1.0}),
        # Frame 48: Victory cycle loop
        make_kf(48, 48/60, 0, -4, 10, 10, 20, -18, 110, 20, 168, 8, 0, 16, 10, 0, -20, 12, 0,
                fx={"auraActive": True, "auraPulse": 1.2})
    ]
    rig["animations"]["victory_pose"] = {
        "name": "victory_pose",
        "displayName": "Champion Victory Pump",
        "category": "Victory",
        "durationFrames": 48,
        "durationSeconds": 0.8,
        "fps": 60,
        "loop": True,
        "description": "Triumphant victory pose with high skyward fist pump and pulsating radiant aura.",
        "keyframes": victory_kfs
    }

    return rig

if __name__ == "__main__":
    rig = build_stickman_rig()
    out_path = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\sprites\stickman_rig.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(rig, f, indent=2)
    print(f"Successfully generated {out_path} with {len(rig['animations'])} animations and {len(rig['hierarchy']['joints'])} joints.")
