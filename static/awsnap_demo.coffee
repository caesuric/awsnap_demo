$(document).ready ->
    if !window.console
        window.console = {}
    if !window.console.log
        window.console.log = ->

    window.canvas = new fabric.Canvas('my_canvas')
    window.canvas.backgroundColor="black"
    window.canvas.renderAll()
    updater.start()
renderText = (x) ->
    window.canvas.clear()
    for i in [1..x]
        group = new fabric.Group()
        if Math.round(i/2)==i/2
            group.add new fabric.Text('2', left: 33, top: 33, fill: 'rgba(255,255,255,1)', fontSize: 15)
        else
            group.add new fabric.Text('W', left: 18, top: 18, fill: 'rgba(255,255,255,1)', fontSize: 22)
        window.canvas.add group
    window.canvas.renderAll()

updater = 
    socket: null
    start: ->
        url = 'ws://' + location.host + '/mainsocket'
        updater.socket = new WebSocket(url)
        updater.socket.onmessage = (event) ->
            updater.processMessage JSON.parse(event.data)
        updater.socket.onopen = updater.initialize
    processMessage: (message) ->
        renderText(2)
