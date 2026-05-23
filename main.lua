-- Der Loader, den deine Nutzer ausführen:
local Player = game:GetService("Players").LocalPlayer
local ScriptURL = "https://raw.githubusercontent.com/nexus113fdfcs-beep/Nexus/refs/heads/main/nexus.lua"

local function loadNexus()
    -- 1. Whitelist prüfen
    local success, whitelist = pcall(function() return game:HttpGet(WhitelistURL) end)
    
    if success and string.find(whitelist, tostring(Player.UserId)) then
        -- 2. Wenn User auf Liste, lade das Hauptskript
        local scriptSuccess, scriptContent = pcall(function() return game:HttpGet(ScriptURL) end)
        if scriptSuccess then
            loadstring(scriptContent)()
        else
            Player:Kick("Nexus Hub: Verbindung zum Server fehlgeschlagen.")
        end
    else
        Player:Kick("Nexus Hub: Du hast keinen Zugriff.")
    end
end

loadNexus()
