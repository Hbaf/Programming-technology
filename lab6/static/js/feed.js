'use strict';
window.onkeydown = esc_handle;
// TODO fix return to main page on Esc
function esc_handle(e) {
    if (e.key == 'Escape'){
        window.location.href='../../';
    }
}
function change_page(page) {
	let id = $('#header > div.logo')[0].id;
	$.ajax({
        url: "/rest/feed/" + id + '/' + page,
        type: "GET",

        contentType: 'application/json; charset=utf-8',
        success: function (resultData) {
            if (resultData['error']) {
                return;
            }
            let section = $('#articles')[0];
            let article = '';
            for (let post of resultData['articles']) {
                article += `
                    <article>
                        <header class="main">
                            <a target="_blank" href="{{article[2]}}"><h2>${post[1]}</h2></a>
                        </header>
                        <div class="row">
                        `;
                if (post[4]) {
                    article += `
                            <div class="col-2 col-12-medium">
                                <p><b>${post[4]}</b></p>
                            </div>`;
                }
                article += `
		                    <div class="col-4 col-12-medium">
		                        <p>${post[3]}</p>
		                    </div>
		                </div>
		                ${post[6]}`;
                for (let _tag of post[5]) {
                    if (_tag != '') {
                        article += `
                        <div class="tag"><b>${_tag}</b></div>`
                    }
                }
                article += `
                    </article>
                    <hr class="major" />`;
            }
            section.innerHTML=article;
		},
		error: function (jqXHR, textStatus, errorThrown) {
		},
		timeout: 60000,
	});
	scrollTo(document.documentElement, 0, 2000);
}

function scrollTo(element, to, duration) {
        if (duration < 0) return;
        var difference = to - element.scrollTop;
        var perTick = difference / duration * 10;

        setTimeout(function() {
            element.scrollTop = element.scrollTop + perTick;
            scrollTo(element, to, duration - 10);
        }, 10);
    }