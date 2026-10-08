// Keyboard Warrior Stickman - Authentic 5-Arena 3D Scene & Perspective Camera System
import * as THREE from 'three';

export class ArenaManager {
  constructor(canvasContainer) {
    this.container = canvasContainer;
    this.currentArenaKey = 'desk';
    this.shakeIntensity = 0;
    this.shakeDecay = 5.0; // Decay rate per second
    this.baseCameraPos = new THREE.Vector3(0, 2.4, 7.2);
    this.baseLookAt = new THREE.Vector3(0, 1.2, 0);

    // Setup Three.js WebGL Renderer
    this.renderer = new THREE.WebGLRenderer({
      antialias: true,
      powerPreference: 'high-performance',
      alpha: false
    });
    this.renderer.setSize(window.innerWidth, window.innerHeight);
    this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    this.renderer.shadowMap.enabled = true;
    this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    this.container.appendChild(this.renderer.domElement);

    // Scene & Camera
    this.scene = new THREE.Scene();
    this.camera = new THREE.PerspectiveCamera(
      45,
      window.innerWidth / window.innerHeight,
      0.1,
      100
    );
    this.camera.position.copy(this.baseCameraPos);
    this.camera.lookAt(this.baseLookAt);

    // Setup Lighting
    this.setupLighting();

    // Setup Arena Assets
    this.textureLoader = new THREE.TextureLoader();
    this.arenaConfigs = {
      desk: {
        name: 'The Wooden Desk',
        texture: 'assets/textures/arenas/desk_room.jpg',
        floorColor: 0x4a3728,
        bgPlaneSize: [18, 10],
        bgPlanePos: [0, 3.5, -4]
      },
      crt: {
        name: 'Retro CRT Computer',
        texture: 'assets/textures/arenas/crt_computer.jpg',
        floorColor: 0x333333,
        bgPlaneSize: [18, 10],
        bgPlanePos: [0, 3.5, -4]
      },
      bliss: {
        name: 'Windows XP Bliss',
        texture: 'assets/textures/arenas/windows_xp_bliss.jpg',
        floorColor: 0x3b8526,
        bgPlaneSize: [20, 11],
        bgPlanePos: [0, 3.5, -5]
      },
      mxpain: {
        name: 'untitled - MXPain',
        texture: 'assets/textures/arenas/mxpain_paint.jpg',
        floorColor: 0xd4d0c8,
        bgPlaneSize: [18, 10],
        bgPlanePos: [0, 3.5, -4]
      },
      greenscreen: {
        name: 'Green Screen Studio',
        texture: null,
        floorColor: 0x00ff00,
        bgColor: 0x00ff00,
        bgPlaneSize: [22, 12],
        bgPlanePos: [0, 3.5, -4]
      }
    };

    this.createEnvironmentMeshes();
    this.switchArena('desk');

    // Handle Window Resize
    window.addEventListener('resize', () => this.onWindowResize());
  }

  setupLighting() {
    // Ambient light
    this.ambientLight = new THREE.AmbientLight(0xffffff, 0.85);
    this.scene.add(this.ambientLight);

    // Directional light from top-front
    this.dirLight = new THREE.DirectionalLight(0xfff5e6, 0.9);
    this.dirLight.position.set(2, 8, 6);
    this.dirLight.castShadow = true;
    this.dirLight.shadow.mapSize.width = 1024;
    this.dirLight.shadow.mapSize.height = 1024;
    this.dirLight.shadow.camera.near = 0.5;
    this.dirLight.shadow.camera.far = 20;
    this.scene.add(this.dirLight);
  }

  createEnvironmentMeshes() {
    // Backdrop Mesh (Background plane that displays the arena screenshot/image)
    this.bgGeo = new THREE.PlaneGeometry(18, 10);
    this.bgMat = new THREE.MeshBasicMaterial({ side: THREE.DoubleSide });
    this.bgMesh = new THREE.Mesh(this.bgGeo, this.bgMat);
    this.bgMesh.position.set(0, 3.5, -4);
    this.scene.add(this.bgMesh);

    // Floor / Desk surface plane (Ground where standees walk and drop shadows)
    const floorGeo = new THREE.PlaneGeometry(24, 12);
    this.floorMat = new THREE.MeshStandardMaterial({
      color: 0x222222,
      roughness: 0.85,
      metalness: 0.1
    });
    this.floorMesh = new THREE.Mesh(floorGeo, this.floorMat);
    this.floorMesh.rotation.x = -Math.PI / 2;
    this.floorMesh.position.y = 0;
    this.floorMesh.receiveShadow = true;
    this.scene.add(this.floorMesh);

    // Grid helper on desk floor for retro digital arcade feel
    this.gridHelper = new THREE.GridHelper(24, 24, 0x00f0ff, 0x334455);
    this.gridHelper.position.y = 0.005;
    this.gridHelper.material.opacity = 0.2;
    this.gridHelper.material.transparent = true;
    this.scene.add(this.gridHelper);
  }

  switchArena(arenaKey) {
    const config = this.arenaConfigs[arenaKey] || this.arenaConfigs['desk'];
    this.currentArenaKey = arenaKey;

    if (arenaKey === 'greenscreen') {
      this.renderer.setClearColor(0x00ff00, 1);
      this.scene.background = new THREE.Color(0x00ff00);
      this.bgMesh.visible = false;
      this.floorMat.color.setHex(0x00ff00);
      this.gridHelper.visible = true;
      this.gridHelper.material.opacity = 0.15;
    } else {
      this.scene.background = new THREE.Color(0x05070c);
      this.bgMesh.visible = true;
      this.gridHelper.visible = false;
      this.floorMat.color.setHex(config.floorColor);

      if (config.texture) {
        this.textureLoader.load(config.texture, (texture) => {
          texture.colorSpace = THREE.SRGBColorSpace;
          this.bgMat.map = texture;
          this.bgMat.needsUpdate = true;
        });
      }
    }
  }

  triggerScreenShake(intensity = 0.3) {
    this.shakeIntensity = Math.min(1.0, this.shakeIntensity + intensity);
  }

  onWindowResize() {
    this.camera.aspect = window.innerWidth / window.innerHeight;
    this.camera.updateProjectionMatrix();
    this.renderer.setSize(window.innerWidth, window.innerHeight);
  }

  update(delta) {
    // Camera shake physics
    if (this.shakeIntensity > 0) {
      const offsetX = (Math.random() - 0.5) * this.shakeIntensity * 0.4;
      const offsetY = (Math.random() - 0.5) * this.shakeIntensity * 0.4;
      const offsetZ = (Math.random() - 0.5) * this.shakeIntensity * 0.2;
      
      this.camera.position.set(
        this.baseCameraPos.x + offsetX,
        this.baseCameraPos.y + offsetY,
        this.baseCameraPos.z + offsetZ
      );
      this.shakeIntensity = Math.max(0, this.shakeIntensity - this.shakeDecay * delta);
    } else {
      this.camera.position.copy(this.baseCameraPos);
    }

    this.camera.lookAt(this.baseLookAt);
  }

  render() {
    this.renderer.render(this.scene, this.camera);
  }
}
