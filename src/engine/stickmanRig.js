// ============================================================================
// TYPEFIGHTER — PROCEDURAL STICKMAN SKELETAL RIG & ANIMATION ENGINE
// ============================================================================

class StickmanRig {
  constructor() {
    this.rigData = null;
    this.isLoaded = false;
  }

  async init() {
    try {
      const res = await fetch('assets/sprites/stickman_rig.json');
      this.rigData = await res.json();
      this.isLoaded = true;
      console.log('[StickmanRig] Rig data loaded successfully.');
    } catch (err) {
      console.error('[StickmanRig] Failed to load stickman_rig.json:', err);
    }
  }

  lerp(a, b, t) {
    return a + (b - a) * t;
  }

  lerpAngle(a, b, t) {
    let diff = (b - a) % 360;
    if (diff < -180) diff += 360;
    if (diff > 180) diff -= 360;
    return a + diff * t;
  }

  sampleAnimation(animKey, frame) {
    if (!this.rigData || !this.rigData.animations[animKey]) return null;
    const anim = this.rigData.animations[animKey];
    const kfs = anim.keyframes;
    if (!kfs || kfs.length === 0) return null;

    if (kfs.length === 1 || frame <= kfs[0].frame) return kfs[0];
    if (frame >= kfs[kfs.length - 1].frame) return kfs[kfs.length - 1];

    let kfA = kfs[0];
    let kfB = kfs[kfs.length - 1];
    for (let i = 0; i < kfs.length - 1; i++) {
      if (frame >= kfs[i].frame && frame <= kfs[i + 1].frame) {
        kfA = kfs[i];
        kfB = kfs[i + 1];
        break;
      }
    }

    const span = kfB.frame - kfA.frame;
    const t = span === 0 ? 0 : (frame - kfA.frame) / span;
    const easeT = (1 - Math.cos(t * Math.PI)) / 2;

    const rootOffset = {
      x: this.lerp(kfA.rootOffset.x, kfB.rootOffset.x, easeT),
      y: this.lerp(kfA.rootOffset.y, kfB.rootOffset.y, easeT),
      rotation: this.lerpAngle(kfA.rootOffset.rotation || 0, kfB.rootOffset.rotation || 0, easeT)
    };

    const angles = {};
    for (const jKey of Object.keys(kfA.angles)) {
      const valA = kfA.angles[jKey];
      const valB = (kfB.angles && kfB.angles[jKey] !== undefined) ? kfB.angles[jKey] : valA;
      angles[jKey] = this.lerpAngle(valA, valB, easeT);
    }

    return {
      rootOffset,
      angles,
      fx: (t > 0.4 && t < 0.6) ? kfB.fx : kfA.fx,
      rawT: t
    };
  }

  solveSkeleton(pose, originX, groundY, scale, facing) {
    if (!this.rigData) return null;
    const dims = this.rigData.dimensions;
    const rootOffset = pose.rootOffset;
    const angles = pose.angles;

    const rootX = originX + (rootOffset.x * scale * facing);
    const rootY = groundY + (rootOffset.y * scale);
    const rootRot = (rootOffset.rotation || 0) * (Math.PI / 180) * facing;

    // Torso
    const torsoAngle = (-Math.PI / 2) + (angles.torso * (Math.PI / 180) * facing) + rootRot;
    const torsoEndX = rootX + Math.cos(torsoAngle) * (dims.torsoLength * scale);
    const torsoEndY = rootY + Math.sin(torsoAngle) * (dims.torsoLength * scale);

    // Neck
    const neckAngle = torsoAngle + (angles.neck * (Math.PI / 180) * facing);
    const neckEndX = torsoEndX + Math.cos(neckAngle) * (dims.neckLength * scale);
    const neckEndY = torsoEndY + Math.sin(neckAngle) * (dims.neckLength * scale);

    // Head
    const headAngle = neckAngle + (angles.head * (Math.PI / 180) * facing);
    const headRad = dims.headRadius * scale;
    const headCenterX = neckEndX + Math.cos(headAngle) * headRad;
    const headCenterY = neckEndY + Math.sin(headAngle) * headRad;

    // Torso normal
    const torsoNormX = -Math.sin(torsoAngle);
    const torsoNormY = Math.cos(torsoAngle);
    const shoulderLateral = dims.shoulderWidth * 0.5 * scale * facing;

    // Left Shoulder & Arm
    const lShoulderX = rootX + Math.cos(torsoAngle) * (dims.torsoLength * scale * 0.86) - torsoNormX * shoulderLateral;
    const lShoulderY = rootY + Math.sin(torsoAngle) * (dims.torsoLength * scale * 0.86) - torsoNormY * shoulderLateral;
    const lShoulderAngle = (Math.PI / 2) - (angles.leftShoulder * (Math.PI / 180) * facing);
    const lElbowX = lShoulderX + Math.cos(lShoulderAngle) * (dims.upperArmLength * scale);
    const lElbowY = lShoulderY + Math.sin(lShoulderAngle) * (dims.upperArmLength * scale);
    const lElbowAngle = lShoulderAngle - (angles.leftElbow * (Math.PI / 180) * facing);
    const lHandX = lElbowX + Math.cos(lElbowAngle) * (dims.forearmLength * scale);
    const lHandY = lElbowY + Math.sin(lElbowAngle) * (dims.forearmLength * scale);

    // Right Shoulder & Arm
    const rShoulderX = rootX + Math.cos(torsoAngle) * (dims.torsoLength * scale * 0.86) + torsoNormX * shoulderLateral;
    const rShoulderY = rootY + Math.sin(torsoAngle) * (dims.torsoLength * scale * 0.86) + torsoNormY * shoulderLateral;
    const rShoulderAngle = (Math.PI / 2) - (angles.rightShoulder * (Math.PI / 180) * facing);
    const rElbowX = rShoulderX + Math.cos(rShoulderAngle) * (dims.upperArmLength * scale);
    const rElbowY = rShoulderY + Math.sin(rShoulderAngle) * (dims.upperArmLength * scale);
    const rElbowAngle = rShoulderAngle - (angles.rightElbow * (Math.PI / 180) * facing);
    const rHandX = rElbowX + Math.cos(rElbowAngle) * (dims.forearmLength * scale);
    const rHandY = rElbowY + Math.sin(rElbowAngle) * (dims.forearmLength * scale);

    // Hips
    const hipLateral = dims.hipWidth * 0.5 * scale * facing;
    const lHipX = rootX - torsoNormX * hipLateral;
    const lHipY = rootY - torsoNormY * hipLateral;
    const rHipX = rootX + torsoNormX * hipLateral;
    const rHipY = rootY + torsoNormY * hipLateral;

    // Left Leg
    const lHipAngle = (Math.PI / 2) - (angles.leftHip * (Math.PI / 180) * facing);
    const lKneeX = lHipX + Math.cos(lHipAngle) * (dims.thighLength * scale);
    const lKneeY = lHipY + Math.sin(lHipAngle) * (dims.thighLength * scale);
    const lKneeAngle = lHipAngle + (angles.leftKnee * (Math.PI / 180) * facing);
    const lFootX = lKneeX + Math.cos(lKneeAngle) * (dims.shinLength * scale);
    const lFootY = lKneeY + Math.sin(lKneeAngle) * (dims.shinLength * scale);
    const lFootTipAngle = lKneeAngle - (Math.PI / 2) + (angles.leftFoot * (Math.PI / 180) * facing);
    const lToeX = lFootX + Math.cos(lFootTipAngle) * (dims.footLength * scale);
    const lToeY = lFootY + Math.sin(lFootTipAngle) * (dims.footLength * scale);

    // Right Leg
    const rHipAngle = (Math.PI / 2) - (angles.rightHip * (Math.PI / 180) * facing);
    const rKneeX = rHipX + Math.cos(rHipAngle) * (dims.thighLength * scale);
    const rKneeY = rHipY + Math.sin(rHipAngle) * (dims.thighLength * scale);
    const rKneeAngle = rHipAngle + (angles.rightKnee * (Math.PI / 180) * facing);
    const rFootX = rKneeX + Math.cos(rKneeAngle) * (dims.shinLength * scale);
    const rFootY = rKneeY + Math.sin(rKneeAngle) * (dims.shinLength * scale);
    const rFootTipAngle = rKneeAngle - (Math.PI / 2) + (angles.rightFoot * (Math.PI / 180) * facing);
    const rToeX = rFootX + Math.cos(rFootTipAngle) * (dims.footLength * scale);
    const rToeY = rFootY + Math.sin(rFootTipAngle) * (dims.footLength * scale);

    return {
      root: { x: rootX, y: rootY },
      torsoEnd: { x: torsoEndX, y: torsoEndY },
      neckEnd: { x: neckEndX, y: neckEndY },
      head: { x: headCenterX, y: headCenterY, radius: headRad, angle: headAngle },
      leftShoulder: { x: lShoulderX, y: lShoulderY },
      leftElbow: { x: lElbowX, y: lElbowY },
      leftHand: { x: lHandX, y: lHandY },
      rightShoulder: { x: rShoulderX, y: rShoulderY },
      rightElbow: { x: rElbowX, y: rElbowY },
      rightHand: { x: rHandX, y: rHandY },
      leftHip: { x: lHipX, y: lHipY },
      leftKnee: { x: lKneeX, y: lKneeY },
      leftFoot: { x: lFootX, y: lFootY },
      leftToe: { x: lToeX, y: lToeY },
      rightHip: { x: rHipX, y: rHipY },
      rightKnee: { x: rKneeX, y: rKneeY },
      rightFoot: { x: rFootX, y: rFootY },
      rightToe: { x: rToeX, y: rToeY },
      facing,
      scale
    };
  }

  drawStickman(ctx, skel, theme, alpha = 1.0, isTrail = false, auraLevel = 0) {
    if (!skel || !theme) return;
    ctx.save();
    ctx.globalAlpha = alpha;

    const lw = (theme.lineWidth || 5) * (skel.scale / 1.75);
    ctx.lineWidth = lw;
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    // Aura / Streak Glow
    if (!isTrail) {
      if (auraLevel === 1) { // Fire Streak
        ctx.shadowColor = '#ff5500';
        ctx.shadowBlur = 24;
      } else if (auraLevel === 2) { // Lightning Streak
        ctx.shadowColor = '#00f0ff';
        ctx.shadowBlur = 32;
      } else if (auraLevel >= 3) { // Hyper Overdrive
        ctx.shadowColor = '#ffd700';
        ctx.shadowBlur = 45;
      } else {
        ctx.shadowColor = theme.glow;
        ctx.shadowBlur = theme.glowSize || 18;
      }
    } else {
      ctx.shadowBlur = 0;
    }

    ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : (auraLevel >= 3 ? '#ffe066' : theme.primary);

    const drawBone = (p1, p2, wMult = 1.0) => {
      ctx.beginPath();
      ctx.lineWidth = lw * wMult;
      ctx.moveTo(p1.x, p1.y);
      ctx.lineTo(p2.x, p2.y);
      ctx.stroke();
    };

    // 1. Rear Limbs (Right Arm & Right Leg)
    ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : (theme.secondary || theme.primary);
    drawBone(skel.rightHip, skel.rightKnee, 1.05);
    drawBone(skel.rightKnee, skel.rightFoot, 0.95);
    drawBone(skel.rightFoot, skel.rightToe, 0.85);

    drawBone(skel.rightShoulder, skel.rightElbow, 0.95);
    drawBone(skel.rightElbow, skel.rightHand, 0.85);

    // 2. Spine / Torso
    ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : (auraLevel >= 3 ? '#fff' : theme.primary);
    drawBone(skel.root, skel.torsoEnd, 1.25);
    drawBone(skel.torsoEnd, skel.neckEnd, 0.9);

    // 3. Head & Visor
    ctx.beginPath();
    ctx.arc(skel.head.x, skel.head.y, skel.head.radius, 0, Math.PI * 2);
    ctx.fillStyle = isTrail ? 'rgba(0,0,0,0)' : (auraLevel >= 3 ? '#2a2000' : (theme.headFill || '#001a2c'));
    ctx.fill();
    ctx.stroke();

    // Eye Visor
    if (!isTrail) {
      const eyeOffset = skel.head.radius * 0.45 * skel.facing;
      ctx.fillStyle = auraLevel >= 3 ? '#ffffff' : (theme.eyeColor || '#00ffff');
      ctx.beginPath();
      ctx.arc(skel.head.x + eyeOffset, skel.head.y - skel.head.radius * 0.15, skel.scale * 2.5, 0, Math.PI * 2);
      ctx.fill();
    }

    // 4. Front Limbs (Left Leg & Left Arm)
    ctx.strokeStyle = isTrail ? (theme.trailColor || theme.primary) : (auraLevel >= 3 ? '#ffe066' : theme.primary);
    drawBone(skel.leftHip, skel.leftKnee, 1.15);
    drawBone(skel.leftKnee, skel.leftFoot, 1.0);
    drawBone(skel.leftFoot, skel.leftToe, 0.9);

    drawBone(skel.leftShoulder, skel.leftElbow, 1.05);
    drawBone(skel.leftElbow, skel.leftHand, 0.95);

    // Joints / Knuckles
    if (!isTrail) {
      const joints = [skel.leftHand, skel.rightHand, skel.leftFoot, skel.rightFoot];
      ctx.fillStyle = theme.jointFill || '#ffffff';
      for (const j of joints) {
        ctx.beginPath();
        ctx.arc(j.x, j.y, lw * 0.75, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    ctx.restore();
  }
}

window.stickmanRig = new StickmanRig();
