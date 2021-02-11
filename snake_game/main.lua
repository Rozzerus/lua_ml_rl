local utf8 = require("utf8")
require('game')

function love.load()
    love.window.setPosition(500, 50, 1)
    interval = 20
    add_apple()
    text = 'Player step log -- '
end

function love.draw()
    game_draw()
    if state == GaneStates.game_over then
        love.graphics.print('Game Over!', 330, 350, 0, 4, 4)
        love.graphics.print('Press r to restart ', 270, 450, 0, 3, 3)
    end
    love.graphics.print(text, 10, 30, 0, 1, 1)
end

function love.update()
    if state == GaneStates.running then 
        interval = interval - 1
        if interval < 0 then
            game_update()
            if tail_legth <= 5 then
                interval = 12
            elseif tail_legth > 5 and tail_legth <= 10 then
                interval = 9
            elseif tail_legth > 10 and tail_legth <= 15 then
                interval = 6
            else
                interval = 3
            end
        end
    end
end

function love.textinput(key)
    text = text .. key
    if key == 'a' and state == GaneStates.running then
        left, right, up, down = true, false, false, false
    elseif key == 'd' and state == GaneStates.running then
        left, right, up, down = false, true, false, false
    elseif key == 'w' and state == GaneStates.running then
        left, right, up, down = false, false, true, false
    elseif key == 's' and state == GaneStates.running then
        left, right, up, down = false, false, false, true
    elseif key == 'r' and state == GaneStates.game_over then
        game_restart()
    end
end

----this implementation correct only for player game
function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    elseif key == 'p' then
        if state == GaneStates.running then
            state = GaneStates.pause
        elseif state == GaneStates.pause then
            state = GaneStates.running
        end
  end
end