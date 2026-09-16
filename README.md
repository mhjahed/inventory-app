<!-- INVENTORY MANAGEMENT APP · rose #fb7185 on #0d1117 · widgets verified 2026-09-12 -->

<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,100:fb7185&height=190&section=header&text=INVENTORY%20MANAGER&fontSize=54&fontColor=ffffff&animation=fadeIn&fontAlignY=36&desc=stock%20%C2%B7%20customers%20%C2%B7%20sales%20%C2%B7%20invoices%20%E2%80%94%20one%20synced%20ledger&descSize=16&descAlignY=60" alt="Inventory Manager" />

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=19&duration=2600&pause=900&color=FDA4AF&center=true&vCenter=true&width=780&height=95&lines=stock+%C2%B7+customers+%C2%B7+invoices;revenue+vs+expenses+%E2%80%94+synced+live;low-stock+alerts+%C2%B7+pdf+invoices" alt="typing" />

<p>
  <img src="https://img.shields.io/badge/django-backend-0d1117?style=for-the-badge&logo=django&logoColor=44b78b" alt="django" />
  <img src="https://img.shields.io/badge/postgresql-served-0d1117?style=for-the-badge&logo=postgresql&logoColor=336791" alt="postgres" />
  <img src="https://img.shields.io/badge/allauth-auth-0d1117?style=for-the-badge&logo=django&logoColor=fb7185" alt="allauth" />
  <img src="https://img.shields.io/badge/whitenoise-static-fb7185?style=for-the-badge&logoColor=white" alt="whitenoise" />
  <img src="https://img.shields.io/badge/license-MIT-0d1117?style=for-the-badge&logoColor=fb7185" alt="license" />
</p>

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:fb7185,100:0d1117&height=3" alt="" />

## ▍$ cat pitch.txt

Inventory, customers, sales, expenses and invoices — one application where every
number stays consistent because every module writes to the same ledger. A sale
adjusts stock, lands in the customer's history, updates revenue, and spawns a
printable invoice in one motion. Built for small shops, retail counters, and
warehouses that outgrew the spreadsheet.

```yaml
modules : items + categories · customers · sales · expenses · invoices
sync    : sale → stock−1 · purchase-history+ · revenue+ · invoice drafted
roles   : super admin · manager
alerts  : low-stock thresholds per item
deploy  : whitenoise static serving — heroku / vps / aws ready
```

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:fb7185,100:0d1117&height=3" alt="" />

## ▍$ ls modules/

| MODULE | CAPABILITY |
|---|---|
| `items` | add / edit / delete · categorize by type, brand, supplier · live stock levels |
| `stock-alerts` | automatic low-stock warnings |
| `customers` | profiles · purchase history · per-customer reports |
| `sales` | recorded sales auto-update inventory · daily / weekly / monthly revenue |
| `expenses` | purchases + operational costs tracked against revenue |
| `invoices` | auto-filled from items + customer · save + print as pdf · outstanding-payment tracking |

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:fb7185,100:0d1117&height=3" alt="" />

## ▍$ cat stack.json

<div align="center">
  <img src="https://skillicons.dev/icons?i=django,py,postgres,sqlite,js,html,css&perline=9" alt="stack" />
</div>

<br/>

| PIECE | TECH |
|---|---|
| backend | Python · Django · Django ORM |
| auth | django-allauth |
| fields | django-multiselectfield (categories) |
| assets | django-js-asset |
| static (prod) | whitenoise |
| db | sqlite (dev) · postgresql (prod) |
| frontend | HTML5 · CSS3 · JavaScript |

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:fb7185,100:0d1117&height=3" alt="" />

## ▍$ ./setup

```bash
git clone https://github.com/mhjahed/inventory-app.git && cd inventory-app
python -m venv .venv && source .venv/bin/activate   # windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser                    # optional
python manage.py runserver                          # → http://127.0.0.1:8000
```

## ▍$ tree .

```
inventory_app/
├── inventory/        items · customers · invoices
│   ├── templates/    html views
│   ├── static/       css · js · images
│   ├── models.py     items · customers · invoices
│   ├── views.py      business logic
│   ├── urls.py       routes
│   └── admin.py      admin configuration
├── manage.py
└── requirements.txt
```

<img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0:0d1117,50:fb7185,100:0d1117&height=3" alt="" />

## ▍$ grep -i next roadmap.txt

- ▸ auto-email invoices to customers on sale
- ▸ barcode scanner integration for stock ops
- ▸ analytics dashboard — trends, profit & loss curves
- ▸ multi-warehouse support

<br/>

<div align="center">

`one ledger — stock, money and paperwork never disagree`
`built end-to-end by` **[MH JAHED](https://github.com/mhjahed)** · `mhjahed@proton.me`

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:fb7185,100:0d1117&height=110&section=footer" alt="" />
