const {app, BrowserWindow} = require('electron');


let win
function createWindow() {
  win = new BrowserWindow({width:1280, height:660, center:true, maximizable:false, transparent:true, autoHideMenuBar:true})
  //win.loadFile('index.html')
  win.loadURL("http://192.168.0.4:5000/")
}

app.on('ready', createWindow)
