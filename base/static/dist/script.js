var S={init:function(){S.problems.init()},problems:{dom:{get_challenge_button:!1,challenge_container:!1},init:function(){$("button[data-problem]").length>0&&(S.problems.dom.get_challenge_button=$("button[data-problem]"),S.problems.dom.challenge_container=$("#challenge_container"),S.problems.dom.get_challenge_button.click(function(a){a.preventDefault(),S.problems.dom.challenge_container.load("/problems/"+S.problems.dom.get_challenge_button.data("problem")+"/challenge")}))}}};$(document).ready(S.init);