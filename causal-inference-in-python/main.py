{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "681c01a7-987f-4232-b1a2-caa03710bd70",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   t  x    y\n",
      "0  0  0  200\n",
      "1  0  0  120\n",
      "2  0  1  300\n",
      "3  1  0  500\n",
      "4  1  0  600\n",
      "5  1  1  800\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "def generate_data() -> pd.DataFrame: \n",
    "    data = {\n",
    "        \"t\": [0,0,0,1,1,1],\n",
    "        \"x\": [0,0,1,0,0,1],\n",
    "        \"y\": [200,120,300,500,600,800]\n",
    "    }\n",
    "    \n",
    "    return pd.DataFrame(data)\n",
    "\n",
    "df = generate_data()\n",
    "\n",
    "print(df)"
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
