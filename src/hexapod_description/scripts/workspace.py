import numpy as np
import matplotlib.pyplot as plt

l_coxa = 0.05
l_femur = 0.1
l_tibia = 0.15

x_c = 0.1
y_c = 0.08
z_c = -0.02

# sudut yam awal di 45 derajat
PSI = np.deg2rad(45.0)

# batas sudut tiap joint
q1_values = np.deg2rad(np.arange(-45, 46, 10))
q2_values = np.deg2rad(np.arange(-60, 61, 10))
q3_values = np.deg2rad(np.arange(-90, 91, 10))

# fk

workspace_points = []

for q1 in q1_values:
    for q2 in q2_values:
        for q3 in q3_values:
            x_lokal = (
                l_coxa - l_femur*np.sin(q2) - l_tibia*np.sin(q2+q3)
            )
            z_lokal = (-l_femur*np.cos(q2) - l_tibia*np.cos(q2+q3))

            # orientasi kaki terhadap base link
            phi = PSI + q1
            # transformasi ke koordinat base link
            x = x_c + x_lokal * np.cos(phi)
            y = y_c + x_lokal * np.sin(phi)
            z = z_c +z_lokal

            workspace_points.append([x,y,z])

points = np.array(workspace_points)

# 4. FILTER POSISI UJUNG KAKI DI DALAM BODY
# ==========================================

BODY_LENGTH = 0.30
BODY_WIDTH = 0.20
BODY_HEIGHT = 0.04

# Margin tambahan 1 cm sebagai clearance awal
MARGIN = 0.01

inside_body = (
    (np.abs(points[:, 0]) <= BODY_LENGTH / 2 + MARGIN)
    & (np.abs(points[:, 1]) <= BODY_WIDTH / 2 + MARGIN)
    & (np.abs(points[:, 2]) <= BODY_HEIGHT / 2 + MARGIN)
)

safe_foot_points = points[~inside_body]

print("Jumlah seluruh titik:", len(points))
print("Titik foot di dalam body:", np.sum(inside_body))
print("Titik foot di luar body:", len(safe_foot_points))

# 4. INFORMASI WORKSPACE
# ==========================================

print("Jumlah titik workspace:", len(points))

print("\nBatas koordinat kaki:")
print("X:", points[:, 0].min(), "sampai", points[:, 0].max(), "m")
print("Y:", points[:, 1].min(), "sampai", points[:, 1].max(), "m")
print("Z:", points[:, 2].min(), "sampai", points[:, 2].max(), "m")

# ==========================================
# 5. VISUALISASI 3D
# ==========================================

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(
    safe_foot_points[:, 0],
    safe_foot_points[:, 1],
    safe_foot_points[:, 2],
    s=2,
    alpha=0.25,
    label="Foot outside body"
)

# Titik pemasangan coxa
ax.scatter(
    x_c, y_c, z_c,
    s=60,
    marker="o",
    label="Coxa mount"
)

# Pusat base_link
ax.scatter(
    0, 0, 0,
    s=60,
    marker="^",
    label="Base link origin"
)

ax.set_title("Hexapod Front-Left Leg Workspace")
ax.set_xlabel("X (meter)")
ax.set_ylabel("Y (meter)")
ax.set_zlabel("Z (meter)")

ax.legend()
ax.set_box_aspect((1, 1, 1))
plt.tight_layout()
plt.show()