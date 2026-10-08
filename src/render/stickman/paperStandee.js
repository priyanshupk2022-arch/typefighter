// Keyboard Warrior Stickman - Authentic Crumpled Notebook Paper Cutout Standee System
import * as THREE from 'three';

export class PaperStandee {
  constructor(isHero = true, scene) {
    this.isHero = isHero;
    this.scene = scene;
    this.group = new THREE.Group();
    
    // Transform state
    this.x = isHero ? -1.8 : 1.8;
    this.y = 0; // vertical height (for air launches)
    this.z = 0;
    this.facing = isHero ? 1 : -1;
    this.vy = 0;
    this.isAirborne = false;
    
    // Animation state
    this.currentPose = 'idle'; // idle, run, jab, punch, kick, launcher, juggle, slam, hurt, knockdown
    this.animTime = 0;
    this.hitStopFrames = 0;
    this.health = 100;
    this.maxHealth = 100;

    // Load authentic extracted cutout textures
    const textureLoader = new THREE.TextureLoader();
    this.textures = {
      hero_guard: textureLoader.load('assets/textures/paper/standee_hero_guard.png'),
      hero_kick: textureLoader.load('assets/textures/paper/standee_hero_kick.png'),
      enemy_guard: textureLoader.load('assets/textures/paper/standee_enemy_guard.png'),
      enemy_hit: textureLoader.load('assets/textures/paper/standee_enemy_hit.png'),
      enemy_knockdown: textureLoader.load('assets/textures/paper/standee_enemy_knockdown.png'),
      enemy_jump: textureLoader.load('assets/textures/paper/standee_enemy_jump.png')
    };

    // Build the 3D Billboard mesh with paper cutout material
    const geometry = new THREE.PlaneGeometry(2.4, 2.6);
    this.material = new THREE.MeshBasicMaterial({
      map: isHero ? this.textures.hero_guard : this.textures.enemy_guard,
      transparent: true,
      alphaTest: 0.05,
      side: THREE.DoubleSide
    });

    this.mesh = new THREE.Mesh(geometry, this.material);
    this.mesh.position.y = 1.3;
    this.group.add(this.mesh);

    // Realistic Elliptical Drop Shadow onto the 3D Desk/Keyboard
    const shadowGeo = new THREE.PlaneGeometry(1.6, 0.6);
    const shadowCanvas = document.createElement('canvas');
    shadowCanvas.width = 128;
    shadowCanvas.height = 64;
    const sCtx = shadowCanvas.getContext('2d');
    const grad = sCtx.createRadialGradient(64, 32, 0, 64, 32, 56);
    grad.addColorStop(0, 'rgba(0, 0, 0, 0.65)');
    grad.addColorStop(0.6, 'rgba(15, 10, 5, 0.35)');
    grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
    sCtx.fillStyle = grad;
    sCtx.fillRect(0, 0, 128, 64);

    const shadowTex = new THREE.CanvasTexture(shadowCanvas);
    const shadowMat = new THREE.MeshBasicMaterial({
      map: shadowTex,
      transparent: true,
      opacity: 0.85,
      depthWrite: false
    });
    this.shadowMesh = new THREE.Mesh(shadowGeo, shadowMat);
    this.shadowMesh.rotation.x = -Math.PI / 2;
    this.shadowMesh.position.y = 0.02;
    this.group.add(this.shadowMesh);

    this.updatePosition();
    this.scene.add(this.group);
  }

  setPose(poseName, duration = 0.25) {
    if (this.currentPose === 'knockdown' && poseName !== 'idle') return;
    this.currentPose = poseName;
    this.animTime = duration;

    if (this.isHero) {
      if (poseName === 'kick' || poseName === 'launcher') {
        this.material.map = this.textures.hero_kick;
      } else {
        this.material.map = this.textures.hero_guard;
      }
    } else {
      if (poseName === 'hurt') {
        this.material.map = this.textures.enemy_hit;
      } else if (poseName === 'knockdown') {
        this.material.map = this.textures.enemy_knockdown;
      } else if (poseName === 'air') {
        this.material.map = this.textures.enemy_jump;
      } else {
        this.material.map = this.textures.enemy_guard;
      }
    }
    this.material.needsUpdate = true;
  }

  launchIntoAir(verticalPower = 12) {
    this.vy = verticalPower;
    this.isAirborne = true;
    this.setPose(this.isHero ? 'juggle' : 'air', 1.0);
  }

  groundSlam() {
    this.vy = -18;
    this.setPose('slam', 0.5);
  }

  takeHit(damage = 10, launch = false) {
    this.health = Math.max(0, this.health - damage);
    this.hitStopFrames = 4; // 60 FPS frame-freeze juice

    if (this.health <= 0) {
      this.setPose('knockdown', 3.0);
      this.vy = 4;
      this.isAirborne = true;
    } else if (launch) {
      this.launchIntoAir(10);
    } else {
      this.setPose('hurt', 0.22);
      this.x += this.facing * -0.25; // Knockback
    }
  }

  update(delta) {
    if (this.hitStopFrames > 0) {
      this.hitStopFrames--;
      return;
    }

    // Airborne physics
    if (this.isAirborne) {
      this.y += this.vy * delta;
      this.vy -= 28 * delta; // Gravity

      if (this.y <= 0) {
        this.y = 0;
        this.vy = 0;
        this.isAirborne = false;
        if (this.health <= 0) {
          this.setPose('knockdown', 3.0);
        } else {
          this.setPose('idle');
        }
      }
    }

    // Pose timer recovery
    if (this.animTime > 0) {
      this.animTime -= delta;
      if (this.animTime <= 0 && this.health > 0) {
        this.setPose('idle');
      }
    }

    // Procedural Idle bobbing / martial arts guard breathing
    let bob = 0;
    if (this.currentPose === 'idle' && !this.isAirborne) {
      bob = Math.sin(Date.now() * 0.007) * 0.05;
    }

    this.mesh.position.y = 1.3 + this.y + bob;

    // Scale shadow based on altitude
    const shadowScale = Math.max(0.2, 1.0 - this.y * 0.15);
    this.shadowMesh.scale.set(shadowScale, shadowScale, shadowScale);
    this.shadowMesh.material.opacity = Math.max(0.1, 0.85 - this.y * 0.12);

    this.updatePosition();
  }

  updatePosition() {
    this.group.position.set(this.x, 0, this.z);
    this.mesh.scale.x = this.facing;
  }
}
