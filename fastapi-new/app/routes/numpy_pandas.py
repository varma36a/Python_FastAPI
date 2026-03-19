from fastapi import APIRouter, Body
import numpy as np
import pandas as pd

router = APIRouter(prefix="/numpy_pandas", tags=["Set Exercises"])

# =========================
# 🔷 NUMPY ROUTES
# =========================


@router.post("/numpy/basic")
def numpy_basic(numbers: list = Body(...)):
    arr = np.array(numbers)
    return {
        "array": arr.tolist(),
        "sum": int(arr.sum()),
        "mean": float(arr.mean()),
        "max": int(arr.max()),
    }


@router.post("/numpy/matrix")
def matrix_multiply(a: list = Body(...), b: list = Body(...)):
    arr1 = np.array(a)
    arr2 = np.array(b)
    result = np.dot(arr1, arr2)
    return {"result": result.tolist()}


@router.get("/numpy/random")
def random_array(rows: int, cols: int):
    arr = np.random.randint(100, 500, size=(rows, cols))
    return {"array": arr.tolist(), "shape": arr.shape}


@router.post("/numpy/normalize")
def normalize(numbers: list = Body(...)):
    arr = np.array(numbers)
    norm = (arr - arr.min()) / (arr.max() - arr.min())
    return {"normalized": norm.tolist()}


@router.post("/numpy/stats")
def stats(numbers: list = Body(...)):
    arr = np.array(numbers)
    return {
        "mean": float(arr.mean()),
        "std": float(arr.std()),
        "variance": float(arr.var()),
    }


# =========================
# 🔷 PANDAS ROUTES
# =========================


@router.post("/pandas/create")
def create_df(data: list = Body(...)):
    df = pd.DataFrame(data)
    return {
        "columns": df.columns.tolist(),
        "shape": df.shape,
        "preview": df.head().to_dict(orient="records"),
    }


@router.post("/pandas/filter")
def filter_data(
    data: list = Body(...), column: str = Body(...), value: float = Body(...)
):
    df = pd.DataFrame(data)
    filtered = df[df[column] > value]
    return filtered.to_dict(orient="records")


@router.post("/pandas/groupby")
def groupby_data(
    data: list = Body(...), group_col: str = Body(...), agg_col: str = Body(...)
):
    df = pd.DataFrame(data)
    result = df.groupby(group_col)[agg_col].mean()
    return result.to_dict()


@router.post("/pandas/fillna")
def fill_missing(data: list = Body(...)):
    df = pd.DataFrame(data)
    df_filled = df.fillna(0)
    return df_filled.to_dict(orient="records")


@router.post("/pandas/sort")
def sort_data(data: list = Body(...), column: str = Body(...)):
    df = pd.DataFrame(data)
    sorted_df = df.sort_values(by=column)
    return sorted_df.to_dict(orient="records")


@router.post("/pandas/stats")
def describe_data(data: list = Body(...)):
    df = pd.DataFrame(data)
    return df.describe().to_dict()


# =========================
# 🔷 COMBINED REAL TASKS
# =========================


@router.post("/analytics/sales")
def sales_analysis(data: list = Body(...)):
    df = pd.DataFrame(data)

    total_sales = df["sales"].sum()
    avg_sales = df["sales"].mean()
    top_product = df.loc[df["sales"].idxmax()]["product"]

    return {
        "total_sales": float(total_sales),
        "avg_sales": float(avg_sales),
        "top_product": top_product,
    }


@router.post("/analytics/normalize")
def normalize_dataset(data: list = Body(...), column: str = Body(...)):
    df = pd.DataFrame(data)

    arr = df[column].values
    df[column] = (arr - arr.min()) / (arr.max() - arr.min())

    return df.to_dict(orient="records")


# =========================
# 🔷 BONUS
# =========================


@router.post("/pandas/join")
def join_data(left: list = Body(...), right: list = Body(...), on: str = Body(...)):
    df1 = pd.DataFrame(left)
    df2 = pd.DataFrame(right)

    merged = pd.merge(df1, df2, on=on)
    return merged.to_dict(orient="records")


@router.get("/health")
def health_check():
    return {"status": "Practice API running 🚀"}
