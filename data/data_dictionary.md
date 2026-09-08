# Data dictionary

Each CSV contains one year of five-minute SEND campus energy data.

| Column | Meaning | Unit |
| --- | --- | --- |
| `DateTime` | Date and time of the observation, as supplied in the source dataset | Not applicable |
| `power-con-ave` | Average campus electricity consumption | kW |
| `power-gen-wt-ave` | Average wind-turbine electricity generation | kW |
| `power-gen-pv-ave` | Average solar photovoltaic electricity generation | kW |

All three files use the column order shown above: `DateTime`, `power-con-ave`, `power-gen-wt-ave`, then `power-gen-pv-ave`.

## How to read a row

The three power columns record average power in kilowatts during a five-minute interval. Power describes the rate at which electricity is being consumed or generated. Energy describes the amount accumulated over time.

Convert a series of five-minute average power readings to megawatt-hours with:

```text
Energy in MWh = sum of power readings in kW / 12,000
```

The divisor combines the five-minute interval and the conversion from kilowatt-hours to megawatt-hours.

## Derived values

These calculations are useful for the hackathon:

```text
generation_kW = power-gen-wt-ave + power-gen-pv-ave
balance_kW = generation_kW - power-con-ave
excess_kW = max(balance_kW, 0)
shortfall_kW = max(-balance_kW, 0)
```

A positive balance means renewable generation is greater than campus demand during that interval. A negative balance means demand is greater than renewable generation.

## Dataset provenance

- The 2023 file is the reviewed and repaired annual dataset.
- The 2024 and 2025 files are reconstructed annual datasets. They are not untouched raw meter exports.

Treat year-to-year differences with care. A difference may reflect physical conditions, campus operation, data preparation or a combination of these.

## Data-quality checks

- Check the timestamp sequence before assuming that every expected interval is present.
- Do not treat every zero as missing data or failure.
- Solar generation at night should normally be zero.
- A wind value of zero may have several possible explanations.
- A long run of zero campus consumption needs investigation before it is used in an excess-energy calculation.
