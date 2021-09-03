from AutoHotPy import AutoHotPy
from InterceptionWrapper import *
def exitAutoHotKey(autohotpy,event):
    autohotpy.stop()
def recorded_macro(autohotpy, event):
    autohotpy.moveMouseToPosition(449,299)
    autohotpy.sleep(0)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.006003618240356445)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007710933685302734)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 4
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007993459701538086)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 6
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007468461990356445)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 7
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008545637130737305)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 7
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007734060287475586)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 8
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007984161376953125)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 7
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008114814758300781)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 10
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008019685745239258)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 9
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.010098934173583984)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 8
    stroke.y = 2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007901191711425781)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 11
    stroke.y = 2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00794219970703125)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 7
    stroke.y = 2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.011901617050170898)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 6
    stroke.y = 3
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007967948913574219)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 7
    stroke.y = 5
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008482694625854492)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 3
    stroke.y = 3
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008130073547363281)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 2
    stroke.y = 2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.011299610137939453)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = 3
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.01202845573425293)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = 4
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007906198501586914)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 5
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008371353149414062)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 3
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0077898502349853516)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = 4
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00848531723022461)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = 3
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007721424102783203)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 5
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00836181640625)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007758617401123047)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -4
    stroke.y = 2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008241415023803711)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007805585861206055)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -4
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008235692977905273)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0071489810943603516)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00824427604675293)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.01642131805419922)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.01592850685119629)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0082550048828125)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0070073604583740234)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007955312728881836)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008020877838134766)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007993459701538086)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008970022201538086)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0075724124908447266)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007998466491699219)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007994890213012695)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00993800163269043)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.01196742057800293)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.5563497543334961)
    autohotpy.LEFT_ARROW.down()
    autohotpy.sleep(0.12323522567749023)
    autohotpy.SPACE.down()
    autohotpy.sleep(0.07739114761352539)
    autohotpy.LEFT_ARROW.up()
    autohotpy.sleep(0.02412247657775879)
    autohotpy.SPACE.up()
    autohotpy.sleep(0.031499624252319336)
    autohotpy.D.down()
    autohotpy.sleep(0.14873313903808594)
    autohotpy.D.up()
    autohotpy.sleep(0.33785009384155273)
    autohotpy.RIGHT_ARROW.down()
    autohotpy.sleep(0.19908595085144043)
    autohotpy.SPACE.down()
    autohotpy.sleep(0.08012890815734863)
    autohotpy.D.down()
    autohotpy.sleep(0.02121114730834961)
    autohotpy.RIGHT_ARROW.up()
    autohotpy.sleep(0.01667642593383789)
    autohotpy.SPACE.up()
    autohotpy.sleep(0.10797762870788574)
    autohotpy.D.up()
    autohotpy.sleep(0.6363198757171631)
    autohotpy.I.down()
    autohotpy.sleep(0.10667848587036133)
    autohotpy.I.up()
    autohotpy.sleep(0.1230459213256836)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007833719253540039)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007978200912475586)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008015155792236328)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00825357437133789)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00783395767211914)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007467746734619141)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008327245712280273)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008114099502563477)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.11399626731872559)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.006066560745239258)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008374929428100586)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0071239471435546875)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007767677307128906)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.010974645614624023)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007978439331054688)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0074841976165771484)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00803065299987793)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -8
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008394956588745117)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -6
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008000373840332031)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -7
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007753849029541016)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -8
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008000373840332031)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -7
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008244514465332031)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007752180099487305)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -9
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007698535919189453)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -9
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008243560791015625)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -6
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007571220397949219)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -6
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008917808532714844)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -8
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007978677749633789)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -6
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.011698246002197266)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008050918579101562)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -10
    stroke.y = -5
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008288383483886719)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00771331787109375)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -6
    stroke.y = -3
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007405757904052734)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = -3
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008464336395263672)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008079051971435547)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -4
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008336067199707031)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007524728775024414)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00754237174987793)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00876927375793457)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.01571488380432129)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008429288864135742)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 3
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0077664852142333984)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 7
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008241653442382812)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 8
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00796365737915039)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 11
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.011015892028808594)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 15
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.009056806564331055)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 23
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.013789176940917969)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 23
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007145404815673828)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 25
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.011970043182373047)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 22
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.012359857559204102)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 30
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00797891616821289)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 32
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008722305297851562)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 23
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007843255996704102)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 14
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00792074203491211)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 20
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007431507110595703)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 12
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008315563201904297)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 11
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007997274398803711)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 15
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.012303829193115234)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 10
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.012064933776855469)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 13
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00792551040649414)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 11
    stroke.y = 1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007576704025268555)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 7
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008074760437011719)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 5
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008573293685913086)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 4
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007784843444824219)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 3
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008072137832641602)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 3
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007948160171508789)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00800943374633789)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007530927658081055)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00771331787109375)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007979154586791992)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.009001970291137695)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 4
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00695490837097168)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 3
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00797724723815918)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 5
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.009140968322753906)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 5
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007227420806884766)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 4
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008295059204101562)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 6
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00824594497680664)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 3
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00805354118347168)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 3
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.01123809814453125)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.009975433349609375)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.04437899589538574)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00825643539428711)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007646322250366211)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008512735366821289)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007550477981567383)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007982730865478516)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -4
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00848531723022461)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007711648941040039)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -6
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00797891616821289)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -7
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008021116256713867)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007811784744262695)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -8
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007866382598876953)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -7
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00798797607421875)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008204936981201172)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -7
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008034944534301758)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -5
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00748133659362793)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008921384811401367)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007201433181762695)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007982015609741211)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008835077285766602)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007711648941040039)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008244037628173828)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0078067779541015625)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007501125335693359)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00823521614074707)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007527351379394531)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008048295974731445)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008637189865112305)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.010141611099243164)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007302045822143555)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008024215698242188)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00832509994506836)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0074770450592041016)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007978200912475586)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.009076356887817383)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007372379302978516)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -3
    stroke.y = -2
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007764339447021484)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00877833366394043)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.0077626705169677734)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008025646209716797)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008083581924438477)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00745844841003418)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007973909378051758)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008031129837036133)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008387327194213867)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.007843017578125)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008054733276367188)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008433103561401367)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = -1
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00803375244140625)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -2
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00696873664855957)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008990287780761719)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.006918907165527344)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.00846099853515625)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.14178037643432617)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.008415699005126953)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.024211645126342773)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.22562956809997559)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_BUTTON_1_DOWN
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.18375015258789062)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_BUTTON_1_UP
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = 0
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
    autohotpy.sleep(0.34449148178100586)
    stroke = InterceptionMouseStroke()
    stroke.state = InterceptionMouseState.INTERCEPTION_MOUSE_MOVE
    stroke.flags = InterceptionMouseFlag.INTERCEPTION_MOUSE_MOVE_RELATIVE
    stroke.rolling = 0
    stroke.x = -1
    stroke.y = 0
    stroke.information = 0
    autohotpy.sendToDefaultMouse(stroke)
if __name__=="__main__":
    auto = AutoHotPy()
    auto.registerExit(auto.ESC,exitAutoHotKey)
    auto.registerForKeyDown(auto.F1,recorded_macro)
    auto.start()
