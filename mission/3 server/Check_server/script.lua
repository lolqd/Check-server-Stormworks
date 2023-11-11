tickrate = 0
tick_restart = 0
Port = 601

function onTick(game_ticks)
	tickrate = tickrate + 1
    tick_restart = tick_restart + game_ticks
	if tick_restart > 300 then
		messages = "3 True"
		server.httpGet(Port,messages)
		tick_restart = 0
	end
end