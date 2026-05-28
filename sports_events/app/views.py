"""
views.py
Route handler logic (framework-agnostic pseudocode / reference).
Plug these into Flask / Django as needed.
"""

from .models import Event, Registration
from .forms import validate_registration


def index(request):
    """GET / — Render registration form."""
    return render("templates/index.html", {})


def events(request):
    """GET /events — Show event listing (requires session name+email)."""
    events = Event.all()
    return render("templates/events.html", {"events": events})


def register(request):
    """POST /register — Handle form submission."""
    if request.method != "POST":
        return redirect("/")

    data = {
        "full_name": request.POST.get("full_name"),
        "email":     request.POST.get("email"),
        "event_id":  request.POST.get("event_id"),
    }

    valid, errors = validate_registration(data)
    if not valid:
        return render("templates/events.html", {"errors": errors})

    reg = Registration(
        full_name=data["full_name"],
        email=data["email"],
        event_id=int(data["event_id"]),
    )
    reg.save()

    return redirect("/success")


def success(request):
    """GET /success — Show confirmation page."""
    return render("templates/success.html", {})


# ── stubs (replace with your framework's equivalents) ──
def render(template, context):
    raise NotImplementedError("Wire up to Flask render_template or Django render()")

def redirect(url):
    raise NotImplementedError("Wire up to Flask/Django redirect()")
