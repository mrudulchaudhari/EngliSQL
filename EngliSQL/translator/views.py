from django.shortcuts import render
from .prompts import generate_sql_from_english
# Create your views here.

def home(request):
    sql_query = ""
    if request.method == "POST":
        schema = request.POST.get("schema")
        english_query = request.POST.get("english_query")
        user_schema = request.POST.get("user_schema", "")
        sql_query = generate_sql_from_english(english_query, schema, user_schema)

    return render(request, "home.html", {"sql_query": sql_query})