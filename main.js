const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const path = require('path');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true
        }
    });

    win.loadFile('index.html');
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

// Flask sunucusunu başlat
const flaskProcess = spawn('python', ['app.py'], { cwd: __dirname, shell: true });

flaskProcess.stdout.on('data', (data) => {
    console.log(`Flask stdout: ${data}`);
});

flaskProcess.stderr.on('data', (data) => {
    console.error(`Flask stderr: ${data}`);
});

flaskProcess.on('close', (code) => {
    console.log(`Flask sunucusu kapandı: ${code}`);
});

app.on('ready', () => {
    console.log('Electron uygulaması başlatıldı!');
});
