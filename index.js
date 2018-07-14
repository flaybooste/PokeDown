const {app, BrowserWindow} = require('electron');


let win
function createWindow() {
  win = new BrowserWindow({width:800, height:600, center:true, maximizable:false, transparent:true, autoHideMenuBar:true})
  //win.loadFile('index.html')
  win.loadURL("http://192.168.0.2:5000/")
}

app.on('ready', createWindow)
