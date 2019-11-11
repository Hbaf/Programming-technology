current_round = {};
			function new_round() {
				$.ajax({
					url: "/rest/" + document.getElementById('type-selector').value,
					type: "GET",

					contentType: 'application/json; charset=utf-8',
					success: function (resultData) {
						current_round = resultData;
						$('#pic img').attr('src', resultData['url'][0]);
						var selector = document.getElementById('ans-input');
						selector.options[0].value = resultData['name_var'][0];
						selector.options[1].value = resultData['name_var'][1];
						selector.options[2].value = resultData['name_var'][2];
						selector.options[3].value = resultData['name_var'][3];
						selector.options[0].text = resultData['name_var'][0];
						selector.options[1].text = resultData['name_var'][1];
						selector.options[2].text = resultData['name_var'][2];
						selector.options[3].text = resultData['name_var'][3];
					},
					error: function (jqXHR, textStatus, errorThrown) {
					},
					timeout: 60000,
				});
			}

			function showMsg(msg) {
				document.getElementById('result-msg').innerHTML = msg;
				if (msg === 'Correct') {
					document.getElementById('result').className = 'shown correct';
				}else{
					document.getElementById('result').className = 'shown wrong';
				}
			}

			function hideMsg() {
				document.getElementById('result').className = 'hidden';
			}

			function check_answer(){
				if (document.getElementById('ans-input').value == current_round['answer']) {
					showMsg('Correct');
					setTimeout(hideMsg, 1000);
					new_round();
				}else{
					showMsg('Wrong');
					setTimeout(hideMsg, 1000);
				}
			}
			document.getElementById('ans-bttn').onclick = check_answer;
			document.getElementById('type-selector').onchange = new_round;
			new_round();