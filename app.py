from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

PROFILE = {
    "name": "Shivam Kachawar",
    "role": "Software Engineer · Backend & Systems",
    "location": "Bangalore, Karnataka, India",
    "email": "shivamkachawar@gmail.com",
    "phone": "+91 91468 37144",
    "summary": (
        "Software Engineer building backend applications in Java, Spring Boot, Go, and Python. "
        "Experienced with Kafka-based job execution, PostgreSQL-backed services, Flask dashboards, "
        "and production infrastructure."
    ),
    "education": "B.Tech, Computer Science & Engineering",
    "college": "SGGS Institute of Engineering & Technology, Nanded",
    "cgpa": "8.76 / 10",
    "graduation": "2026",
    "dsa": "1,150+",
    "linkedin": "https://linkedin.com/in/shivam-kachawar-85a297257/",
    "leetcode": "https://leetcode.com/u/Shivam_kachawar/",
    "geeksforgeeks": "https://www.geeksforgeeks.org/user/shivamkachawar/",
    "tuf": "https://takeuforward.org/profile/shivam_kachawar",
    "github": "https://github.com/shivamkachawar",
}

PROJECTS = [
    {
        "number": "01", "name": "Distributed Job Scheduler",
        "type": "Backend Systems",
        "description": "A resilient scheduler with multiple scheduling modes, asynchronous execution, durable state, and concurrency-safe claiming.",
        "stack": ["Java", "Spring Boot", "PostgreSQL", "Kafka", "React"],
        "details": [
            "Supports one-time, interval, and cron schedules with PostgreSQL-backed recovery.",
            "Uses Kafka and the Transactional Outbox Pattern for durable, at-least-once event delivery.",
            "Configurable retries with exponential backoff and per-attempt tracking.",
            "Benchmarked 10,000 executions; measured 14.9K claims/sec at 10 workers across three local runs.",
            "26 automated tests, including PostgreSQL concurrency tests."
        ],
        "links": [
            {"label": "Backend repository", "url": "https://github.com/shivamkachawar/job-scheduler"},
            {"label": "Frontend repository", "url": "https://github.com/shivamkachawar/job-scheduler-ui"},
        ]
    },
    {
        "number": "02", "name": "Sniply — URL Shortener",
        "type": "Full-stack Product",
        "description": "A full-stack link management platform with analytics, secure authentication, QR codes, and cache-optimized redirects.",
        "stack": ["Spring Boot", "React", "PostgreSQL", "Redis", "OAuth 2.0"],
        "details": [
            "Base62 short links, custom aliases, link expiry, QR codes, and click analytics.",
            "JWT authentication and Google OAuth 2.0 with role-based access and admin features.",
            "Cache-Aside strategy reduced cached-link redirect latency from 200ms to 40–50ms.",
            "Deployed with Vercel, Render, Neon PostgreSQL, and Upstash Redis Cloud."
        ],
        "links": [{"label": "Live application", "url": "https://snip--ly.vercel.app"}]
    },
    {
        "number": "03", "name": "Redis-like In-Memory Database",
        "type": "Systems Programming",
        "description": "A Redis-compatible server built from scratch in Go, focused on event-driven networking and practical data structures.",
        "stack": ["Go", "Linux epoll", "TCP", "RESP2", "Skip List"],
        "details": [
            "Single-threaded event loop, non-blocking sockets, persistent TCP connections, and pipelining.",
            "Incremental RESP2 parsing with fragmented-packet handling and per-client buffers.",
            "50+ commands across strings, lists, hashes, sets, and sorted sets.",
            "AOF persistence, transactions, Pub/Sub, and LRU eviction.",
            "Benchmarked about 174K GET/sec and 65K SET/sec with 100K requests and 50 clients."
        ],
        "links": [{"label": "Source code", "url": "https://github.com/shivamkachawar/redis-clone"}]
    }
]

EXPERIENCE = [
    {
        "period": "JUN 2026 — PRESENT", "role": "Software Engineer",
        "company": "Algoquant Fintech Ltd", "location": "Bengaluru, India",
        "points": [
            "Built a Flask Kubernetes dashboard used daily by 12–15 people to inspect CPU and memory usage, pod logs, events, status, job history, and namespace usage history.",
            "Automated daily hardware audits across 150+ systems with Ansible and displayed inventory results in a Flask dashboard.",
            "Built an MCX open-position dashboard that parses Bash script output into JSON for a web UI.",
            "Built an NSE pre-open market dashboard that stores prices for 2,400+ equity and 400+ F&O instruments in PostgreSQL and graphs price history.",
            "Automated reconciliation across 2–3 exchange contract databases with Python, SQL, and cron, saving roughly one hour daily.",
            "Deployed and managed a production Kubernetes cluster with 23 bare-metal nodes, 1,590 CPU cores, and about 10 TiB RAM; also managed OpenStack infrastructure and monitoring."
        ]
    },
    {
        "period": "JAN 2026 — JUN 2026", "role": "DevOps Intern",
        "company": "Algoquant Fintech Ltd", "location": "Bengaluru, India",
        "points": ["Set up Wazuh, Observium, Greenbone, and OpenStack; load-tested RADIUS/pfSense login with Locust."]
    }
]

SKILLS = {
    "Languages": ["Java", "Go", "Python"],
    "Backend & Messaging": ["Spring Boot", "REST APIs", "Apache Kafka", "Redis", "JWT", "OAuth 2.0"],
    "Databases": ["PostgreSQL", "MySQL", "Firebase"],
    "Systems & Cloud": ["Linux", "Kubernetes", "OpenStack", "Docker", "Git"],
    "Computer Science": ["Data Structures & Algorithms", "System Design", "OOP", "DBMS", "Operating Systems", "Computer Networks"],
}

ACHIEVEMENTS = [
    ("1st Runner-Up", "HackFusion National Hackathon", "Paperless College Management System · Feb 2025"),
    ("1st Runner-Up", "HackSpectra National Hackathon", "Resume Tailoring & Job Matching Platform · Apr 2025"),
    ("1,150+", "DSA problems solved", "GeeksForGeeks, LeetCode, and takeUforward+"),
]

@app.route("/")
def index():
    return render_template("index.html", profile=PROFILE, projects=PROJECTS,
                           experience=EXPERIENCE, skills=SKILLS, achievements=ACHIEVEMENTS,
                           year=datetime.now().year)

@app.route("/api/profile")
def api_profile():
    return jsonify({"profile": PROFILE, "projects": PROJECTS, "skills": SKILLS})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
