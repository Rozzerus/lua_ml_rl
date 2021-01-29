require('game')

function love.load()
    love.window.setPosition(500, 50, 1)
    interval = 20
    add_apple()
end

function love.draw()
    game_draw()
    if state == GaneStates.game_over then
        love.graphics.print('Game Over!', 330, 350, 0, 4, 4)
        love.graphics.print('Press Space to restart ', 270, 450, 0, 3, 3)
    end
end

function love.update()
    if state == GaneStates.running then 
        interval = interval - 1
        if interval < 0 then
            game_update()
            if tail_legth <= 5 then
                interval = 20
            elseif tail_legth > 5 and tail_legth <= 10 then
                interval = 15
            elseif tail_legth > 10 and tail_legth <= 15 then
                interval = 10
            else
                interval = 5
            end
        end
    end
end

function love.keypressed(key)
    if key == 'escape' then
        love.event.quit()
    elseif key == 'left' and state == GaneStates.running then
        left, right, up, down = true, false, false, false
    elseif key == 'right' and state == GaneStates.running then
        left, right, up, down = false, true, false, false
    elseif key == 'up' and state == GaneStates.running then
        left, right, up, down = false, false, true, false
    elseif key == 'down' and state == GaneStates.running then
        left, right, up, down = false, false, false, true
    elseif key == 'space' and state == GaneStates.game_over then
        game_restart()
    elseif key == 'p' then
        if state == GaneStates.running then
            state = GaneStates.pause
        elseif state == GaneStates.pause then
            state = GaneStates.running
        end
    end
end