import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
from load_css import local_css
from wordcloud import WordCloud
from wordcloud import ImageColorGenerator
import matplotlib.pyplot as plt

local_css("style.css")
 

#with open("style.css") as f:
    #st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
st.set_option('deprecation.showPyplotGlobalUse', False)


#####################
# Header 
st.markdown("""
<style>
.font_fam {
    font_family:serif !important;
}
</style>
""", unsafe_allow_html=True)

#st.markdown('<p class="font_color">Hello World !!</p>', unsafe_allow_html=True)
st.write('''
# Marcela AGUILERA-BLANC 
### Data Analyst Jr.

''')

image = Image.open('mab.png')
st.image(image, width=350)

st.markdown("## Profil", unsafe_allow_html=True)
st.info('''
Diplômée d'une licence en marketing et forte de 10 ans d'expérience dans le milieu de l'enseignement, je suis actuellement en reconversion dans les métiers du développement. Au cours du stage intégré à ma formation, j'ai pu mettre en œuvre mes compétences en développement. J'ai aussi été amenée à travailler avec des données, ce qui m'a particulièrement intéressé et m'a conduit à suivre la formation tremplin data analyst chez Matrice. Je recherche aujourd'hui un contrat d'alternance dans le domaine de la data à partir de septembre 2022 (4 jours en entreprise, 1 jour en formation).
''')

#####################
# Navigation

st.markdown("""<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
""" , unsafe_allow_html=True)
          
st.markdown("""

<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #f75940; font-family: Courier New, monospace;">
  <a class="navbar-brand" href="#" target="_blank">MAB</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#formation">Formation</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experiences-professionnelles">Experiences Professionnelles</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#langues">Langues</a>
      </li>
       <li class="nav-item">
        <a class="nav-link" href="#data">Data</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#hobbies">Hobbies</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#contact">Contact</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([5,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Formation
''')

txt('**Tremplin Data Analyst**  *Matrice*, Paris',
'avril - juillet 2022')
st.markdown('''
- Data Analysis, data cleaning, data visualisation & exploration
- Web scraping & reporting
- Machine learning 
''')

txt('**Développement Web & Web mobile**  *DesCodeuses*, Paris',
'février - juillet 2021')
st.markdown('''
- Apprentissage du développement web
- Maîtrise des langages informatiques et frameworks 
- Réalisation de projets individuels & en groupe
''')

txt('**CELTA Certificat de Cambridge**  *ILC France*, Paris',
'2018')
st.markdown('''
- diplôme pour enseigner l'anglais en école primaire et secondaire privée 
  ou pour être vacataire dans l'Éducation Nationale.
''')

txt('**Fashion Marketing & Merchandising**$~$' '*International Academy of Design & Technology*' 'Toronto',
'2000 - 2003')
st.markdown('''
- Merchandising, achat, vente au détail, stratégie marketing, 
- Relations publiques, 
- Développement de produits et gestion de marque 
''')


#####################
st.markdown('''
## Experiences Professionnelles
''')

txt('**Développeuse application python (stage)**, ITRMG Group, BNP Paribas, Montreuil',
'septembre 2021 - mars 2022')
st.markdown('''
- Conception d'un outil interne d'automatisation au sein du groupe ITRMG    
- Modélisation et construction d'une base de données
- Agrégation de données
- Visualisation des données via une application Django
- Interfaçage avec différentes solutions API
''')

txt('**Formatrice & Conceptrice Pedagogique**, obEiNGLISH, Paris',
'novembre 2019- janvier 2021')
st.markdown('''
- Cours d'anglais tous niveaux (supérieur, collège et primaire, professionnel) 
- Conception de stages intensifs en ligne et présentiel tous niveaux 
- Création de supports pédagogiques numériques
''')
txt('**Enseignante**, (primaire), Yel World School, Perpignan',
'2018-2019')
txt('**Formatrice & Animatrice**, (freelance), The English Express, Perpignan',
'2010-2018')


#####################
st.markdown('''
## Projets Web
''')
txt4('LibIt', ' :desktop_computer: Site de partage de ressources web gratuites à utiliser librement Outils : HTML, CSS, Javascript, Jquery, PHP, MySql', 'http://codes.bio/abcpred/')
txt4('Sounds Good', ' :musical_score: Site e-commerce avec fonctionnalités : panier et barre de recherche. Outils : HTML, CSS, Bootstrap, Javascript, Jquery', 'http://codes.bio/abcpred/')
txt4('Pac-Man', ' :ghost: Remake du jeu culte Pac-man en Javascript . Outils : HTML, CSS, Javascript', 'http://codes.bio/abcpred/')

######################
st.markdown('''
## Data
''')
# Another container
stats_container = st.container()	
with stats_container:


	# 4 --- You import datasets like you always do with pandas
	# 		if you'd like to import data from a database, you need to set up a database connection
	data = pd.read_csv('JC-202103-citibike-tripdata.csv')


	# 5 --- You can work with data, change it and filter it as you always do using Pandas or any other library
	start_station_list = ['All'] + data['start station name'].unique().tolist()
	end_station_list = ['All'] + data['end station name'].unique().tolist()


	# 6 --- collecting input from the user
	#		Steamlit has built in components to collect input from users


	# collect input using a list of options in a drop down format
	# TODO: change the option list to end_station_list and see what happens
	st.write('Or you can ask the user to select an option from the dropdown menu')
	s_station = st.selectbox('Which start station would you like to see?', start_station_list, key='start_station')

	# display the collected input
	st.write('You selected the station: ' + str(s_station))

	# you can filter/alter the data based on user input and display the results in a plot
	st.write('And display things based on what the user has selected')
	if s_station != 'All':
		display_data = data[data['start station name'] == s_station]

	else:
		display_data = data.copy()


	# display the dataset in a table format
	# if you'd like to customize it more, consider plotly tables: https://plotly.com/python/table/
	# I have a YouTube tutorial that can help you in this: https://youtu.be/CYi0pPWQ1Do
	st.write(display_data)



	# 7 --- creating columns inside a container 
	#		(you can create more than 2)
	bar_col, pie_col = st.columns(2)
   
	# in order to display things inside columns, replace the st. with the column name when creating components

	# preparing data to display on pie chart
	user_type = data['usertype'].value_counts().reset_index()
	user_type.columns = ['user type','count']






	# 8 --- Creating plots and charts
	#		The simplest way is to use the built in Streamlit plots
	#		You can also use other plotting libraries with Streamlit
	#		The pie chart below is an example of using Plotly


	# preparing data to display in a bar chart
	start_location = data['start station name'].value_counts()

	# don't forget to add titles to your plots
	bar_col.text('Trip duration in minutes per start station')

	# This is the way to make a very simple bar chart 
	# Visit https://docs.streamlit.io/en/stable/api.html for more information on what other plots and charts are possible
	bar_col.line_chart(start_location)


	# don't forget to add titles to your plots
	pie_col.text('How many of the users were subscribed?')

	# This is an example of a plotly pie chart
	fig = px.pie(user_type, values='count', names = 'user type', hover_name='user type')

	# TODO: change the values of the update_layout function and see the effect
	fig.update_layout(showlegend=False,
		width=400,
		height=400,
		margin=dict(l=1,r=1,b=1,t=1),
		font=dict(color='#383635', size=15))

	# this function adds labels to the pie chart
	# for more information on this chart, visit: https://plotly.com/python/pie-charts/
	fig.update_traces(textposition='inside', textinfo='percent+label')

	# after creating the chart, we display it on the app's screen using this command
	pie_col.write(fig)


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`')
#txt3('Machine Learning', '`scikit-learn`')
#txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Django`,`Flask`, `HTML`, `CSS`, `JavaScript`, `PHP`')
#txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
st.markdown('''
## Langues
''')

st.markdown('''

- Anglais (langue maternelle)
- Espanol (langue maternelle)
''')


#####################
st.markdown('''
## Hobbies
''')

st.markdown('''

- Jeux de stratégie et réflexion
- Courir, faire du rollers
- Expérimenter de nouvelles recette
''')
# Create some sample text
text = 'Fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image:
wordcloud = WordCloud(max_font_size=50, colormap='rainbow',background_color="white").generate(text)

# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()



#####################
st.markdown('''
  ## Contact
  ''')
st.markdown('''
Got a catchy idea for a project collab or want to get in touch to know more about my interests?   
Hit me up! I'm all ears.   
Email me at marcela.aguilerablanc@gmail.com   

or via

''')
txt2('LinkedIn', 'www.linkedin.com/in/marcela-aguilera-blanc')

