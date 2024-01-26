{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMOH99AOZjEUXWIdtwIXQeU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Priyapan65/CODSOFT/blob/main/codsoft_task_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Task 1\n",
        "##Titanic Survival Prediction\n",
        "##Import required dependencies\n"
      ],
      "metadata": {
        "id": "bQXRRX7ByhyH"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "uploaded=files.upload()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 73
        },
        "id": "fDnbG2bryzLC",
        "outputId": "6c86e805-4358-4255-d1e4-04baef39ddab"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-2fffc459-dbca-483e-b2f9-786baca1e703\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-2fffc459-dbca-483e-b2f9-786baca1e703\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving tested.csv to tested.csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import os\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report\n",
        "from sklearn.linear_model import LogisticRegression"
      ],
      "metadata": {
        "id": "PNrM8u2dyD0G"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "wsQ6Muz0zCDt"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "t_data = pd.read_csv(\"tested.csv\")"
      ],
      "metadata": {
        "id": "MWHEBIG9yJ4p"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "Ox3438pkyY7a",
        "outputId": "3f6ad37a-6ed3-4a05-8854-14586a523416"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     PassengerId  Survived  Pclass  \\\n",
              "0            892         0       3   \n",
              "1            893         1       3   \n",
              "2            894         0       2   \n",
              "3            895         0       3   \n",
              "4            896         1       3   \n",
              "..           ...       ...     ...   \n",
              "413         1305         0       3   \n",
              "414         1306         1       1   \n",
              "415         1307         0       3   \n",
              "416         1308         0       3   \n",
              "417         1309         0       3   \n",
              "\n",
              "                                             Name     Sex   Age  SibSp  Parch  \\\n",
              "0                                Kelly, Mr. James    male  34.5      0      0   \n",
              "1                Wilkes, Mrs. James (Ellen Needs)  female  47.0      1      0   \n",
              "2                       Myles, Mr. Thomas Francis    male  62.0      0      0   \n",
              "3                                Wirz, Mr. Albert    male  27.0      0      0   \n",
              "4    Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.0      1      1   \n",
              "..                                            ...     ...   ...    ...    ...   \n",
              "413                            Spector, Mr. Woolf    male   NaN      0      0   \n",
              "414                  Oliva y Ocana, Dona. Fermina  female  39.0      0      0   \n",
              "415                  Saether, Mr. Simon Sivertsen    male  38.5      0      0   \n",
              "416                           Ware, Mr. Frederick    male   NaN      0      0   \n",
              "417                      Peter, Master. Michael J    male   NaN      1      1   \n",
              "\n",
              "                 Ticket      Fare Cabin Embarked  \n",
              "0                330911    7.8292   NaN        Q  \n",
              "1                363272    7.0000   NaN        S  \n",
              "2                240276    9.6875   NaN        Q  \n",
              "3                315154    8.6625   NaN        S  \n",
              "4               3101298   12.2875   NaN        S  \n",
              "..                  ...       ...   ...      ...  \n",
              "413           A.5. 3236    8.0500   NaN        S  \n",
              "414            PC 17758  108.9000  C105        C  \n",
              "415  SOTON/O.Q. 3101262    7.2500   NaN        S  \n",
              "416              359309    8.0500   NaN        S  \n",
              "417                2668   22.3583   NaN        C  \n",
              "\n",
              "[418 rows x 12 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-1c3262a8-d216-4e10-b179-3019ff35a670\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Name</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>SibSp</th>\n",
              "      <th>Parch</th>\n",
              "      <th>Ticket</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Embarked</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>892</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Kelly, Mr. James</td>\n",
              "      <td>male</td>\n",
              "      <td>34.5</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>330911</td>\n",
              "      <td>7.8292</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Q</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>893</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Wilkes, Mrs. James (Ellen Needs)</td>\n",
              "      <td>female</td>\n",
              "      <td>47.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>363272</td>\n",
              "      <td>7.0000</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>894</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>Myles, Mr. Thomas Francis</td>\n",
              "      <td>male</td>\n",
              "      <td>62.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>240276</td>\n",
              "      <td>9.6875</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Q</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>895</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Wirz, Mr. Albert</td>\n",
              "      <td>male</td>\n",
              "      <td>27.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>315154</td>\n",
              "      <td>8.6625</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>896</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>\n",
              "      <td>female</td>\n",
              "      <td>22.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>3101298</td>\n",
              "      <td>12.2875</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>413</th>\n",
              "      <td>1305</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Spector, Mr. Woolf</td>\n",
              "      <td>male</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>A.5. 3236</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>414</th>\n",
              "      <td>1306</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Oliva y Ocana, Dona. Fermina</td>\n",
              "      <td>female</td>\n",
              "      <td>39.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>PC 17758</td>\n",
              "      <td>108.9000</td>\n",
              "      <td>C105</td>\n",
              "      <td>C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>415</th>\n",
              "      <td>1307</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Saether, Mr. Simon Sivertsen</td>\n",
              "      <td>male</td>\n",
              "      <td>38.5</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>SOTON/O.Q. 3101262</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>416</th>\n",
              "      <td>1308</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Ware, Mr. Frederick</td>\n",
              "      <td>male</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>359309</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>417</th>\n",
              "      <td>1309</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Peter, Master. Michael J</td>\n",
              "      <td>male</td>\n",
              "      <td>NaN</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2668</td>\n",
              "      <td>22.3583</td>\n",
              "      <td>NaN</td>\n",
              "      <td>C</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>418 rows × 12 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-1c3262a8-d216-4e10-b179-3019ff35a670')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-1c3262a8-d216-4e10-b179-3019ff35a670 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-1c3262a8-d216-4e10-b179-3019ff35a670');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-ffef3a1b-084f-44cd-8424-9e3038974a49\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-ffef3a1b-084f-44cd-8424-9e3038974a49')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-ffef3a1b-084f-44cd-8424-9e3038974a49 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 4
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##learning about the data set"
      ],
      "metadata": {
        "id": "3bd7Tb43zJh2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.head()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "eCHKOWMwyba3",
        "outputId": "ed8e4824-655c-4625-c3e0-a6a19aec58a3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   PassengerId  Survived  Pclass  \\\n",
              "0          892         0       3   \n",
              "1          893         1       3   \n",
              "2          894         0       2   \n",
              "3          895         0       3   \n",
              "4          896         1       3   \n",
              "\n",
              "                                           Name     Sex   Age  SibSp  Parch  \\\n",
              "0                              Kelly, Mr. James    male  34.5      0      0   \n",
              "1              Wilkes, Mrs. James (Ellen Needs)  female  47.0      1      0   \n",
              "2                     Myles, Mr. Thomas Francis    male  62.0      0      0   \n",
              "3                              Wirz, Mr. Albert    male  27.0      0      0   \n",
              "4  Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.0      1      1   \n",
              "\n",
              "    Ticket     Fare Cabin Embarked  \n",
              "0   330911   7.8292   NaN        Q  \n",
              "1   363272   7.0000   NaN        S  \n",
              "2   240276   9.6875   NaN        Q  \n",
              "3   315154   8.6625   NaN        S  \n",
              "4  3101298  12.2875   NaN        S  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-ed63a38d-3f02-4daa-a32d-cb4776cb4420\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Name</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>SibSp</th>\n",
              "      <th>Parch</th>\n",
              "      <th>Ticket</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Embarked</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>892</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Kelly, Mr. James</td>\n",
              "      <td>male</td>\n",
              "      <td>34.5</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>330911</td>\n",
              "      <td>7.8292</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Q</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>893</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Wilkes, Mrs. James (Ellen Needs)</td>\n",
              "      <td>female</td>\n",
              "      <td>47.0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>363272</td>\n",
              "      <td>7.0000</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>894</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>Myles, Mr. Thomas Francis</td>\n",
              "      <td>male</td>\n",
              "      <td>62.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>240276</td>\n",
              "      <td>9.6875</td>\n",
              "      <td>NaN</td>\n",
              "      <td>Q</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>895</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Wirz, Mr. Albert</td>\n",
              "      <td>male</td>\n",
              "      <td>27.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>315154</td>\n",
              "      <td>8.6625</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>896</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>\n",
              "      <td>female</td>\n",
              "      <td>22.0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>3101298</td>\n",
              "      <td>12.2875</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-ed63a38d-3f02-4daa-a32d-cb4776cb4420')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-ed63a38d-3f02-4daa-a32d-cb4776cb4420 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-ed63a38d-3f02-4daa-a32d-cb4776cb4420');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-971c140e-48ef-45f5-9073-0e5952efc7b1\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-971c140e-48ef-45f5-9073-0e5952efc7b1')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-971c140e-48ef-45f5-9073-0e5952efc7b1 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.tail()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 206
        },
        "id": "eiHu9eHbzrFy",
        "outputId": "8808ca0b-18af-46f7-b383-727d972d8d94"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     PassengerId  Survived  Pclass                          Name     Sex  \\\n",
              "413         1305         0       3            Spector, Mr. Woolf    male   \n",
              "414         1306         1       1  Oliva y Ocana, Dona. Fermina  female   \n",
              "415         1307         0       3  Saether, Mr. Simon Sivertsen    male   \n",
              "416         1308         0       3           Ware, Mr. Frederick    male   \n",
              "417         1309         0       3      Peter, Master. Michael J    male   \n",
              "\n",
              "      Age  SibSp  Parch              Ticket      Fare Cabin Embarked  \n",
              "413   NaN      0      0           A.5. 3236    8.0500   NaN        S  \n",
              "414  39.0      0      0            PC 17758  108.9000  C105        C  \n",
              "415  38.5      0      0  SOTON/O.Q. 3101262    7.2500   NaN        S  \n",
              "416   NaN      0      0              359309    8.0500   NaN        S  \n",
              "417   NaN      1      1                2668   22.3583   NaN        C  "
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-32ad3207-0cb4-4ef8-b650-4f6592f7273d\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Name</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>SibSp</th>\n",
              "      <th>Parch</th>\n",
              "      <th>Ticket</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Cabin</th>\n",
              "      <th>Embarked</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>413</th>\n",
              "      <td>1305</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Spector, Mr. Woolf</td>\n",
              "      <td>male</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>A.5. 3236</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>414</th>\n",
              "      <td>1306</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Oliva y Ocana, Dona. Fermina</td>\n",
              "      <td>female</td>\n",
              "      <td>39.0</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>PC 17758</td>\n",
              "      <td>108.9000</td>\n",
              "      <td>C105</td>\n",
              "      <td>C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>415</th>\n",
              "      <td>1307</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Saether, Mr. Simon Sivertsen</td>\n",
              "      <td>male</td>\n",
              "      <td>38.5</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>SOTON/O.Q. 3101262</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>416</th>\n",
              "      <td>1308</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Ware, Mr. Frederick</td>\n",
              "      <td>male</td>\n",
              "      <td>NaN</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>359309</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>NaN</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>417</th>\n",
              "      <td>1309</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Peter, Master. Michael J</td>\n",
              "      <td>male</td>\n",
              "      <td>NaN</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2668</td>\n",
              "      <td>22.3583</td>\n",
              "      <td>NaN</td>\n",
              "      <td>C</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-32ad3207-0cb4-4ef8-b650-4f6592f7273d')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-32ad3207-0cb4-4ef8-b650-4f6592f7273d button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-32ad3207-0cb4-4ef8-b650-4f6592f7273d');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-6fdf1147-a06f-4ea2-8c18-bb7301053331\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-6fdf1147-a06f-4ea2-8c18-bb7301053331')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-6fdf1147-a06f-4ea2-8c18-bb7301053331 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7GuLw0YIzu28",
        "outputId": "efe03c18-5d45-4537-f6d9-853cbda8082b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(418, 12)"
            ]
          },
          "metadata": {},
          "execution_count": 7
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3fcv0nvqz5Mc",
        "outputId": "5c02b736-b74f-440d-c116-d524f862fcf3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 418 entries, 0 to 417\n",
            "Data columns (total 12 columns):\n",
            " #   Column       Non-Null Count  Dtype  \n",
            "---  ------       --------------  -----  \n",
            " 0   PassengerId  418 non-null    int64  \n",
            " 1   Survived     418 non-null    int64  \n",
            " 2   Pclass       418 non-null    int64  \n",
            " 3   Name         418 non-null    object \n",
            " 4   Sex          418 non-null    object \n",
            " 5   Age          332 non-null    float64\n",
            " 6   SibSp        418 non-null    int64  \n",
            " 7   Parch        418 non-null    int64  \n",
            " 8   Ticket       418 non-null    object \n",
            " 9   Fare         417 non-null    float64\n",
            " 10  Cabin        91 non-null     object \n",
            " 11  Embarked     418 non-null    object \n",
            "dtypes: float64(2), int64(5), object(5)\n",
            "memory usage: 39.3+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "LGue73S6z83n",
        "outputId": "226891a0-5d70-45a2-ab05-319205506245"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "PassengerId      0\n",
              "Survived         0\n",
              "Pclass           0\n",
              "Name             0\n",
              "Sex              0\n",
              "Age             86\n",
              "SibSp            0\n",
              "Parch            0\n",
              "Ticket           0\n",
              "Fare             1\n",
              "Cabin          327\n",
              "Embarked         0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##we need to handle missing values"
      ],
      "metadata": {
        "id": "m8q3cXZw0D4n"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# to handle missing values in the cabin column we will drop it as they are numerous"
      ],
      "metadata": {
        "id": "lV0rEnoQ0BEy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.drop(columns='Cabin', axis=1, inplace=True)"
      ],
      "metadata": {
        "id": "4RDdK_2l0IKM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# to handle missing values in the age and fare column we will replace them with the mean age and fare"
      ],
      "metadata": {
        "id": "VtNgKCMs0MMl"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Age = t_data['Age'].mean()"
      ],
      "metadata": {
        "id": "nOxGrfiY0PVs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data['Age'].fillna(Age, inplace = True)"
      ],
      "metadata": {
        "id": "JsExrT6L0S86"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Fare = t_data['Fare'].mean()"
      ],
      "metadata": {
        "id": "QvJyKfWS0ZlL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data['Fare'].fillna(Fare, inplace = True)"
      ],
      "metadata": {
        "id": "bdNlgdJI0dB0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.info()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aCr1fpZS0gdd",
        "outputId": "161add96-f1c0-42c3-f05f-7f241b54d264"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 418 entries, 0 to 417\n",
            "Data columns (total 11 columns):\n",
            " #   Column       Non-Null Count  Dtype  \n",
            "---  ------       --------------  -----  \n",
            " 0   PassengerId  418 non-null    int64  \n",
            " 1   Survived     418 non-null    int64  \n",
            " 2   Pclass       418 non-null    int64  \n",
            " 3   Name         418 non-null    object \n",
            " 4   Sex          418 non-null    object \n",
            " 5   Age          418 non-null    float64\n",
            " 6   SibSp        418 non-null    int64  \n",
            " 7   Parch        418 non-null    int64  \n",
            " 8   Ticket       418 non-null    object \n",
            " 9   Fare         418 non-null    float64\n",
            " 10  Embarked     418 non-null    object \n",
            "dtypes: float64(2), int64(5), object(4)\n",
            "memory usage: 36.0+ KB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Our data is now consistent"
      ],
      "metadata": {
        "id": "Wyw3-dxX0klQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "dw0ZXg2s0nb_",
        "outputId": "fb0f14dd-1c79-4af9-9a18-fc6f658aa4ed"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     PassengerId  Survived  Pclass  \\\n",
              "0            892         0       3   \n",
              "1            893         1       3   \n",
              "2            894         0       2   \n",
              "3            895         0       3   \n",
              "4            896         1       3   \n",
              "..           ...       ...     ...   \n",
              "413         1305         0       3   \n",
              "414         1306         1       1   \n",
              "415         1307         0       3   \n",
              "416         1308         0       3   \n",
              "417         1309         0       3   \n",
              "\n",
              "                                             Name     Sex       Age  SibSp  \\\n",
              "0                                Kelly, Mr. James    male  34.50000      0   \n",
              "1                Wilkes, Mrs. James (Ellen Needs)  female  47.00000      1   \n",
              "2                       Myles, Mr. Thomas Francis    male  62.00000      0   \n",
              "3                                Wirz, Mr. Albert    male  27.00000      0   \n",
              "4    Hirvonen, Mrs. Alexander (Helga E Lindqvist)  female  22.00000      1   \n",
              "..                                            ...     ...       ...    ...   \n",
              "413                            Spector, Mr. Woolf    male  30.27259      0   \n",
              "414                  Oliva y Ocana, Dona. Fermina  female  39.00000      0   \n",
              "415                  Saether, Mr. Simon Sivertsen    male  38.50000      0   \n",
              "416                           Ware, Mr. Frederick    male  30.27259      0   \n",
              "417                      Peter, Master. Michael J    male  30.27259      1   \n",
              "\n",
              "     Parch              Ticket      Fare Embarked  \n",
              "0        0              330911    7.8292        Q  \n",
              "1        0              363272    7.0000        S  \n",
              "2        0              240276    9.6875        Q  \n",
              "3        0              315154    8.6625        S  \n",
              "4        1             3101298   12.2875        S  \n",
              "..     ...                 ...       ...      ...  \n",
              "413      0           A.5. 3236    8.0500        S  \n",
              "414      0            PC 17758  108.9000        C  \n",
              "415      0  SOTON/O.Q. 3101262    7.2500        S  \n",
              "416      0              359309    8.0500        S  \n",
              "417      1                2668   22.3583        C  \n",
              "\n",
              "[418 rows x 11 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-80fd5eaf-f53f-4ec5-a2f1-7a41f742f6b7\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Name</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>SibSp</th>\n",
              "      <th>Parch</th>\n",
              "      <th>Ticket</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Embarked</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>892</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Kelly, Mr. James</td>\n",
              "      <td>male</td>\n",
              "      <td>34.50000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>330911</td>\n",
              "      <td>7.8292</td>\n",
              "      <td>Q</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>893</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Wilkes, Mrs. James (Ellen Needs)</td>\n",
              "      <td>female</td>\n",
              "      <td>47.00000</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>363272</td>\n",
              "      <td>7.0000</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>894</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>Myles, Mr. Thomas Francis</td>\n",
              "      <td>male</td>\n",
              "      <td>62.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>240276</td>\n",
              "      <td>9.6875</td>\n",
              "      <td>Q</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>895</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Wirz, Mr. Albert</td>\n",
              "      <td>male</td>\n",
              "      <td>27.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>315154</td>\n",
              "      <td>8.6625</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>896</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>\n",
              "      <td>female</td>\n",
              "      <td>22.00000</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>3101298</td>\n",
              "      <td>12.2875</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>413</th>\n",
              "      <td>1305</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Spector, Mr. Woolf</td>\n",
              "      <td>male</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>A.5. 3236</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>414</th>\n",
              "      <td>1306</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Oliva y Ocana, Dona. Fermina</td>\n",
              "      <td>female</td>\n",
              "      <td>39.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>PC 17758</td>\n",
              "      <td>108.9000</td>\n",
              "      <td>C</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>415</th>\n",
              "      <td>1307</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Saether, Mr. Simon Sivertsen</td>\n",
              "      <td>male</td>\n",
              "      <td>38.50000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>SOTON/O.Q. 3101262</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>416</th>\n",
              "      <td>1308</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Ware, Mr. Frederick</td>\n",
              "      <td>male</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>359309</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>S</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>417</th>\n",
              "      <td>1309</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Peter, Master. Michael J</td>\n",
              "      <td>male</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2668</td>\n",
              "      <td>22.3583</td>\n",
              "      <td>C</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>418 rows × 11 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-80fd5eaf-f53f-4ec5-a2f1-7a41f742f6b7')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-80fd5eaf-f53f-4ec5-a2f1-7a41f742f6b7 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-80fd5eaf-f53f-4ec5-a2f1-7a41f742f6b7');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-a48d820a-3663-4935-bd72-d423e63c929e\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-a48d820a-3663-4935-bd72-d423e63c929e')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-a48d820a-3663-4935-bd72-d423e63c929e button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "##Data Visualization\n"
      ],
      "metadata": {
        "id": "Qa8jghE20tK2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "sns.set()"
      ],
      "metadata": {
        "id": "4vajD7fK0wTk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot(x='Sex', data=t_data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 475
        },
        "id": "LTrX2bje0173",
        "outputId": "37101332-fde0-4cd2-8f94-1c91851acd6b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='Sex', ylabel='count'>"
            ]
          },
          "metadata": {},
          "execution_count": 21
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t_data['Survived'].value_counts()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1rbX3rsN06sl",
        "outputId": "4a71b2fb-f55c-4ab4-ab53-1f05c93283a3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0    266\n",
              "1    152\n",
              "Name: Survived, dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 22
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot(x='Survived', data=t_data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 475
        },
        "id": "7Xu3Xj9w1C4Q",
        "outputId": "f83b89db-163f-423c-85df-1debaa5eae29"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='Survived', ylabel='count'>"
            ]
          },
          "metadata": {},
          "execution_count": 23
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot (x='Sex', hue = 'Survived', data = t_data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 475
        },
        "id": "FdwEwazM1FRf",
        "outputId": "8f82a0e2-4bc3-40da-95fa-4545351421f4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='Sex', ylabel='count'>"
            ]
          },
          "metadata": {},
          "execution_count": 24
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkUAAAG5CAYAAACAxkA+AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAzrklEQVR4nO3deXQV9f3/8WduIMh2wyKLsiVBiaBAYpU1REWEL5taLbbaQg8qolYWq35BDvKDfivQVguyqGX5utbd1mKNyCpRxFIrliJuSFCgIhRDEjZDcu/vD8r9mgYEEpJ7E5+Pczgyn/nMZ96T44TXnfncmbhwOBxGkiTpOy4Q7QIkSZJigaFIkiQJQ5EkSRJgKJIkSQIMRZIkSYChSJIkCTAUSZIkAYYiSZIkwFAkSZIEQI1oF1DVhMNhQiEfAi5JUlURCMQRFxd33H6GopMUCoX56qt90S5DkiSdoEaN6hIff/xQ5O0zSZIkDEWSJEmAoUiSJAkwFEmSJAFOtJYkKWpCoRDFxUXRLqNKi4+vQSBwaq7xGIokSapk4XCY/PyvOHBgb7RLqRZq165HMNjohL52/20MRZIkVbIjgahevYYkJNQq9z/m31XhcJjCwq/ZuzcXgMTExuUaz1AkSVIlCoWKI4GoXr1gtMup8hISagGwd28u9es3LNetNCdaS5JUiYqLi4H/+8dc5XfkZ1ne+VmGIkmSosBbZqfOqfpZGookSZIwFEmSJAGGIkmSdBz33juZH/xgcFT2nZFxAQsX/q5S9uW3zyRJijGffrqJRx6ZxwcfbCQ39yuCwUSSkpLJyMjkBz/4UbTLq7YMRTEmEIgjEHDynfSfQqEwoVA42mVIFe4f//g7o0ffTLNmzRk8+EoaNz6dnTu/5P33/8Hzzz8TlVA0btxEQqFQpe+3shmKYkggEEeDBnWIj/eupvSfiotD7Nmz32Ckau/xx/+XunXrMX/+49SvX7/Eutzcr07JPg4cOEDt2rVPuH+NGt+NuPDdOMoqIhCIIz4+wNynV7N9Z160y5FiRoumifzs2p4EAnGGIlV727dvIzk5pVQgAmjYsBEAX3zxT4YMuZwJE/4fAwaUnOuTkXEBw4eP4IYbRgKwcOHveOSR+TzxxHM89thC3n77Lc444wwuu6w/Dz74AC+88DLNm59RYoyHH57DM888yaJFSwgGg9x772TWrfsbL7zwMkVFRQwe3JdevS5iwoT/V2K7ffv2MnhwX6666hpuu20sAIWFhTzxxCMsWfIqO3d+ScOGjejTpy833ngLCQkJkW0LCwt5+OHZLFnyKl9/Xcj553+PO+4YX+6f58kwFMWg7Tvz2LI9N9plSJKioHnzM9iw4R9s3ryJlJSzTtm499wznlatWjFy5M8Ih8P06NGLhx6axYoVS7nuumEl+q5YsZQuXboRDJZ+4naNGjXIzLyYVatWctddE6hZs2ZkXXb26xQWFtKnT1/g8Atvx4//OevXv8fll3+fNm2S2bx5E88++xRbt37OtGn3R7b91a/+h9dee5XLLvsvzjuvE++++1fuumvsKTv+E2EokiQphlx77U+4884xDB/+Y9q3P5dOndK44IIunH/+BeW6jXXWWWczefK9JdrOPbcjy5eXDEUffPA+//zndq6//qZjjnXppX155ZVFrF37Nj179oq0r1ixlDPPbME553QAYOnSxbzzzlpmz55H585pkX7JyW25775p/OMff6djx8588snHvPbaq3z/+0O4445xAFx99TVMmTKRTz/9pMzHfLKcvCJJUgy58MJuPPzw/9KzZyabNn3MU089zs9/fhtXXtmfN99cVeZxr7zy6lJtvXtfxkcffcD27dsibcuXLyUhIYFevS465ljnn38BDRo0YMWKJZG2/Px8/vrXv3DppX0jbStXLqNNmyTatEliz549kT/f+96FALz77jsAvP32agCGDPlhif1cc821ZTjSsvNKkSRJMaZ9+3OZOvU3HDp0iE2bPiY7+3WeffYpJk4cxyOPPMVpp5120mOeccaZpdp69+7DnDkzWL58CcOGXU84HGblymV07dqDunXrHXOsGjVqcNFFvVm69DUKCwtJSEggO3sFRUVF9O59WaTftm1b2bIlh0GD+hx1nNzcw1NFduz4gkAgwJlntiyxvnXrNid9nOVhKJIkKUbVrFmT9u3PpX37c2nVqjVTp05h5cplpSZXH3HkZbNHU6tW6SB1+ulN6NQpjRUrljFs2PW8//4/+PLLHdxyy6jj1nbppX3505/+wNtvv0Vm5sWsWHH4qtDZZ7eL9AmFQrRtexa33Xb7Ucdo1qzZcfdTmQxFkiRVAeec0x6A3bv/Fflm2t69BSX67NjxxUmPe+mlfbn//ul8/vkWli9fymmnnUbPnpnH3S4t7Xwa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RnDJJZfQsGHDaJek7wBDkSQp5uTk5BAOh7nmmmto1apVtMvRd4S3z1QtjR8/nkGDBvHWW28xePBgOnXqxE9+8hO2bdvGnj17GDNmDOeffz59+vQhKysrst3rr7/O8OHD6d69O+effz5DhgwhOzv7uPsrLCzkt7/9LZdccgnnnXce/fv35+WXX67IQ5SqrfHjx3PzzTcD0KdPH1JTU/nDH/5Afn4+kydPJiMjg/POO4+rrrqKN998s8S2Q4cOZeTIkfz5z3+mb9++dO7cmZtvvpm8vDy2b9/ODTfcQHp6OgMHDuQvf/lLiW1feuklrr32Wrp06cKFF17I0KFDWb9+/XHrPZG6VDV4pUjV1q5du5g+fTq33HILNWrU4Je//CV33nkntWvX5oILLuCaa67hueee46677qJz5860aNGCbdu2cckll3D99dcTCATIzs7mpptu4rHHHqNr167H3NeYMWN49913+dnPfkbbtm1ZtWoVd911F8FgkIsuuqgSj1qq+m699Vbatm3Lfffdx5w5c2jSpAktW7Zk+PDh7N69m7Fjx9KsWTMWLVrEyJEjI/P8jti4cSO5ubn893//N3v37uWXv/wl99xzD9u3b+fKK69k+PDh/O53v2PUqFGsXLmSunXrArBt2zauvPJKWrduTWFhIa+88go//vGPWbRoEcnJyUettbCw8ITrUhUQlqqhcePGhVNTU8Mff/xxpO2JJ54It2vXLvyb3/wm0paXlxdu3759+NFHHy01RnFxcfjQoUPh66+/Pvzzn/880v7iiy+G27VrF969e3c4HA6H16xZE27Xrl34jTfeKLH92LFjw1dfffWpPjTpO2Hp0qXhdu3ahbdu3RoOh8PhF154IdyhQ4fwJ598UqLfkCFDwqNHj44s/+QnPwmnpaVFzs9wOByePn16uF27duGnnnoq0vbRRx+F27VrF166dOlR93/k/O/Xr1/4/vvvj7TPmjUrnJaWFlk+0bpUNXilSNVW06ZNOfvssyPLSUlJAPTo0SPSFgwGadSoETt27ABgx44dzJgxg7feeotdu3YR/vf7ks8999xj7mf16tU0aNCAbt26UVRUFGnv0aMHkydPpri4mPj4+FN5aNJ3zurVq2nXrh1JSUmlzrNFixaV6HvOOefQqFGjyPLRzv0jbUfOfYBPP/2U3/72t6xbt47du3dH2rds2XJK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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##this is clearly visible that those who survived were only females"
      ],
      "metadata": {
        "id": "D6hbkVwJ1Qcy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "t_data[['Survived', 'Sex']]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "K20UzbWg1NC5",
        "outputId": "5a5b8259-a9fa-4c6b-92d1-ada8e17ab065"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     Survived     Sex\n",
              "0           0    male\n",
              "1           1  female\n",
              "2           0    male\n",
              "3           0    male\n",
              "4           1  female\n",
              "..        ...     ...\n",
              "413         0    male\n",
              "414         1  female\n",
              "415         0    male\n",
              "416         0    male\n",
              "417         0    male\n",
              "\n",
              "[418 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-e1879879-bc46-45ec-afa8-9aa93668c4a8\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Survived</th>\n",
              "      <th>Sex</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>female</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0</td>\n",
              "      <td>male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0</td>\n",
              "      <td>male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>female</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>413</th>\n",
              "      <td>0</td>\n",
              "      <td>male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>414</th>\n",
              "      <td>1</td>\n",
              "      <td>female</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>415</th>\n",
              "      <td>0</td>\n",
              "      <td>male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>416</th>\n",
              "      <td>0</td>\n",
              "      <td>male</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>417</th>\n",
              "      <td>0</td>\n",
              "      <td>male</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>418 rows × 2 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-e1879879-bc46-45ec-afa8-9aa93668c4a8')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-e1879879-bc46-45ec-afa8-9aa93668c4a8 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-e1879879-bc46-45ec-afa8-9aa93668c4a8');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-71ac0360-7157-456d-971d-082b041a8bc5\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-71ac0360-7157-456d-971d-082b041a8bc5')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-71ac0360-7157-456d-971d-082b041a8bc5 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 25
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "t_data[['Survived', 'Pclass' ]]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "ADkRPcg-1Xue",
        "outputId": "a9e5f13d-7d76-4ef4-afb5-0e9d6e387ea6"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     Survived  Pclass\n",
              "0           0       3\n",
              "1           1       3\n",
              "2           0       2\n",
              "3           0       3\n",
              "4           1       3\n",
              "..        ...     ...\n",
              "413         0       3\n",
              "414         1       1\n",
              "415         0       3\n",
              "416         0       3\n",
              "417         0       3\n",
              "\n",
              "[418 rows x 2 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-7ff28d9e-8584-43d0-904b-5e711db9611e\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>413</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>414</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>415</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>416</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>417</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>418 rows × 2 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-7ff28d9e-8584-43d0-904b-5e711db9611e')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-7ff28d9e-8584-43d0-904b-5e711db9611e button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-7ff28d9e-8584-43d0-904b-5e711db9611e');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-cf21423a-df55-4286-9327-22ac2daa0a42\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-cf21423a-df55-4286-9327-22ac2daa0a42')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-cf21423a-df55-4286-9327-22ac2daa0a42 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.countplot(x ='Pclass',hue= 'Survived', data=t_data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 475
        },
        "id": "Ex2NQB3j1cw_",
        "outputId": "a74d6776-d2e1-4f1a-d8d1-edebd3d4bf13"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: xlabel='Pclass', ylabel='count'>"
            ]
          },
          "metadata": {},
          "execution_count": 27
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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PP7449x5550UFBTw05/+lEgkkuiy6jyPFEk65oXDYUaOHElmZiZTp051/psSrn379gB07dqVTp06cfHFF7Nw4ULOP//8BFdWtxmKJB3T9u7dyzXXXENRURHz5s3zXjCqddq1a0f9+vXZvHlzokup8wxFko5ZZWVljB49moKCAubOnevlzqqV1qxZw759+5xoHQeGIsVNSUkJy5YtA2Dbtm0UFxezYMECALp3737Qy6OlmnT77bezdOlSxo0bR3FxMW+99VZ532mnnUZqamriitMxadSoUZx++um0a9eOhg0b8sEHHzBr1izatWvHwIEDE11enefNGxU3W7duZcCAAQftmzNnDj169IhzRTrW9e/fn23bth20b/Hixf6XueJu5syZ5Ofns3nzZmKxGC1btuTcc8/l6quv9jYRcWAokiRJwkvyJUmSAEORJEkSYCiSJEkCDEWSJEmAoUiSJAkwFEmSJAGGIkmSJMBQJOkYtHXrVtq1a8ef//znRJciqRbxMR+Sksaf//xnbrnllvLXqampnHTSSfTu3Ztrr72W4447LoHVSUp2hiJJSeeGG26gVatWlJaW8sYbb/DYY4+xbNkynnvuOdLS0hJdnqQkZSiSlHT69etHp06dABg+fDiZmZnMnj2bxYsXc8EFFyS4OknJylAkKen17NmT2bNns3XrVgDC4TDTpk1j0aJF7Nixg6ZNm9KzZ0/GjRtH06ZND7qODz74gD/+8Y+8/vrr7Nixg1AoRL9+/fjlL39JVlZW+bji4mKmTJnC4sWL2bFjB02aNKF9+/aMHTuWjh07ArBp0ybuuece3nzzTcLhMFlZWXzjG9/gjjvuoEmTJjX/gUiqEkORpKS3efNmADIzM9m9ezff/e532bBhA8OGDeO0005j586dLFmyhO3btx8yFL3yyits2bKFyy67jOOPP55169Yxf/581q9fz/z58wkEAgD86le/4oUXXuB73/seubm57Nq1izfeeIMNGzbQsWNHSktLufrqqyktLeV73/sexx13HNu3b+fvf/874XDYUCTVYoYiSUmnuLiYzz//nNLSUt58802mT59Ow4YNOeecc5g1axYffvgh06ZN49xzzy1f5tprryUWix1ynVdeeSVXXXVVhbYuXbpw00038cYbb9CtWzcAli1bxre//W3GjRtXPm7kyJHl/96wYQNbt25lypQpnH/++eXto0aNOur3LalmGYokJZ0f/vCHFV63bNmSu+++mxYtWvDiiy/Svn37CoHogANHew6mYcOG5f/+4osv2L17N2eccQYA7777bnkoCoVCrFmzhu3bt9OiRYtK62ncuDEAL7/8MmeddZYTv6UkYiiSlHRuu+02srOzSUlJ4bjjjiM7O5tgcP9t1zZv3sx55513xOvctWsX06ZNIz8/n88++6xCX1FRUfm/x44dy7hx4zj77LPp2LEjZ511FpdccgmtW7cGoHXr1vzoRz9i9uzZ/PWvf6Vbt27079+fiy66yFNnUi1nKJKUdDp37lx+9Vl1GT16NKtXr+bqq6+mQ4cONGrUiGg0yo9//OMKp92GDBlCt27dWLhwIStWrGDWrFnk5eUxdepUzjrrLADGjRvHpZdeyuLFi1mxYgV33nkn//M//8P8+fM54YQTqrVuSdXHO1pLqlPatGnDunXrjmiZwsJCVq5cyciRI7nhhhs499xz6d27d/nRn3/XvHlzvvvd7zJjxgwWL15MZmYmDz74YIUx7dq149prr2Xu3LnMnTuX7du389hjj1X5fUmqeYYiSXXKeeedxwcffMDChQsr9R1qonVKSspB2//0pz9VeB2JRCqcSgNo1qwZzZs3p7S0FNg/CbysrKzCmFNPPZVgMFg+RlLt5OkzSXXK1VdfzQsvvMCNN97IsGHD6NixI4WFhSxZsoTbb7+d9u3bV1qmcePGfPOb3+Shhx5i3759tGjRghUrVpTf9+iA3bt3c9ZZZzFo0CDat29Po0aNeOWVV3jnnXfKr0Z79dVXueOOOzj//PNp27YtkUiEZ555hpSUFAYNGhSXz0BS1RiKJNUp6enpzJ07l6lTp7Jw4UKefvppmjVrRq9evQ56tdgB99xzD7/+9a959NFHicVi9O7dm7y8PPr27Vs+pmHDhlxxxRWsWLGCF198kVgsRps2bfjVr37FlVdeCew/bdanTx+WLl3K9u3bSUtLo127duTl5dGlS5eafvuSjkIg9p9u3CFJknSMcE6RJEkShiJJkiTAUCRJkgQYiiRJkgBDkSRJEmAokiRJAgxFkiRJgKFIkiQJMBRJkiQBhiJJkiTAUCRJkgQYiiRJkgBDkSRJEgD/D0isc0EfnTqYAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##converting the categorical variables into numerical data"
      ],
      "metadata": {
        "id": "ZnMKr3AC1oEi"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.replace({'Sex':{'male':0, 'female':1},'Embarked':{'S':0, 'C':1, 'Q':2}}, inplace=True)"
      ],
      "metadata": {
        "id": "xOhyw9xL1j8W"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "NK2o6qrT1yD4",
        "outputId": "35fa8898-ee88-4a50-81c2-b99828c4176b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     PassengerId  Survived  Pclass  \\\n",
              "0            892         0       3   \n",
              "1            893         1       3   \n",
              "2            894         0       2   \n",
              "3            895         0       3   \n",
              "4            896         1       3   \n",
              "..           ...       ...     ...   \n",
              "413         1305         0       3   \n",
              "414         1306         1       1   \n",
              "415         1307         0       3   \n",
              "416         1308         0       3   \n",
              "417         1309         0       3   \n",
              "\n",
              "                                             Name  Sex       Age  SibSp  \\\n",
              "0                                Kelly, Mr. James    0  34.50000      0   \n",
              "1                Wilkes, Mrs. James (Ellen Needs)    1  47.00000      1   \n",
              "2                       Myles, Mr. Thomas Francis    0  62.00000      0   \n",
              "3                                Wirz, Mr. Albert    0  27.00000      0   \n",
              "4    Hirvonen, Mrs. Alexander (Helga E Lindqvist)    1  22.00000      1   \n",
              "..                                            ...  ...       ...    ...   \n",
              "413                            Spector, Mr. Woolf    0  30.27259      0   \n",
              "414                  Oliva y Ocana, Dona. Fermina    1  39.00000      0   \n",
              "415                  Saether, Mr. Simon Sivertsen    0  38.50000      0   \n",
              "416                           Ware, Mr. Frederick    0  30.27259      0   \n",
              "417                      Peter, Master. Michael J    0  30.27259      1   \n",
              "\n",
              "     Parch              Ticket      Fare  Embarked  \n",
              "0        0              330911    7.8292         2  \n",
              "1        0              363272    7.0000         0  \n",
              "2        0              240276    9.6875         2  \n",
              "3        0              315154    8.6625         0  \n",
              "4        1             3101298   12.2875         0  \n",
              "..     ...                 ...       ...       ...  \n",
              "413      0           A.5. 3236    8.0500         0  \n",
              "414      0            PC 17758  108.9000         1  \n",
              "415      0  SOTON/O.Q. 3101262    7.2500         0  \n",
              "416      0              359309    8.0500         0  \n",
              "417      1                2668   22.3583         1  \n",
              "\n",
              "[418 rows x 11 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-cd56781e-2ef1-41c3-80f4-38c16c62a1a5\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>PassengerId</th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Name</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>SibSp</th>\n",
              "      <th>Parch</th>\n",
              "      <th>Ticket</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Embarked</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>892</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Kelly, Mr. James</td>\n",
              "      <td>0</td>\n",
              "      <td>34.50000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>330911</td>\n",
              "      <td>7.8292</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>893</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Wilkes, Mrs. James (Ellen Needs)</td>\n",
              "      <td>1</td>\n",
              "      <td>47.00000</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>363272</td>\n",
              "      <td>7.0000</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>894</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>Myles, Mr. Thomas Francis</td>\n",
              "      <td>0</td>\n",
              "      <td>62.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>240276</td>\n",
              "      <td>9.6875</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>895</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Wirz, Mr. Albert</td>\n",
              "      <td>0</td>\n",
              "      <td>27.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>315154</td>\n",
              "      <td>8.6625</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>896</td>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>Hirvonen, Mrs. Alexander (Helga E Lindqvist)</td>\n",
              "      <td>1</td>\n",
              "      <td>22.00000</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>3101298</td>\n",
              "      <td>12.2875</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>413</th>\n",
              "      <td>1305</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Spector, Mr. Woolf</td>\n",
              "      <td>0</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>A.5. 3236</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>414</th>\n",
              "      <td>1306</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>Oliva y Ocana, Dona. Fermina</td>\n",
              "      <td>1</td>\n",
              "      <td>39.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>PC 17758</td>\n",
              "      <td>108.9000</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>415</th>\n",
              "      <td>1307</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Saether, Mr. Simon Sivertsen</td>\n",
              "      <td>0</td>\n",
              "      <td>38.50000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>SOTON/O.Q. 3101262</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>416</th>\n",
              "      <td>1308</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Ware, Mr. Frederick</td>\n",
              "      <td>0</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>359309</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>417</th>\n",
              "      <td>1309</td>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>Peter, Master. Michael J</td>\n",
              "      <td>0</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>2668</td>\n",
              "      <td>22.3583</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>418 rows × 11 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-cd56781e-2ef1-41c3-80f4-38c16c62a1a5')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-cd56781e-2ef1-41c3-80f4-38c16c62a1a5 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-cd56781e-2ef1-41c3-80f4-38c16c62a1a5');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-399b2020-014c-4962-bcd6-0f251f4cc708\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-399b2020-014c-4962-bcd6-0f251f4cc708')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-399b2020-014c-4962-bcd6-0f251f4cc708 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Now drop the columns which are irrelevant for the survival prediction, such as PassengerId, Name and Ticket"
      ],
      "metadata": {
        "id": "jwnWxL_e117-"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data.drop(columns={'PassengerId','Name','Ticket'},axis=1, inplace=True)"
      ],
      "metadata": {
        "id": "u4uDO3MW15DN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "t_data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 423
        },
        "id": "grSatKvE2EQV",
        "outputId": "fc6a47a7-ae0c-48bb-884a-c71008eefaa8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "     Survived  Pclass  Sex       Age  SibSp  Parch      Fare  Embarked\n",
              "0           0       3    0  34.50000      0      0    7.8292         2\n",
              "1           1       3    1  47.00000      1      0    7.0000         0\n",
              "2           0       2    0  62.00000      0      0    9.6875         2\n",
              "3           0       3    0  27.00000      0      0    8.6625         0\n",
              "4           1       3    1  22.00000      1      1   12.2875         0\n",
              "..        ...     ...  ...       ...    ...    ...       ...       ...\n",
              "413         0       3    0  30.27259      0      0    8.0500         0\n",
              "414         1       1    1  39.00000      0      0  108.9000         1\n",
              "415         0       3    0  38.50000      0      0    7.2500         0\n",
              "416         0       3    0  30.27259      0      0    8.0500         0\n",
              "417         0       3    0  30.27259      1      1   22.3583         1\n",
              "\n",
              "[418 rows x 8 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-c7bc21ea-d8f0-4497-b5cf-45b8af459b87\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Survived</th>\n",
              "      <th>Pclass</th>\n",
              "      <th>Sex</th>\n",
              "      <th>Age</th>\n",
              "      <th>SibSp</th>\n",
              "      <th>Parch</th>\n",
              "      <th>Fare</th>\n",
              "      <th>Embarked</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>34.50000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>7.8292</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>47.00000</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>7.0000</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>62.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>9.6875</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>27.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>8.6625</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>1</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>22.00000</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>12.2875</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>413</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>414</th>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>39.00000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>108.9000</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>415</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>38.50000</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>7.2500</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>416</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>8.0500</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>417</th>\n",
              "      <td>0</td>\n",
              "      <td>3</td>\n",
              "      <td>0</td>\n",
              "      <td>30.27259</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>22.3583</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>418 rows × 8 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-c7bc21ea-d8f0-4497-b5cf-45b8af459b87')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-c7bc21ea-d8f0-4497-b5cf-45b8af459b87 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-c7bc21ea-d8f0-4497-b5cf-45b8af459b87');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-f1a559ee-5707-4f01-854f-86df241d74eb\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-f1a559ee-5707-4f01-854f-86df241d74eb')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-f1a559ee-5707-4f01-854f-86df241d74eb button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##separating features and target"
      ],
      "metadata": {
        "id": "BFimKHpR2V5F"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X = t_data.drop(columns='Survived', axis=1)\n",
        "Y = t_data['Survived']"
      ],
      "metadata": {
        "id": "M2m1lqr72STe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X)\n",
        "print(Y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8MidbJGI2bpd",
        "outputId": "d32370ff-9f2a-4b26-802d-14dbaa709a80"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     Pclass  Sex       Age  SibSp  Parch      Fare  Embarked\n",
            "0         3    0  34.50000      0      0    7.8292         2\n",
            "1         3    1  47.00000      1      0    7.0000         0\n",
            "2         2    0  62.00000      0      0    9.6875         2\n",
            "3         3    0  27.00000      0      0    8.6625         0\n",
            "4         3    1  22.00000      1      1   12.2875         0\n",
            "..      ...  ...       ...    ...    ...       ...       ...\n",
            "413       3    0  30.27259      0      0    8.0500         0\n",
            "414       1    1  39.00000      0      0  108.9000         1\n",
            "415       3    0  38.50000      0      0    7.2500         0\n",
            "416       3    0  30.27259      0      0    8.0500         0\n",
            "417       3    0  30.27259      1      1   22.3583         1\n",
            "\n",
            "[418 rows x 7 columns]\n",
            "0      0\n",
            "1      1\n",
            "2      0\n",
            "3      0\n",
            "4      1\n",
            "      ..\n",
            "413    0\n",
            "414    1\n",
            "415    0\n",
            "416    0\n",
            "417    0\n",
            "Name: Survived, Length: 418, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##splitting the data into training and testing"
      ],
      "metadata": {
        "id": "u0Ewv5Wx2l43"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)\n"
      ],
      "metadata": {
        "id": "T46cWrcC2hb5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wFTP5mWr4ZVG",
        "outputId": "c43bf942-e0e3-4e66-fd5f-c69a62a248b7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Pclass      0\n",
              "Sex         0\n",
              "Age         0\n",
              "SibSp       0\n",
              "Parch       0\n",
              "Fare        0\n",
              "Embarked    0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Model Training"
      ],
      "metadata": {
        "id": "8jjdCDEQ4_Sr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# we're using logistic regression model that uses binary classification for the prediction"
      ],
      "metadata": {
        "id": "XAKyIgLM4ebz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = LogisticRegression()"
      ],
      "metadata": {
        "id": "56hKV89R5EAU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#training the model with the training data"
      ],
      "metadata": {
        "id": "mxi3Evgz5KaM"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model.fit(X_train,Y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 213
        },
        "id": "RGxdL-Xv5NuC",
        "outputId": "779ec390-fc5e-431a-c032-563979ad9ffb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/linear_model/_logistic.py:458: ConvergenceWarning: lbfgs failed to converge (status=1):\n",
            "STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.\n",
            "\n",
            "Increase the number of iterations (max_iter) or scale the data as shown in:\n",
            "    https://scikit-learn.org/stable/modules/preprocessing.html\n",
            "Please also refer to the documentation for alternative solver options:\n",
            "    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression\n",
            "  n_iter_i = _check_optimize_result(\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "LogisticRegression()"
            ],
            "text/html": [
              "<style>#sk-container-id-1 {color: black;background-color: white;}#sk-container-id-1 pre{padding: 0;}#sk-container-id-1 div.sk-toggleable {background-color: white;}#sk-container-id-1 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-1 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-1 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-1 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-1 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-1 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-1 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-1 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-1 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-1 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-1 div.sk-item {position: relative;z-index: 1;}#sk-container-id-1 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-1 div.sk-item::before, #sk-container-id-1 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-1 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-1 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-1 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-1 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-1 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-1 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-1 div.sk-label-container {text-align: center;}#sk-container-id-1 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-1 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-1\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-1\" type=\"checkbox\" checked><label for=\"sk-estimator-id-1\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 40
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Model Evaluation\n",
        "##Accuracy Score || Precision Score || Recall Score"
      ],
      "metadata": {
        "id": "ksi8S6nC5VVc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "X_test_prediction = model.predict(X_test)"
      ],
      "metadata": {
        "id": "R_rUNNPq5Rit"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# accuracy score for training data"
      ],
      "metadata": {
        "id": "QdwXeqCc5fww"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# accuracy score for test data"
      ],
      "metadata": {
        "id": "gggYuJoA5jEp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(X_test_prediction)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "THTLcDxx5lqX",
        "outputId": "c1bdd548-73d1-49ec-d4ba-a6f4879b2297"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0 0 0 1 0 1 1 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 1 0 0 0 0 1 0 0 1 1\n",
            " 1 0 1 1 0 0 0 0 1 0 1 0 0 1 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0 0 0 1\n",
            " 0 1 0 1 1 0 0 0 1 0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)"
      ],
      "metadata": {
        "id": "XN3Ye5CI5prS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('Accuracy score of test data is : ',testing_data_accuracy)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7e-GsEMY5tNn",
        "outputId": "5ec25d3d-4144-4e8b-b5ed-ecf86cd25444"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy score of test data is :  1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# precision score"
      ],
      "metadata": {
        "id": "-MIV0jn15wKE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "test_data_precision = precision_score(Y_test, X_test_prediction)"
      ],
      "metadata": {
        "id": "RzH_fe9P5zV7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('test data precion is :', test_data_precision)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "76lNKyo553rD",
        "outputId": "a371d227-6b82-43c7-bd4e-fa9a9077d65c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "test data precion is : 1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# recall score"
      ],
      "metadata": {
        "id": "lBtlEo6u583w"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import recall_score"
      ],
      "metadata": {
        "id": "rDT1UFHg6Anj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train_prediction = model.predict(X_train)\n",
        "\n",
        "# Now you can calculate the recall\n",
        "test_data_recall = recall_score(Y_train, X_train_prediction)"
      ],
      "metadata": {
        "id": "6zbq-i0kIc_R"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print('test data recall is :', test_data_recall)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Dzk0RdyHIhyc",
        "outputId": "eb1fe49b-425f-4468-ed51-52624784491a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "test data recall is : 1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn import metrics"
      ],
      "metadata": {
        "id": "kv2yybsvInkh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "score = model.score(X_test,Y_test)\n",
        "print(score)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Y9NvJ_HuIrmd",
        "outputId": "19bdf3ac-5b91-42e3-bbea-65f42bc7923c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cm = metrics.confusion_matrix(Y_train, X_train_prediction)\n",
        "print(cm)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "x-blGHMJIvQ9",
        "outputId": "ebc9476e-2708-4b08-99e5-f8794616b248"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[208   0]\n",
            " [  0 126]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.heatmap(cm, annot = True, fmt = \"d\", square = True, cmap= \"inferno\")\n",
        "plt.ylabel('Actual label')\n",
        "plt.xlabel('predicted label')\n",
        "title = ('Accuracy Score :',score)\n",
        "plt.title(title, size = 10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 494
        },
        "id": "0phXLk_PIyr-",
        "outputId": "8055dcae-aeba-45ab-bc69-91a47063e709"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0.5, 1.0, \"('Accuracy Score :', 1.0)\")"
            ]
          },
          "metadata": {},
          "execution_count": 57
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.metrics import classification_report"
      ],
      "metadata": {
        "id": "qzTam1uEI4Pe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_test_pred = model.predict(X_test)\n",
        "\n",
        "# Now you can generate the classification report\n",
        "report = classification_report(X_test_pred, Y_test)\n",
        "print(report)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p7XytL-HJWP9",
        "outputId": "dc1176e1-29de-4662-82cf-03bebfdacc39"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       1.00      1.00      1.00        58\n",
            "           1       1.00      1.00      1.00        26\n",
            "\n",
            "    accuracy                           1.00        84\n",
            "   macro avg       1.00      1.00      1.00        84\n",
            "weighted avg       1.00      1.00      1.00        84\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Model 2\n",
        "##Random Forest Classification"
      ],
      "metadata": {
        "id": "k1lfwLBHJd4i"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.ensemble import RandomForestClassifier"
      ],
      "metadata": {
        "id": "I4E2x2zsJZwD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_2 = RandomForestClassifier(n_estimators=100)"
      ],
      "metadata": {
        "id": "HgNuHrYsJoOQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_2.fit(X_train,Y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "WhJGSgabJrhE",
        "outputId": "22ad1da9-662d-455f-a949-c97f2d5ef771"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestClassifier()"
            ],
            "text/html": [
              "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier()</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 63
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_test_pred = model_2.predict(X_test)"
      ],
      "metadata": {
        "id": "qWoDXoNhJvl3"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_2.score(X_train, Y_train)\n",
        "acc_score = round(model_2.score(X_test, Y_test) * 100, 2)\n",
        "model_2_acc = accuracy_score(X_test_pred, Y_test)"
      ],
      "metadata": {
        "id": "ZHF6-srTJ3hf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_2_acc"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sQS9jgYdJ54C",
        "outputId": "98f3229b-0f97-4c90-c494-995178a8d981"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "1.0"
            ]
          },
          "metadata": {},
          "execution_count": 67
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "acc_score"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O1Zy1xphJ9JA",
        "outputId": "f208f56f-f454-4cc1-b161-0a27e9fd4a03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "100.0"
            ]
          },
          "metadata": {},
          "execution_count": 68
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "precision = precision_score(X_test_pred, Y_test)\n",
        "recall = recall_score(X_test_pred, Y_test)"
      ],
      "metadata": {
        "id": "ydgQnQyQKDp_"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(precision)\n",
        "print(recall)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w24RvdamKHY-",
        "outputId": "cdf1ca93-7bda-4245-8470-7b4eb50f4d6d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1.0\n",
            "1.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "classification_report(X_test_pred, Y_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 70
        },
        "id": "JnC3c34BKJIX",
        "outputId": "387c66b9-f060-4b14-a95d-bfa9d1c0392b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'              precision    recall  f1-score   support\\n\\n           0       1.00      1.00      1.00        58\\n           1       1.00      1.00      1.00        26\\n\\n    accuracy                           1.00        84\\n   macro avg       1.00      1.00      1.00        84\\nweighted avg       1.00      1.00      1.00        84\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 71
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Model 3\n",
        "##KNN"
      ],
      "metadata": {
        "id": "CC6jP2gQKNLu"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.neighbors import KNeighborsClassifier"
      ],
      "metadata": {
        "id": "xe0nb1ptKUrE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_3 = KNeighborsClassifier(n_neighbors=3)"
      ],
      "metadata": {
        "id": "-tiir3Z-Ki0d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_3.fit(X_train, Y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "mJ0D-fceKmMZ",
        "outputId": "7a3561c9-38b8-45e2-954d-07cbe1f7c49f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "KNeighborsClassifier(n_neighbors=3)"
            ],
            "text/html": [
              "<style>#sk-container-id-3 {color: black;background-color: white;}#sk-container-id-3 pre{padding: 0;}#sk-container-id-3 div.sk-toggleable {background-color: white;}#sk-container-id-3 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-3 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-3 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-3 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-3 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-3 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-3 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-3 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-3 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-3 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-3 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-3 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-3 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-3 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-3 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-3 div.sk-item {position: relative;z-index: 1;}#sk-container-id-3 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-3 div.sk-item::before, #sk-container-id-3 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-3 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-3 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-3 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-3 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-3 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-3 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-3 div.sk-label-container {text-align: center;}#sk-container-id-3 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-3 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-3\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>KNeighborsClassifier(n_neighbors=3)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-3\" type=\"checkbox\" checked><label for=\"sk-estimator-id-3\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">KNeighborsClassifier</label><div class=\"sk-toggleable__content\"><pre>KNeighborsClassifier(n_neighbors=3)</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 74
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X_test_pred = model_3.predict(X_test)"
      ],
      "metadata": {
        "id": "toM2NA6sKpy4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_3_acc = accuracy_score(X_test_pred, Y_test, normalize=True)"
      ],
      "metadata": {
        "id": "PxW4JW4oKvEC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_3_score = round(model_3.score(X_train, Y_train) * 100, 2)"
      ],
      "metadata": {
        "id": "NgoWBSFYKwxW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_3_precision = precision_score(X_test_pred, Y_test)\n",
        "model_3_recall = recall_score(X_test_pred, Y_test)"
      ],
      "metadata": {
        "id": "0-kLWRJXK2ik"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model_3_score"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mLZ0FkYwK5oX",
        "outputId": "99df0ec2-b270-4169-db31-ee4d90824cec"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "85.03"
            ]
          },
          "metadata": {},
          "execution_count": 79
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "model_3_acc"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Gpiaw1YkK7sK",
        "outputId": "d285a850-735b-4b77-abb4-31521c6f7633"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.7023809523809523"
            ]
          },
          "metadata": {},
          "execution_count": 80
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(model_3_precision)\n",
        "print(model_3_recall)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VR-cdWdyK_ao",
        "outputId": "80139e18-241e-487e-f8c7-eae9b00ad201"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0.5769230769230769\n",
            "0.5172413793103449\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "classification_report(X_test_pred, Y_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 70
        },
        "id": "V1BOoDSyLD7I",
        "outputId": "2740e10b-8805-4ee6-edc9-1f3dba6666cd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'              precision    recall  f1-score   support\\n\\n           0       0.76      0.80      0.78        55\\n           1       0.58      0.52      0.55        29\\n\\n    accuracy                           0.70        84\\n   macro avg       0.67      0.66      0.66        84\\nweighted avg       0.70      0.70      0.70        84\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 82
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Predicting values"
      ],
      "metadata": {
        "id": "Sq0_HRExLHyV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(X)\n",
        "print(Y)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KEwNb9g9LMXz",
        "outputId": "b9fe3571-89ed-4d9c-e391-37a63d26ac0a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "     Pclass  Sex       Age  SibSp  Parch      Fare  Embarked\n",
            "0         3    0  34.50000      0      0    7.8292         2\n",
            "1         3    1  47.00000      1      0    7.0000         0\n",
            "2         2    0  62.00000      0      0    9.6875         2\n",
            "3         3    0  27.00000      0      0    8.6625         0\n",
            "4         3    1  22.00000      1      1   12.2875         0\n",
            "..      ...  ...       ...    ...    ...       ...       ...\n",
            "413       3    0  30.27259      0      0    8.0500         0\n",
            "414       1    1  39.00000      0      0  108.9000         1\n",
            "415       3    0  38.50000      0      0    7.2500         0\n",
            "416       3    0  30.27259      0      0    8.0500         0\n",
            "417       3    0  30.27259      1      1   22.3583         1\n",
            "\n",
            "[418 rows x 7 columns]\n",
            "0      0\n",
            "1      1\n",
            "2      0\n",
            "3      0\n",
            "4      1\n",
            "      ..\n",
            "413    0\n",
            "414    1\n",
            "415    0\n",
            "416    0\n",
            "417    0\n",
            "Name: Survived, Length: 418, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "p1 = model.predict([[3, 0, 34.5, 0, 0, 7.8292, 2]])\n",
        "p2 = model_2.predict([[3, 0, 34.5, 0, 0, 7.8292, 2]])\n",
        "p3 = model_3.predict([[3, 0, 34.5, 0, 0, 7.8292, 2]])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RdukzocYLQPS",
        "outputId": "ceedf336-3d47-433e-dada-54b00fc92e12"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names\n",
            "  warnings.warn(\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
            "  warnings.warn(\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but KNeighborsClassifier was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(p1)\n",
        "print(p2)\n",
        "print(p3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r0wvheTULU1q",
        "outputId": "a1a77a16-d125-4bf1-e231-450b5867ae4c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0]\n",
            "[0]\n",
            "[0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "p1 = model.predict([[2, 0, 38.5, 0, 0, 7.2500, 0]])\n",
        "p2 = model_2.predict([[2, 0, 38.5, 0, 0, 7.2500, 0]])\n",
        "p3 = model_3.predict([[2, 0, 38.5, 0, 0, 7.2500, 0]])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7hUX-s0HLZbK",
        "outputId": "41ab4447-52a2-4069-946e-0531cadb9e6f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but LogisticRegression was fitted with feature names\n",
            "  warnings.warn(\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but RandomForestClassifier was fitted with feature names\n",
            "  warnings.warn(\n",
            "/usr/local/lib/python3.10/dist-packages/sklearn/base.py:439: UserWarning: X does not have valid feature names, but KNeighborsClassifier was fitted with feature names\n",
            "  warnings.warn(\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(p1)\n",
        "print(p2)\n",
        "print(p3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NQWaOhbmLgTB",
        "outputId": "8b650257-166c-4bed-dd1d-a20f7da47e97"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0]\n",
            "[0]\n",
            "[0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Our prediction model is ready , and we have also predicted certain values"
      ],
      "metadata": {
        "id": "ft57xkP3Lj_q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Our prediction model is ready , and we have also predicted certain values\n",
        "#We used three different models to predict our target vaiable and saw that they provided different accuracy and precision."
      ],
      "metadata": {
        "id": "3XrzpHeILnxX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Thank you\n"
      ],
      "metadata": {
        "id": "Z7yZKG7eLsrZ"
      }
    }
  ]
}