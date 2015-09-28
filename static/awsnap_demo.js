var renderText, updater;

$(document).ready(function() {
  if (!window.console) {
    window.console = {};
  }
  if (!window.console.log) {
    window.console.log = function() {};
  }
  window.canvas = new fabric.Canvas('my_canvas');
  window.canvas.backgroundColor = "black";
  window.canvas.renderAll();
  return updater.start();
});

renderText = function(x) {
  var i, j, ref;
  window.canvas.clear();
  for (i = j = 1, ref = x; 1 <= ref ? j <= ref : j >= ref; i = 1 <= ref ? ++j : --j) {
    if (Math.round(i / 2) === i / 2) {
      window.canvas.add(new fabric.Text('2', {
        left: 33,
        top: 33,
        fill: 'rgba(255,255,255,1)',
        fontSize: 15
      }));
    } else {
      window.canvas.add(new fabric.Text('W', {
        left: 18,
        top: 18,
        fill: 'rgba(255,255,255,1)',
        fontSize: 22
      }));
    }
  }
  return window.canvas.renderAll();
};

updater = {
  socket: null,
  start: function() {
    var url;
    url = 'ws://' + location.host + '/mainsocket';
    updater.socket = new WebSocket(url);
    updater.socket.onmessage = function(event) {
      return updater.processMessage(JSON.parse(event.data));
    };
    return updater.socket.onopen = updater.initialize;
  },
  processMessage: function(message) {
    return renderText(2);
  }
};
