$(document).ready(function(){
  var playlist = [{
      title:"NiceHidden",
      artist:"CuPlayer.com",
      mp3:"http://rm.sina.com.cn/wm/VZ2010050511043310440VK/music/MUSIC1005051622027270.mp3",
      poster: "/static/images/player/1.jpg"
    },{
      title:"Cro Magnon Man",
      artist:"The Stark Palace",
      mp3:"http://rm.sina.com.cn/wm/VZ2010050511043310440VK/music/MUSIC1005051622027270.mp3",
      poster: "/static/images/player/2.jpg"
    },{
      title:"Bubble",
	  artist:"The Stark Palace",
      mp3: "http://rm.sina.com.cn/wm/VZ2010050511043310440VK/music/MUSIC1005051622027270.mp3",
      poster: "/static/images/player/3.jpg"
  }];
  
  var cssSelector = {
    jPlayer: "#jquery_jplayer",
    cssSelectorAncestor: ".music-player"
  };
  
  var options = {
    swfPath: "/media/files/Jplayer.swf",
    supplied: "ogv, m4v, oga, mp3"
  };
  
  var myPlaylist = new jPlayerPlaylist(cssSelector, playlist, options);
  
});
