const { app, BrowserWindow, ipcMain, globalShortcut } = require('electron');
const path = require('path');
const fs = require('fs');

// Redirect user data outside OneDrive to standard Windows AppData
const userDataPath = path.join(app.getPath('appData'), 'KeyboardWarriorStickman');
app.setPath('userData', userDataPath);
const logFile = path.join(userDataPath, 'main_debug.log');

function log(msg) {
  try {
    if (!fs.existsSync(userDataPath)) fs.mkdirSync(userDataPath, { recursive: true });
    fs.appendFileSync(logFile, `[${new Date().toISOString()}] ${msg}\n`);
  } catch(e){}
}

process.on('uncaughtException', (err) => log('UNCAUGHT EXCEPTION: ' + err.stack));
process.on('unhandledRejection', (err) => log('UNHANDLED REJECTION: ' + (err && err.stack || err)));

// Standard stable switches
app.commandLine.appendSwitch('no-sandbox');
app.commandLine.appendSwitch('allow-file-access-from-files');

let mainWindow = null;

function createWindow() {
  log('createWindow() called');
  mainWindow = new BrowserWindow({
    width: 1440,
    height: 900,
    minWidth: 1024,
    minHeight: 640,
    title: 'Keyboard Warrior Stickman: Typing Beat \'Em Up',
    icon: path.join(__dirname, 'build', 'icon.png'),
    backgroundColor: '#0a0c14',
    show: true,
    autoHideMenuBar: true,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
      sandbox: false,
      webSecurity: false
    }
  });

  mainWindow.webContents.on('render-process-gone', (e, details) => {
    log('RENDER PROCESS GONE: ' + JSON.stringify(details));
  });

  mainWindow.webContents.on('did-fail-load', (e, code, desc, url) => {
    log(`DID FAIL LOAD: code=${code}, desc=${desc}, url=${url}`);
  });

  mainWindow.webContents.on('console-message', (e, level, message, line, sourceId) => {
    log(`[RENDERER CONSOLE ${level}] ${message} (${sourceId}:${line})`);
  });

  const indexPath = path.join(__dirname, 'index.html');
  log('Loading: ' + indexPath);
  mainWindow.loadFile(indexPath).catch(err => {
    log('loadFile error: ' + err.message);
  });

  // Fullscreen toggle with F11
  mainWindow.webContents.on('before-input-event', (event, input) => {
    if (input.key === 'F11' && input.type === 'keyDown') {
      mainWindow.setFullScreen(!mainWindow.isFullScreen());
      event.preventDefault();
    }
    if (input.key === 'F12' && input.type === 'keyDown') {
      mainWindow.webContents.toggleDevTools();
      event.preventDefault();
    }
  });

  mainWindow.on('close', (e) => {
    log('mainWindow close event triggered!');
  });

  mainWindow.on('closed', () => {
    log('mainWindow closed event triggered!');
    mainWindow = null;
  });
}

// IPC Listeners
ipcMain.handle('get-app-version', () => app.getVersion());
ipcMain.handle('toggle-fullscreen', () => {
  if (mainWindow) {
    const isFS = !mainWindow.isFullScreen();
    mainWindow.setFullScreen(isFS);
    return isFS;
  }
  return false;
});
ipcMain.handle('quit-app', () => {
  log('quit-app IPC called');
  app.quit();
});

app.on('before-quit', (e) => {
  log('app before-quit event');
});

app.on('will-quit', (e) => {
  log('app will-quit event');
});

app.on('quit', (e, exitCode) => {
  log('app quit event, exitCode=' + exitCode);
});

app.whenReady().then(() => {
  log('app whenReady fired');
  createWindow();

  app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on('window-all-closed', () => {
  log('window-all-closed event fired');
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

