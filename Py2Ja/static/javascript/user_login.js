$(document).ready(function(){
    $(".user-login").click(function(e){
        // Prevents the default action to be triggered.
        e.preventDefault();
        // Triggering bPopup when click event is fired
        $('#login_to_pop_up').bPopup({
            modalClose: false,
            opacity: 0,
            closeClass: "login-close",
        });
    });

    $(".login-button").click(function(){
        UserName = $(".UserName").val();
        PassWord = $(".PassWord").val();

        // using Ajax POST in Django
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        var csrftoken = getCookie('csrftoken');
        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url : "/user/login",
            type : "POST",
            dataType : "text",
            data : {username: UserName, password: PassWord},

            success: function(data){
                $.dialog({
                    title: '用户操作',
                    content: data,
                });
                setTimeout(function (){
                    window.location.reload();
                }, 1000);
            },

            complete: function(){
            },

            error: function(){
                alert("Error Happened While Running the Code...");
            },
        });
    });

    $(".user-logout").click(function(){
        $.ajax({
            url : "/user/logout",
            type : "GET",
            dataType : "text",
            data : {},

            success: function(data){
                $.alert({
                    title: '用户操作',
                    content: '您确定要登出吗？',
                    confirm: function(){
                        $.dialog({
                            title: '用户操作',
                            content: data,
                        });
                        setTimeout(function (){
                            window.location.reload();
                        }, 1000);
                    }
                });
            },

            complete: function(){
            },

            error: function(){
                alert("Error Happened While Running the Code...");
            },
        });
    });
});
