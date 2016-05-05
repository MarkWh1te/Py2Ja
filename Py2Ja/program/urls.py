from django.conf.urls import url

urlpatterns = [
    url(r'^code/list', "program.views.list_codes", name="program_list_codes"),
    url(r'^code/load/cpp', "program.views.load_cpp", name="program_list_codes"),
    url(r'^code/load/java', "program.views.load_java", name="program_list_codes"),
    url(r'^code/load/python', "program.views.load_python", name="program_list_codes"),
    url(r'^code/load/php', "program.views.load_php", name="program_list_codes"),
    url(r'^code/load/javascript', "program.views.load_javascript", name="program_list_codes"),
    url(r'^code/load/sql', "program.views.load_sql", name="program_list_codes"),
    url(r'^code/view/(?P<snippet_id>\d+)', "program.views.view_code", name="program_view_code"),
    url(r'^code/write', "program.views.write_code", name="program_write_code"),
    url(r'^code/run/python', "program.views.run_python_code", name="program_write_code"),
    url(r'^code/run/cpp', "program.views.run_cpp_code", name="program_write_code"),
    url(r'^code/run/java', "program.views.run_java_code", name="program_write_code"),
    url(r'^code/run/php', "program.views.run_php_code", name="program_write_code"),
    url(r'^code/run/javascript', "program.views.run_javascript_code", name="program_write_code"),
    url(r'^code/run/sql', "program.views.run_sql_code", name="program_write_code"),
]
