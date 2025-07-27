import numpy as np
import matplotlib.pyplot as plt

# ---------- تنظیمات ----------
n1 = 1.0  # ضریب شکست محیط اول (مثلاً هوا)
n2 = 1.5  # ضریب شکست محیط دوم (مثلاً شیشه)
theta_incident_deg = 45  # زاویه تابش (درجه)

# ---------- قانون اسنل ----------
def snell_law(n1, n2, theta1_rad):
    sin_theta2 = n1 / n2 * np.sin(theta1_rad)
    if abs(sin_theta2) > 1:
        return None  # بازتاب کلی داخلی
    return np.arcsin(sin_theta2)

# ---------- ترسیم ----------
def draw_ray_diagram(n1, n2, theta_inc_deg):
    theta1 = np.radians(theta_inc_deg)
    theta2 = snell_law(n1, n2, theta1)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1, 3)
    ax.set_aspect('equal')

    # سطح جدایی بین دو محیط
    ax.axhline(y=1, color='black', linestyle='--', linewidth=1)
    ax.text(-1.8, 1.05, "Interface", fontsize=10)

    # پرتو تابشی
    x0, y0 = 0, 0
    x1, y1 = np.sin(theta1), np.cos(theta1)
    ax.arrow(x0, y0, x1, y1, head_width=0.05, head_length=0.1,
             fc='blue', ec='blue', linewidth=2)
    ax.text(x1 + 0.1, y1 - 0.1, "Incident", color='blue')

    # پرتو شکسته یا بازتاب شده
    if theta2 is not None:
        # پرتو شکسته
        x2, y2 = np.sin(theta2), -np.cos(theta2)
        ax.arrow(x1, y1, x2, y2, head_width=0.05, head_length=0.1,
                 fc='green', ec='green', linewidth=2)
        ax.text(x1 + x2 + 0.1, y1 + y2 - 0.1, "Refracted", color='green')
    else:
        # بازتاب کلی داخلی
        x2, y2 = np.sin(theta1), -np.cos(theta1)
        ax.arrow(x1, y1, x2, y2, head_width=0.05, head_length=0.1,
                 fc='red', ec='red', linewidth=2)
        ax.text(x1 + x2 + 0.1, y1 + y2 - 0.1, "Reflected", color='red')

    ax.set_title("2D Ray Tracing with Snell's Law")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True)
    plt.tight_layout()
    plt.savefig("ray_tracing_2d_output.png")
    plt.show()

# ---------- اجرا ----------
if name == "main":
    draw_ray_diagram(n1, n2, theta_incident_deg)