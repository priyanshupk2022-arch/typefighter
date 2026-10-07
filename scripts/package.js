// ============================================================================
// TYPEFIGHTER — STANDALONE WINDOWS DESKTOP PACKAGING SCRIPT
// ============================================================================

const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const ELECTRON_DIST = path.join(ROOT, 'node_modules', 'electron', 'dist');
const OUTPUT_DIR = path.join(ROOT, 'dist', 'TypeFighter');
const APP_DIR = path.join(OUTPUT_DIR, 'resources', 'app');

console.log('=== PACKAGING TYPEFIGHTER DESKTOP APPLICATION ===\n');

if (!fs.existsSync(ELECTRON_DIST)) {
  console.error('Error: Electron distribution not found in node_modules/electron/dist');
  process.exit(1);
}

// 1. Clean and create output directories
console.log('[1/4] Preparing dist directories...');
if (fs.existsSync(OUTPUT_DIR)) {
  fs.rmSync(OUTPUT_DIR, { recursive: true, force: true });
}
fs.mkdirSync(OUTPUT_DIR, { recursive: true });
fs.mkdirSync(APP_DIR, { recursive: true });

// Helper to copy directory recursively
function copyDirRecursive(src, dest) {
  fs.mkdirSync(dest, { recursive: true });
  const entries = fs.readdirSync(src, { withFileTypes: true });

  for (const entry of entries) {
    const srcPath = path.join(src, entry.name);
    const destPath = path.join(dest, entry.name);

    if (entry.isDirectory()) {
      if (entry.name === 'node_modules' || entry.name === '.git' || entry.name === 'dist' || entry.name === '__pycache__') {
        continue;
      }
      copyDirRecursive(srcPath, destPath);
    } else {
      fs.copyFileSync(srcPath, destPath);
    }
  }
}

// 2. Copy Electron Runtime Binaries
console.log('[2/4] Copying Electron runtime binaries...');
const electronFiles = fs.readdirSync(ELECTRON_DIST, { withFileTypes: true });
for (const entry of electronFiles) {
  const srcPath = path.join(ELECTRON_DIST, entry.name);
  let destName = entry.name;
  if (entry.name === 'electron.exe') {
    destName = 'TypeFighter.exe';
  }
  const destPath = path.join(OUTPUT_DIR, destName);

  if (entry.isDirectory()) {
    copyDirRecursive(srcPath, destPath);
  } else {
    fs.copyFileSync(srcPath, destPath);
  }
}

// 3. Copy Application Payload into resources/app
console.log('[3/4] Copying TypeFighter application assets and source code into resources/app...');
const appPayload = [
  'package.json',
  'main.js',
  'preload.js',
  'index.html',
  'styles.css',
  'build',
  'src',
  'assets'
];

for (const item of appPayload) {
  const srcPath = path.join(ROOT, item);
  const destPath = path.join(APP_DIR, item);

  if (!fs.existsSync(srcPath)) continue;

  const stat = fs.statSync(srcPath);
  if (stat.isDirectory()) {
    copyDirRecursive(srcPath, destPath);
  } else {
    fs.copyFileSync(srcPath, destPath);
  }
}

// 4. Verification
console.log('[4/4] Verifying packaged desktop application...');
const exePath = path.join(OUTPUT_DIR, 'TypeFighter.exe');
if (fs.existsSync(exePath)) {
  const exeSizeMB = Math.round(fs.statSync(exePath).size / (1024 * 1024));
  console.log(`\n✓ SUCCESS: TypeFighter Desktop App packaged!`);
  console.log(`  Path: ${exePath}`);
  console.log(`  Executable Size: ${exeSizeMB} MB`);
  console.log(`  Target Platform: Windows (win32-${process.arch})`);
} else {
  console.error('Failed to create TypeFighter.exe');
  process.exit(1);
}
