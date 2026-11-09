# 🚗 Bolt Ride-Hailing Driver Incentive Allocation & Strategy Model

This repository contains an end-to-end data analytics and driver allocation model built for **Bolt (Estonia)** to evaluate and deploy a targeted weekly attendance incentive campaign.

The objective of the campaign is to **maximize driver online hours and supply availability** for next week while strictly optimizing incentive ROI across different driver segments.

---

## 📌 Executive Summary & Allocation Breakdown

Based on driver behavior patterns and schedule elasticity, the driver fleet ($N = 1,000$) has been categorized into four strategic tiers:

| Tier | Daily Hours Threshold | Targeted Reward % | Total Drivers | Eligible Winners | Strategy & Executive Rationale |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Tier 1** | `< 3 hrs / day` | **0%** | 272 | **0** | **Eliminate Waste**: Drivers have primary jobs elsewhere; incentive elasticity is near zero. |
| **Tier 2** | `3 - 6 hrs / day` | **80%** | 433 | **346** | **Growth Engine**: Highest schedule elasticity. 80% quota maximizes conversion to full-time supply. |
| **Tier 3** | `6 - 8 hrs / day` | **40%** | 188 | **75** | **Consolidation**: Moderate allocation to sustain supply and encourage shift extension. |
| **Tier 4** | `>= 8 hrs / day` | **20%** | 107 | **21** | **Budget Control**: Core full-timers stay online regardless. Capped at 20% to prevent over-subsidization. |
| **Total** | **Fleet-wide** | **44.2%** | **1,000** | **442** | **High-precision targeting covering 44.2% of total fleet.** |

---

## 🎯 Key Strategic Insights for Management

1. **Budget Efficiency & ROI**:
   By excluding **Tier 1** (<3h/day), the model prevents ~$10,000+ in inefficient spend and concentrates capital into **Tier 2**, where incremental hours per incentive Euro are highest.
2. **Quality & Service-Weighted Ranking**:
   For tiers with fractional quotas (e.g., 80%, 40%, 20%), candidate selection is executed using a multi-factor score:
   $$\text{Selection Score} = 0.60 \times \text{Driver Rating} + 0.40 \times \left( \frac{\text{Weekly Hours}}{\text{Max Hours}} \right)$$
   This ensures top-rated, reliable drivers are prioritized for rewards.
3. **Behavioral Gamification Recommendation**:
   For **Tier 2 (3-6h/day)** drivers receiving next week's campaign notification, we recommend adding a stretch target (e.g., *"Complete 25+ hours next week to unlock an extra €15 bonus"*), accelerating their transition into core full-time drivers.

---

## 📁 Repository Contents

* `models/Bolt_Driver_Incentive_Allocation_Model_EN_v3.xlsx`: Complete Excel financial and operational model featuring an Executive Dashboard, clear metrics, and dynamic driver-level allocation.
* `scripts/incentive_allocation.py`: Automated Python data analysis and tier assignment script.
* `data/bolt_driver_weekly_attendance_incentives-v2.csv`: Raw driver dataset containing weekly working hours, ratings, and baseline earnings.
* `README.md`: Project documentation and executive presentation.
