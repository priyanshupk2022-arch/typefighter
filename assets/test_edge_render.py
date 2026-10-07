import subprocess
import os

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\preview_gallery.html"
out_png = r"c:\Users\priya\OneDrive\Documents\Next Toppers\typefighter\assets\gallery_screenshot.png"
html_url = "file:///" + html.replace("\\", "/")

cmd = [
    edge,
    "--headless=new",
    f"--screenshot={out_png}",
    "--window-size=1400,2400",
    html_url
]
res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("PNG exists:", os.path.exists(out_png))
if os.path.exists(out_png):
    print("PNG File Size:", os.path.getsize(out_png), "bytes")
