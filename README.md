# career_plan_agents_classic

โปรเจกต์ CrewAI แบบ Classic/YAML สำหรับสร้างแผนพัฒนาอาชีพ (Career Development Plan)
รองรับทั้ง Ollama Local LLM และ Google Gemini API

## โครงสร้างโปรเจกต์

career_plan_agents_classic/
├── .env                # ตั้งค่าเอง (ห้าม commit ไฟล์นี้)
├── .env.example        # ตัวอย่างการตั้งค่า
├── pyproject.toml
├── README.md
├── knowledge/
├── output/             # ผลลัพธ์ report.md จะถูกเขียนที่นี่
└── src/
    └── career_plan_agents_classic/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        └── config/
            ├── agents.yaml
            └── tasks.yaml

## ติดตั้ง

```bash
cd career_plan_agents_classic
cp .env.example .env   # แล้วแก้ค่าใน .env ตามต้องการ
crewai install
# หรือ
uv sync
```

## ใช้กับ Ollama Local

1. ติดตั้งและรัน Ollama, ดาวน์โหลด model เช่น `ollama run llama3:latest`
2. ตั้งค่าใน `.env`:
MODEL=ollama/llama3
OLLAMA_BASE_URL=http://localhost:11434

## ใช้กับ Google Gemini API

1. สร้าง API key ที่ https://aistudio.google.com/
2. ตั้งค่าใน `.env`:
GOOGLE_API_KEY=your_gemini_api_key_here
MODEL=gemini/gemini-2.0-flash

## รันโปรเจกต์

```bash
crewai run
# หรือ
uv run career_plan_agents
```

ผลลัพธ์สุดท้ายจะถูกเขียนไปที่ `output/career_plan_report.md`