from pathlib import Path

base = Path('app3/templates/app3')
for fn in ['index.html', 'generic.html', 'elements.html']:
    path = base / fn
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    text = text.replace("{% static \\u005c'app3/images/", "{% static 'app3/images/")
    text = text.replace("{% static \\u005c'app3/assets/css/main.css\' %}", "{% static 'app3/assets/css/main.css' %}")
    text = text.replace("{% static \\u005c'app3/assets/css/noscript.css\' %}", "{% static 'app3/assets/css/noscript.css' %}")
    text = text.replace("{% static 'app3/images/", "{% static 'app3/images/")
    # Also fix any url tags with escaped quotes
    text = text.replace("{% url \\u005c'app3:index\\' %}", "{% url 'app3:index' %}")
    text = text.replace("{% url \\u005c'app3:generic\\' %}", "{% url 'app3:generic' %}")
    text = text.replace("{% url \\u005c'app3:elements\\' %}", "{% url 'app3:elements' %}")
    path.write_text(text, encoding='utf-8')
    print('fixed', fn)
