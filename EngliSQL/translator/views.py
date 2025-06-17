from django.shortcuts import render
from .prompts import generate_sql_from_english

def home(request):
    sql_query = ""
    error = ""

    if request.method == "POST":
        schema = request.POST.get("schema")
        english_query = request.POST.get("english_query", "").strip()
        user_schema = request.POST.get("user_schema", "")

        if english_query:
            try:
                sql_query = generate_sql_from_english(english_query, schema, user_schema)
            except Exception as e:
                error = f"Error generating SQL: {e}"
        else:
            sql_query = ""
            error = "Please enter a valid English query."

    return render(request, "home.html", {"sql_query": sql_query, "error": error})
