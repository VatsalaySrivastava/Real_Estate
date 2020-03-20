#!d:\Python34\python.exe
print("""
<!DOCTYPE html>
<html lang="en">
<head>
	<title>LERAMIZ - Landing Page Template</title>
	<meta charset="UTF-8">
	<meta name="description" content="LERAMIZ Landing Page Template">
	<meta name="keywords" content="LERAMIZ, unica, creative, py">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<!-- Favicon -->   
	<link href="img/favicon.ico" rel="shortcut icon"/>

	<!-- Google Fonts -->
	<link href="https://fonts.googleapis.com/css?family=Source+Sans+Pro" rel="stylesheet">

	<!-- Stylesheets -->
	<link rel="stylesheet" href="css/bootstrap.min.css"/>
	<link rel="stylesheet" href="css/font-awesome.min.css"/>
	<link rel="stylesheet" href="css/animate.css"/>
	<link rel="stylesheet" href="css/owl.carousel.css"/>
	<link rel="stylesheet" href="css/style.css"/>


	<!--[if lt IE 9]>
	  <script src="https://oss.maxcdn.com/py5shiv/3.7.2/py5shiv.min.js"></script>
	  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	<![endif]-->

</head>
<body>
	<!-- Page Preloder -->
	<div id="preloder">
		<div class="loader"></div>
	</div>
	
	<!-- Header section -->
	<header class="header-section">
		<div class="header-top">
			<div class="container">
				<div class="row">
					<div class="col-lg-6 header-top-left">
						<div class="top-info">
							<i class="fa fa-phone"></i>
							(+91) 9842493598
						</div>
						<div class="top-info">
							<i class="fa fa-envelope"></i>
							realstate@gmail.com
						</div>
					</div>
					<div class="col-lg-6 text-lg-right header-top-right">
						<div class="top-social">
							<a href=""><i class="fa fa-facebook"></i></a>
							<a href=""><i class="fa fa-twitter"></i></a>
							<a href=""><i class="fa fa-instagram"></i></a>
							<a href=""><i class="fa fa-pinterest"></i></a>
							<a href=""><i class="fa fa-linkedin"></i></a>
						</div>
						<div class="user-panel">
							<a href="register.py"><i class="fa fa-user-circle-o"></i> Register</a>
							
						</div>
					</div>
				</div>
			</div>
		</div>
		<div class="container">
			<div class="row">
				<div class="col-12">
					<div class="site-navbar">
						<a href="index.py" class="site-logo"><img src="img/logo.png" alt=""></a>
						<div class="nav-switch">
							<i class="fa fa-bars"></i>
						</div>
						<ul class="main-menu">
							<li><a href="index.py">Home</a></li>
							<li><a href="categories.py">FEATURED LISTING</a></li>
							<li><a href="about.py">ABOUT US</a></li>
							<li><a href="single-list.py">Pages</a></li>
							<li><a href="blog.py">Blog</a></li>
							<li><a href="contact.py">Contact</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</header>
	<!-- Header section end -->


	<!-- Page top section -->
	<section class="page-top-section set-bg" data-setbg="img/page-top-bg.jpg">
		<div class="container text-white">
			<h2>Featured Listings</h2>
		</div>
	</section>
	<!--  Page top end -->

	<!-- Breadcrumb -->
	<div class="site-breadcrumb">
		<div class="container">
			<a href=""><i class="fa fa-home"></i>Home</a>
			<span><i class="fa fa-angle-right"></i>Featured Listings</span>
		</div>
	</div>


	<!-- page -->
	<section class="page-section categories-page">
		<div class="container">
			<div class="row">
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/1.jpg">
							<div class="sale-notic">FOR SALE</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>1963 C Block Gomti Nagar</h5>
								<p><i class="fa fa-map-marker"></i> Lucknow ,UP 226004</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 800 Square foot</p>
										<p><i class="fa fa-bed"></i> 10 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 2 Garages</p>
										<p><i class="fa fa-bath"></i> 6 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Tony Holland</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 1 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 1,92,00,000</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/2.jpg">
							<div class="sale-notic">FOR SALE</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>17 Sturges Road,Bandra Hills</h5>
								<p><i class="fa fa-map-marker"></i> palwa,Mumbai 90210</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 1500 Square foot</p>
										<p><i class="fa fa-bed"></i> 16 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 2 Garages</p>
										<p><i class="fa fa-bath"></i> 8 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Gina Wesley</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 1 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 1,45,00,000</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/3.jpg">
							<div class="rent-notic">FOR Rent</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>305 North Palm Drive</h5>
								<p><i class="fa fa-map-marker"></i> Beverly Hills, CA 90210</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 1500 Square foot</p>
										<p><i class="fa fa-bed"></i> 16 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 2 Garages</p>
										<p><i class="fa fa-bath"></i> 8 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Gina Wesley</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 1 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 20,500/month</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/4.jpg">
							<div class="sale-notic">FOR SALE</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>28 Quaker Ridge Road, Lucknow</h5>
								<p><i class="fa fa-map-marker"></i> 28 Quaker Ridge Road, Lucknow</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 1200 Square foot</p>
										<p><i class="fa fa-bed"></i> 12 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 3 Garages</p>
										<p><i class="fa fa-bath"></i> 8 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Sasha Gordon </p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 8 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 56,00,000</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/5.jpg">
							<div class="rent-notic">FOR Rent</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>Sofi Berryessa 750 N King Road</h5>
								<p><i class="fa fa-map-marker"></i>Goa, CA 95133</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 500 Square foot</p>
										<p><i class="fa fa-bed"></i> 4 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 1 Garages</p>
										<p><i class="fa fa-bath"></i> 2 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Gina Wesley</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 8 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 15,600/month</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/6.jpg">
							<div class="sale-notic">FOR SALE</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>1203 Orren Street, Northeast</h5>
								<p><i class="fa fa-map-marker"></i> Pune, DC 20002</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 700 Square foot</p>
										<p><i class="fa fa-bed"></i> 7 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 1 Garages</p>
										<p><i class="fa fa-bath"></i> 7 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Sasha Gordon </p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 8 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 1,16,00,000</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/7.jpg">
							<div class="sale-notic">FOR SALE</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>1476 Harvard St NW Unit Ph</h5>
								<p><i class="fa fa-map-marker"></i> New Delhi, DC 20009</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 550 Square foot</p>
										<p><i class="fa fa-bed"></i> 7 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 1 Garages</p>
										<p><i class="fa fa-bath"></i> 3 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Adam Johnson</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 1 days ago</p>
									</div>	
								</div>
							</div>
,							<a href="#" class="room-price">Rs 82,50,000</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/8.jpg">
							<div class="sale-notic">FOR SALE</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>9633 Weathered Oak Ct</h5>
								<p><i class="fa fa-map-marker"></i> Mumbai, MD 208179</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 1000 Square foot</p>
										<p><i class="fa fa-bed"></i> 6 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 2 Garages</p>
										<p><i class="fa fa-bath"></i> 8 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Ann Hathaway</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 1 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 12,30,000</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/9.jpg">
							<div class="rent-notic">FOR Rent</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>2529 Marsh Hill Henry Rd Unit Mc</h5>
								<p><i class="fa fa-map-marker"></i> Chennai, MD 21541</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 550 Square foot</p>
										<p><i class="fa fa-bed"></i> 4 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 1 Garages</p>
										<p><i class="fa fa-bath"></i> 2 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i>  McHenry, MD 21541</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 1 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 18,000/month</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/10.jpg">
							<div class="sale-notic">FOR SALE</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>6335 N Magnolia Ave Apt 1S</h5>
								<p><i class="fa fa-map-marker"></i> Kolkata, IL 60660</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i> 2200 Square foot</p>
										<p><i class="fa fa-bed"></i> 16 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 3 Garages</p>
										<p><i class="fa fa-bath"></i> 10 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Tony Holland </p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 8 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 7,16,00,000</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/11.jpg">
							<div class="rent-notic">FOR Rent</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>441 E Maywood Ct</h5>
								<p><i class="fa fa-map-marker"></i> Ghaziabad, IL 62526</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i>   750 Square foot</p>
										<p><i class="fa fa-bed"></i> 5 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 1 Garages</p>
										<p><i class="fa fa-bath"></i> 3 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i> Chris Brown</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 8 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 19,800/month</a>
						</div>
					</div>
				</div>
				<div class="col-lg-4 col-md-6">
					<!-- feature -->
					<div class="feature-item">
						<div class="feature-pic set-bg" data-setbg="img/feature/12.jpg">
							<div class="sale-notic">FOR SALE</div>
						</div>
						<div class="feature-text">
							<div class="text-center feature-title">
								<h5>712 Southland Circle Dr</h5>
								<p><i class="fa fa-map-marker"></i> Noida, IL 61953</p>
							</div>
							<div class="room-info-warp">
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-th-large"></i>   200 Square foot</p>
										<p><i class="fa fa-bed"></i> 2 Bedrooms</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-car"></i> 1 Garages</p>
										<p><i class="fa fa-bath"></i> 2 Bathrooms</p>
									</div>	
								</div>
								<div class="room-info">
									<div class="rf-left">
										<p><i class="fa fa-user"></i>  Gina Wesley</p>
									</div>
									<div class="rf-right">
										<p><i class="fa fa-clock-o"></i> 8 days ago</p>
									</div>	
								</div>
							</div>
							<a href="#" class="room-price">Rs 46,35,000</a>
						</div>
					</div>
				</div>
			</div>
			<div class="site-pagination">
				<span>1</span>
				<a href="#">2</a>
				<a href="#">3</a>
				<a href="#"><i class="fa fa-angle-right"></i></a>
			</div>
		</div>
	</section>
	<!-- page end -->





<!-- Footer section -->
	<footer class="footer-section set-bg" data-setbg="img/footer-bg.jpg">
		<div class="container">
			<div class="row">
				
				<div class="col-lg-3 col-md-6 footer-widget">
					<div class="contact-widget">
						<h5 class="fw-title">CONTACT US</h5>
						<p><i class="fa fa-map-marker"></i>One BKC, Bandra Kurla Complex, Bandra (E), Mumbai, India 400051</p>
						<p><i class="fa fa-phone"></i>(+88) 9842493598</p>
						<p><i class="fa fa-envelope"></i>realstate@gmail.com</p>
						<p><i class="fa fa-clock-o"></i>Mon - Sat, 08 AM - 06 PM</p>
					</div>
				</div>
				<div class="col-lg-3 col-md-6 footer-widget">
					<div class="double-menu-widget">
						<h5 class="fw-title">POPULAR PLACES</h5>
						<ul>
							<li><a href="">Bengaluru</a></li>
							<li><a href="">New Delhi</a></li>
							<li><a href="">Mumbai</a></li>
							<li><a href="">Kolkata</a></li>
							<li><a href="">Chennai</a></li>
						</ul>
						<ul>
							<li><a href="">Punjab</a></li>
							<li><a href="">Jaipur</a></li>
							<li><a href="">Lucknow</a></li>
							<li><a href="">Goa</a></li>
							<li><a href="">Orissa</a></li>
						</ul>
					</div>
				</div>
				<div class="col-lg-3 col-md-6  footer-widget">
					<div class="newslatter-widget">
						<h5 class="fw-title">NEWSLETTER</h5>
						<p>Subscribe your email to get the latest news and new offer also discount</p>
						<form class="footer-newslatter-form">
							<input type="text" placeholder="Email address">
							<button><i class="fa fa-send"></i></button>
						</form>
					</div>
				</div>
			</div>
			<div class="footer-bottom">
				<div class="copyright">
					<p><!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved 
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
				</div>
			</div>
		</div>
	</footer>
	<!-- Footer section end -->
                                        
	<!--====== Javascripts & Jquery ======-->
	<script src="js/jquery-3.2.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/owl.carousel.min.js"></script>
	<script src="js/masonry.pkgd.min.js"></script>
	<script src="js/magnific-popup.min.js"></script>
	<script src="js/main.js"></script>
</body>
</html>
""")
