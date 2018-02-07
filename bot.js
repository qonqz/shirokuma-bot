const Discord = require('discord.js')
const bot = new Discord.Client()
const responseObject = {
    "สวัสดี": "Yo, สวัสดี!",
    "wat": "Say what?",
    "lol": "roflmaotntpmp",
    "ไอ้อ้วน": "ไหน! ใครอ้วน! อ๊า!"
  };

bot.login(process.env.BOT_TOKEN);

bot.on("ready",()=>{
    console.log("HELLO! THIS IS SHIROKUMA-BOT. NOW, I'M READY TO USE.")
})

bot.on("message", (message) => {
    if (message.content.startsWith("ping")) {
      message.channel.send("pong!");
    } else
  
    if (message.content.startsWith("foo")) {
      message.channel.send("bar!");
    }
  });

  bot.on("guildMemberAdd", (member) => {
    console.log(`New User "${member.user.username}" has joined "${member.guild.name}"` );
    member.guild.channels.get("welcome").send(`"${member.user.username}" has joined this server`);
  });

  bot.on("message", (message) => {
    if(responseObject[message.content]) {
      message.channel.send(responseObject[message.content]);
    }
  });
