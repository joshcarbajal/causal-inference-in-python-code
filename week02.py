{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e6e9a43f-c22e-4af5-90bc-bba60fc1e2e5",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'pd' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mcalculate_ate_ci\u001b[39m(data: \u001b[43mpd\u001b[49m\u001b[38;5;241m.\u001b[39mDataFrame, alpha: \u001b[38;5;28mfloat\u001b[39m \u001b[38;5;241m=\u001b[39m \u001b[38;5;241m0.05\u001b[39m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Tuple[\u001b[38;5;28mfloat\u001b[39m, \u001b[38;5;28mfloat\u001b[39m, \u001b[38;5;28mfloat\u001b[39m]:\n\u001b[0;32m      2\u001b[0m     treated \u001b[38;5;241m=\u001b[39m data[data[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mT\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m1\u001b[39m][\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mY\u001b[39m\u001b[38;5;124m'\u001b[39m]\n\u001b[0;32m      3\u001b[0m     control \u001b[38;5;241m=\u001b[39m data[data[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mT\u001b[39m\u001b[38;5;124m'\u001b[39m] \u001b[38;5;241m==\u001b[39m \u001b[38;5;241m0\u001b[39m][\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mY\u001b[39m\u001b[38;5;124m'\u001b[39m]\n",
      "\u001b[1;31mNameError\u001b[0m: name 'pd' is not defined"
     ]
    }
   ],
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
    "    return ate, ci_lower, ci_upper\n",
    "def calculate_ate_pvalue(data: pd.DataFrame) -> Tuple[float, float, float]:\n",
    "    treated = data[data['T'] == 1]['Y']\n",
    "    control = data[data['T'] == 0]['Y']\n",
    "    n1, n0 = len(treated), len(control)\n",
    "    ate = treated.mean() - control.mean()\n",
    "    se = np.sqrt(treated.var(ddof=1)/n1 + control.var(ddof=1)/n0)\n",
    "    t_stat = ate / se\n",
    "    p_value = 2 * (1 - norm.cdf(abs(t_stat)))\n",
    "    return ate, t_stat, p_value\n"
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
