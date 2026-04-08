{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53a652ab-c681-4ee1-ad9e-98343721748b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy import stats\n",
    "from typing import Tuple\n",
    "\n",
    "def calculate_ate_ci(data: pd.DataFrame, alpha: float = 0.05) -> Tuple[float, float, float]:\n",
    "    \n",
    "    y1 = data[data['T'] == 1]['Y']\n",
    "    y0 = data[data['T'] == 0]['Y']\n",
    "    \n",
    "    mean1 = y1.mean()\n",
    "    mean0 = y0.mean()\n",
    "    \n",
    "    ate_estimate = mean1 - mean0\n",
    "\n",
    "    se_ate = np.sqrt(y1.var(ddof=1) / len(y1) + y0.var(ddof=1) / len(y0))\n",
    "    \n",
    "    z_score = stats.norm.ppf(1 - alpha / 2)\n",
    "    \n",
    "    ci_lower = ate_estimate - z_score * se_ate\n",
    "    ci_upper = ate_estimate + z_score * se_ate\n",
    "    \n",
    "    return float(ate_estimate), float(ci_lower), float(ci_upper)\n",
    "\n",
    "def calculate_ate_pvalue(data: pd.DataFrame) -> Tuple[float, float, float]:\n",
    "\n",
    "    y1 = data[data['T'] == 1]['Y']\n",
    "    y0 = data[data['T'] == 0]['Y']\n",
    "    \n",
    "    ate_estimate = y1.mean() - y0.mean()\n",
    "    \n",
    "    se_ate = np.sqrt(y1.var(ddof=1) / len(y1) + y0.var(ddof=1) / len(y0))\n",
    "    \n",
    "    t_stat = ate_estimate / se_ate\n",
    "\n",
    "    p_value = 2 * (1 - stats.norm.cdf(abs(t_stat)))\n",
    "    \n",
    "    return float(ate_estimate), float(t_stat), float(p_value)"
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
