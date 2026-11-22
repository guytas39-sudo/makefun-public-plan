import os

PLAN = (
    "Day 1: list a $25 Fiverr gig, 'Etsy SEO rescue': rewrite 20 Etsy "
    "listings in 24h. Skip Fiverr search - DM 30 sellers daily, free "
    "3-listing sample. 4 orders/day = $80/day net, ~$2,000 by day 30; no "
    "ads until 5 reviews. Reinvest earnings; no orders in 3 days? Pivot to "
    "Shopify."
)

assert 1 <= len(PLAN) <= 280, f"plan is {len(PLAN)} chars, must be 1-280"
assert PLAN.strip(), "plan must not be only whitespace"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)

print(f"Wrote {len(PLAN)} chars to {os.path.join(out_dir, 'entry.txt')}")
