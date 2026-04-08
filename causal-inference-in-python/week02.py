{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "4e03ba1c-fcc9-4dba-992e-4db6b52b2a73",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy.stats import norm\n",
    "from typing import Tuple\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e6e9a43f-c22e-4af5-90bc-bba60fc1e2e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_ate_ci(data: pd.DataFrame, alpha: float = 0.05) -> Tuple[float, float, float]:\n",
    "    treated = data[data['T'] == 1]['Y']\n",
    "    control = data[data['T'] == 0]['Y']\n",
    "    n1, n0 = len(treated), len(control)\n",
    "    ate = treated.mean() - control.mean()\n",
    "    se = np.sqrt(treated.var(ddof=1)/n1 + control.var(ddof=1)/n0)\n",
    "    z = norm.ppf(1 - alpha/2)\n",
    "    ci_lower = ate - z * se\n",
    "    ci_upper = ate + z * se\n",
    "    return ate, ci_lower, ci_upper\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a0eb0104-aba5-432e-9897-0db1e225a3ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "def calculate_ate_pvalue(data: pd.DataFrame) -> Tuple[float, float, float]:\n",
    "    treated = data[data['T'] == 1]['Y']\n",
    "    control = data[data['T'] == 0]['Y']\n",
    "    n1, n0 = len(treated), len(control)\n",
    "    ate = treated.mean() - control.mean()\n",
    "    se = np.sqrt(treated.var(ddof=1)/n1 + control.var(ddof=1)/n0)\n",
    "    t_stat = ate / se\n",
    "    p_value = 2 * (1 - norm.cdf(abs(t_stat)))\n",
    "    return ate, t_stat, p_value"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
