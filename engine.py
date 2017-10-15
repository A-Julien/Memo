from bs4 import BeautifulSoup as Soup
import random
import glob

html = """
<!DOCTYPE HTML>
<!--
	Phantom by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
-->
<html>
	<head>
		<title>Memo</title>
		<meta charset="utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" />
		<!--[if lte IE 8]><script src="assets/js/ie/html5shiv.js"></script><![endif]-->
		<link rel="stylesheet" href="assets/css/main.css" />
		<!--[if lte IE 9]><link rel="stylesheet" href="assets/css/ie9.css" /><![endif]-->
		<!--[if lte IE 8]><link rel="stylesheet" href="assets/css/ie8.css" /><![endif]-->
	</head>
	<body>
		<!-- Wrapper -->
			<div id="wrapper">

				<!-- Header -->
					<header id="header">
						<div class="inner">

							<!-- Logo -->
								<a href="" class="logo">
									<span class="title">Memo</span>
								</a>
						</div>
					</header>
				<!-- Main -->
					<div id="main">
						<div class="inner">
							<header>
								<h1>This is Memo for my brain</h1>
							</header>
							<section class="tiles" id="append">
							</section>
						</div>
					</div>
			</div>

		<!-- Scripts -->
			<script src="assets/js/jquery.min.js"></script>
			<script src="assets/js/skel.min.js"></script>
			<script src="assets/js/util.js"></script>
			<!--[if lte IE 8]><script src="assets/js/ie/respond.min.js"></script><![endif]-->
			<script src="assets/js/main.js"></script>

	</body>
</html>
"""
soup = Soup(html,'html.parser')
rand = 0

for filename in glob.iglob('/home/pi/Memo/config/compile/*.html'):
    file = str(filename)
    buf = random.randint(1, 9)
    while str(buf) == rand:
        buf = random.randint(1, 4)
    rand = str(buf)
    print file
    namePath = file.split("/")[-1]
    title = file.split("/")[-1].split(".")[0].split("_")[0]
    print title
    article = '<article class=\"style'+ rand +'\">' \
              '<span class=\"image\">' \
              '<img src=\"images/pic0'+ rand +'.jpg\" alt=\"\" />' \
              '</span>' \
              '<a href=\"compile/'+ namePath +'\">' \
              "<h2>"+title+"</h2>" \
              '<div class=\"content\">' \
              "<p>"+ title +"</p>" \
              '</div>' \
              '</a>' \
              '</article>'
    print article
    soup.section.append(Soup(article, 'html.parser'))


print soup
filename = "/home/pi/index.html"

raw = open(filename, "r+")
contents = raw.read().split("\n")
raw.seek(0)
raw.truncate()
raw.write(str(soup))
