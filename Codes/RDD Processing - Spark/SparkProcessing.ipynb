{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Importing required packages"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import re\n",
    "import pandas as pd \n",
    "from urlparse import urlsplit"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Reading all files"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "main_file=sc.textFile(\"hdfs://localhost:8020/pkdd2005/logs/FlumeData*\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'14;1074585600;147.33.10.112;89ccfad2c4bbc02c91ed66055a235fca;/ls/index.php?&id=62&view=1,2,3,4,6,9&sort=,13,4&pozice=40;http://www.shop4.cz/ls/index.php?&id=62&view=1,2,3,4,6,9&sort=,13,4&pozice=20'"
      ]
     },
     "execution_count": 117,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "main_file.first() ## printing the test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3617171"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "main_file.count()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##Creating transformation functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 119,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "def transformsnumer(inputStr):\n",
    "    attList=inputStr.split(\";\")\n",
    "    \n",
    "    x =attList[4]\n",
    "    y =attList[5]\n",
    "    \n",
    "    if len(x)>2:\n",
    "        Visited1 = visited_Transform(x)\n",
    "        ID1=ID_transform(x)\n",
    "    else:\n",
    "        Visited1 =''\n",
    "        ID1=''\n",
    "    if len(y)>2:\n",
    "        Visited2= visited_Transform(y)\n",
    "        ID2=ID_transform(y)\n",
    "        \n",
    "    else:\n",
    "        Visited2=''\n",
    "        ID2=''\n",
    "        \n",
    "    values= ([Visited1,ID1,Visited2,ID2])\n",
    "    \n",
    "    return values   "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def find_nth_character(str1, substr, n):\n",
    "    pos = -1\n",
    "    for x in xrange(n):\n",
    "        pos = str1.find(substr, pos+1)\n",
    "        if pos == -1:\n",
    "            return None\n",
    "    return pos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def visited_Transform(intstr):\n",
    "    parsed = urlsplit(intstr)\n",
    "    try:\n",
    "        if len(parsed.path)==0 or parsed.path =='/' or parsed.path[0:5]=='w-ans':\n",
    "            values=''\n",
    "        \n",
    "        else:\n",
    "        \n",
    "            if parsed.path[3]=='/':\n",
    "                values=parsed.path[0:4]\n",
    "            else:\n",
    "            \n",
    "                c = '/'\n",
    "                x = parsed.path\n",
    "                a=find_nth_character(x,c,2)\n",
    "                if a > 0:\n",
    "                    values=parsed.path[0:a+1]\n",
    "                else:\n",
    "                    values=parsed.path\n",
    "    except:\n",
    "        values=''\n",
    "    return values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def ID_transform(intstr):\n",
    "    parsed = urlsplit(intstr)\n",
    "    x= parsed.query\n",
    "    y=parsed.path\n",
    "    try:\n",
    "        if len(x) == 0:\n",
    "            values=''\n",
    "        else:\n",
    "            if y[0:4]=='/dt/':\n",
    "                c= '=' \n",
    "                a=find_nth_character(x,c,1)\n",
    "                values=x[a+1:]\n",
    "            elif y[0:4]=='/ls/':\n",
    "                if parsed.query[0]=='&':\n",
    "                    c='&'\n",
    "                    d='id='\n",
    "                    a=find_nth_character(x,d,1)\n",
    "                    b=find_nth_character(x,c,2)\n",
    "                    values=parsed.query[a+3:b]\n",
    "#                 except:\n",
    "#                     values=''\n",
    "\n",
    "                else:\n",
    "                    if len(parsed.query)<=6:\n",
    "                        #c=len()\n",
    "                        d='id='\n",
    "                        a=find_nth_character(x,d,1)\n",
    "                        #b=find_nth_character(x,c,2)\n",
    "                        values=parsed.query[a+3:]\n",
    "                    else:\n",
    "                        c='&'\n",
    "                        d='id='\n",
    "                        a=find_nth_character(x,d,1)\n",
    "                        b=find_nth_character(x,c,2)\n",
    "                        values=parsed.query[a+3:b]\n",
    "            else:\n",
    "                parsed.path[0:4] =='/ct/'\n",
    "                values=parsed.query[2:6]\n",
    "    except:\n",
    "        values =''\n",
    "    return  values"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Transforming one RDD to another"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "main_files_conv = main_file.map(transformsnumer)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[[u'/ls/', u'62', u'/ls/', u'62'],\n",
       " [u'/ct/', u'158', '', ''],\n",
       " [u'/klient/', '', u'/klient/', ''],\n",
       " [u'/dt/', u'9354', '', ''],\n",
       " ['', '', '', ''],\n",
       " [u'/ls/', u'67', u'/ls/', u'67'],\n",
       " [u'/dt/', u'3475', u'/ls/', u'62'],\n",
       " [u'/dt/', u'10687', u'/ls/', u'18'],\n",
       " [u'/ls/', u'62', u'/ls/', u'62'],\n",
       " [u'/ls/', u'3', u'/ct/', u'141']]"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "main_files_conv.take(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "Entire_Files_DF= main_files_conv.toDF([\"Visited\",\"ID\",\"Referrer\",\"ID_Referrer\"]) ## transfering rdd to sqlDF"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Visited  ID    Referrer ID_Referrer\n",
      "/ls/     62    /ls/     62         \n",
      "/ct/     158                       \n",
      "/klient/       /klient/            \n",
      "/dt/     9354                      \n",
      "                                   \n",
      "/ls/     67    /ls/     67         \n",
      "/dt/     3475  /ls/     62         \n",
      "/dt/     10687 /ls/     18         \n",
      "/ls/     62    /ls/     62         \n",
      "/ls/     3     /ct/     141        \n"
     ]
    }
   ],
   "source": [
    "Entire_Files_DF.show(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Querying pages where visited = '/ls/-product listing' and referrer = '/ct/-product category '"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Final_Analysis1=Entire_Files_DF.where(Entire_Files_DF.Visited=='/ls/') ## subset the dataframe based on first condt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1363187L"
      ]
     },
     "execution_count": 128,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Final_Analysis1.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Final_Analysis=Final_Analysis1.where(Final_Analysis1.Referrer=='/ct/') ## subset the dataframe based on second condt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "179512L"
      ]
     },
     "execution_count": 130,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Final_Analysis.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 131,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Visited ID  Referrer ID_Referrer\n",
      "/ls/    3   /ct/     141        \n",
      "/ls/    38  /ct/     158        \n",
      "/ls/    106 /ct/     505        \n",
      "/ls/    3   /ct/     141        \n",
      "/ls/    33  /ct/     155        \n",
      "/ls/    51  /ct/     163        \n",
      "/ls/    34  /ct/     155        \n",
      "/ls/    70  /ct/     171        \n",
      "/ls/    74  /ct/     172        \n",
      "/ls/    134 /ct/     506        \n"
     ]
    }
   ],
   "source": [
    "Final_Analysis.show(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "Last_trans= Final_Analysis.where(Final_Analysis.ID_Referrer>0) ## subset the dataframe removing blank lines on visit_ID\n",
    "#Last_tans.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "174258L"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Final_Df=Last_trans.where(Last_trans.ID>0)## subset the dataframe removing blank lines on referrer_ID\n",
    "Final_Df.count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Visited ID  Referrer ID_Referrer\n",
      "/ls/    3   /ct/     141        \n",
      "/ls/    38  /ct/     158        \n",
      "/ls/    106 /ct/     505        \n",
      "/ls/    3   /ct/     141        \n",
      "/ls/    33  /ct/     155        \n",
      "/ls/    51  /ct/     163        \n",
      "/ls/    34  /ct/     155        \n",
      "/ls/    70  /ct/     171        \n",
      "/ls/    74  /ct/     172        \n",
      "/ls/    134 /ct/     506        \n"
     ]
    }
   ],
   "source": [
    "Final_Df.show(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##Converting to Pandas for visualizing in Neo4j (Graph DB)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "FinalPD= Final_Df.toPandas()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Final_output=FinalPD.groupby([\"ID\", \"ID_Referrer\"]).size().reset_index(name=\"Frequency\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ID</th>\n",
       "      <th>ID_Referrer</th>\n",
       "      <th>Frequency</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>140</td>\n",
       "      <td>873</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>141</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10</td>\n",
       "      <td>145</td>\n",
       "      <td>2466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10</td>\n",
       "      <td>160</td>\n",
       "      <td>186</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10</td>\n",
       "      <td>173</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>10</td>\n",
       "      <td>174</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>10</td>\n",
       "      <td>465</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>100</td>\n",
       "      <td>388</td>\n",
       "      <td>432</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>101</td>\n",
       "      <td>401</td>\n",
       "      <td>1650</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>102</td>\n",
       "      <td>401</td>\n",
       "      <td>635</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    ID ID_Referrer  Frequency\n",
       "0    1         140        873\n",
       "1    1         141          1\n",
       "2   10         145       2466\n",
       "3   10         160        186\n",
       "4   10         173          4\n",
       "5   10         174         11\n",
       "6   10         465         10\n",
       "7  100         388        432\n",
       "8  101         401       1650\n",
       "9  102         401        635"
      ]
     },
     "execution_count": 136,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Final_output.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 157,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "Final_list=Final_output.values.tolist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##Importing dimension tables"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'140\\tKlasick\\xe9 fotoapar\\xe1ty\\tFilm cameras'"
      ]
     },
     "execution_count": 137,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "category=sc.textFile(\"hdfs://localhost:8020/user/training/assignment/category/*\")\n",
    "category.first()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 138,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def transformers(intstr):\n",
    "    attLst =intstr.split(\"\\t\")\n",
    "    values=([attLst[0],attLst[2]])\n",
    "    return values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 139,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[u'140', u'Film cameras']"
      ]
     },
     "execution_count": 139,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat=category.map(transformers)\n",
    "cat.first()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id  category_name       \n",
      "140 Film cameras        \n",
      "141 Digital cameras     \n",
      "142 Zoom lenses         \n",
      "143 Standard lenses     \n",
      "144 Accessories         \n",
      "145 Data recording media\n",
      "146 HiFi systems        \n",
      "147 HiFi components     \n",
      "148 Earphones           \n",
      "149 Cassette radios     \n"
     ]
    }
   ],
   "source": [
    "category_df=cat.toDF([\"id\",\"category_name\"])\n",
    "category_df.show(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "category_Pdf=category_df.toPandas()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 218,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "category_list=category_Pdf.values.tolist()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 143,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "u'1\\tKlasick\\xe9 fotoapar\\xe1ty\\tFilm cameras'"
      ]
     },
     "execution_count": 143,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product=sc.textFile(\"hdfs://localhost:8020/user/training/assignment/list/*\")\n",
    "product.first()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "prod=product.map(transformers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 145,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "id product_name        \n",
      "1  Film cameras        \n",
      "2  Film SLR cameras    \n",
      "3  Digital cameras     \n",
      "4  Digital SLR cameras \n",
      "5  Lenses - manual zoom\n",
      "6  Lenses - auto zoom  \n",
      "7  Lenses - manual f...\n",
      "8  Lenses - auto fixed \n",
      "9  Flash lights        \n",
      "10 Memories            \n"
     ]
    }
   ],
   "source": [
    "product_df=prod.toDF([\"id\",\"product_name\"])\n",
    "product_df.show(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 146,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "product_Pdf=product_df.toPandas()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 214,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>product_name</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Film cameras</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Film SLR cameras</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Digital cameras</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Digital SLR cameras</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Lenses - manual zoom</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>Lenses - auto zoom</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>7</td>\n",
       "      <td>Lenses - manual fixed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>8</td>\n",
       "      <td>Lenses - auto fixed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>9</td>\n",
       "      <td>Flash lights</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>10</td>\n",
       "      <td>Memories</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id           product_name\n",
       "0   1           Film cameras\n",
       "1   2       Film SLR cameras\n",
       "2   3        Digital cameras\n",
       "3   4    Digital SLR cameras\n",
       "4   5   Lenses - manual zoom\n",
       "5   6     Lenses - auto zoom\n",
       "6   7  Lenses - manual fixed\n",
       "7   8    Lenses - auto fixed\n",
       "8   9           Flash lights\n",
       "9  10               Memories"
      ]
     },
     "execution_count": 214,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "product_Pdf.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 217,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "product_list=product_Pdf.values.tolist()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##Importing required packages from neo4j"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from py2neo import Graph, Path\n",
    "from py2neo import Node,Relationship\n",
    "from py2neo import authenticate"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "authenticate(\"localhost:7474\",\"training\",\"training\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "graph=Graph(\"http://localhost:7474/db/data/\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "###Creating nodes and relationships; with properties"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ctx = graph.cypher.begin()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "for id,category_name in category_list:\n",
    "    ctx.append(\"create (c:category {name:{category_name}, id:{id}}) return c\",id=id,category_name=category_name)\n",
    "    #tx.append(\"CREATE (person:Person {name:{name}}) RETURN person\", name=name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {
    "collapsed": false,
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "category = [result.one for result in ctx.commit()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "ptx = graph.cypher.begin()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 194,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "for id,product_name in product_list:\n",
    "    ptx.append(\"create (p:product {name:{product_name}, id:{id}}) return p\",id=id,product_name=product_name)\n",
    "    #tx.append(\"CREATE (person:Person {name:{name}}) RETURN person\", name=name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "product=[result.one for result in ptx.commit()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "for ID,ID2,Frequency in Final_list:\n",
    "    graph.cypher.execute(\"match(p:product {id:{id1}})\\\n",
    "                         match(c:category {id:{id2}})\\\n",
    "                         create ((c)-[:refered{frequency:{frequency}}]->(p))\",id1=ID,id2=ID2,frequency=Frequency)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##Future scope"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### > Recommendation based on User patterns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### > Include Brands in the analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### > Identify Fraud based on the entire session"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
