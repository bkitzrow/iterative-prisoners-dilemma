
<!DOCTYPE html>
<!--[if gte IE 9 ]><html class="ie ie9 scripts-not-loaded" lang="en"> <![endif]-->
<!--[if !(IE)]><!--> <html class="not-ie scripts-not-loaded" lang="en"> <!--<![endif]-->
<head>
  <meta charset="utf-8">
  <title>
  1.3.9.P.PY prisoners_dilemma.py: CS-CSE - 2014 - Oklahoma State University - 20140615
</title>
  <noscript> <h1>You need to have javascript enabled in order to access this site.</h1> </noscript>
  <!--[if lte IE 8]> <meta http-equiv=refresh content="0; URL=/ie-8-is-not-supported.html" /> <![endif]-->

  
  <link href="/assets/vendor_legacy_normal_contrast.css?1403712865" media="all" rel="stylesheet" type="text/css" />
<link href="/assets/common_legacy_normal_contrast.css?1403712872" media="all" rel="stylesheet" type="text/css" />
  
  <meta content="app-id=480883488" name="apple-itunes-app" />
  
  
  <link href="https://my.pltw.org/sites/default/files/canvas_pltw.css" media="all" rel="stylesheet" type="text/css" />
  <script>
    // listen for any clicks on links that have href="#" and queue them to be fired on dom ready.
      function _earlyClick(e){
        var cur = e.target || e.srcElement;
        while ( cur && cur.ownerDocument ) {
          if ( cur.getAttribute('href') == '#' ) {
            e.preventDefault();
            _earlyClick.clicks = _earlyClick.clicks || [];
            _earlyClick.clicks.push(cur);
            break;
          }
          cur = cur.parentNode;
        }
      }
      document.addEventListener('click', _earlyClick);
  </script>
</head>
<body class="with-left-side files context-course_167642">


<ul id="flash_message_buffer" aria-hidden="true">
  
</ul>
<ul id="flash_message_holder">
  
</ul>
<div id="flash_screenreader_holder" class="screenreader-only" role="alert">
</div>


<div id="header" class="no-print ">
  <div id="header-inner">
    <a href="#content" id="skip_navigation_link">Skip To Content</a>
    <a id="header-logo" href="https://pltw.instructure.com/">My Dashboard</a>
    <b id="header-logo-secondary"></b>
    <div id="topbar">
          <ul id="identity">
      <li class="user_name"><a href="/about/404463">Bryan Kitzrow</a></li>
      <li class="first inbox"><a href="/conversations?"><span>Inbox</span>
      <b class="unread-messages-count" style="display: none;">0</b>
      </a></li>
    <li><a href="/profile/settings">Settings</a></li>
    <li class="user_id" style="display: none;">404463</li>
    <li class="course_id" style="display: none;">167642</li>
    <li id="current_context_code" style="display: none;">course_167642</li>
    <li class="user_long_name" style="display: none;">Bryan Kitzrow</li>
    <li class="logout"><a href="/logout" onclick="var f = document.createElement('form'); f.style.display = 'none'; this.parentNode.appendChild(f); f.method = 'POST'; f.action = this.href;var m = document.createElement('input'); m.setAttribute('type', 'hidden'); m.setAttribute('name', '_method'); m.setAttribute('value', 'delete'); f.appendChild(m);var s = document.createElement('input'); s.setAttribute('type', 'hidden'); s.setAttribute('name', 'authenticity_token'); s.setAttribute('value', 'kwXHiFmFjTIS6r2nUPzTxIV1ZZKb/w+z6Jkja6iu4EZC/i1ywr4I/gP7oifO0hYXWtQ9JwQK3KRv67i4qm4Qkw=='); f.appendChild(s);f.submit();return false;">Logout</a></li>
    <li id="identity-help-container"><a href="http://help.instructure.com/" class="support_url help_dialog_trigger" data-track-category="help system" data-track-label="help button">Help</a></li>
</ul>

    </div>
    
    <ul role="navigation" id="menu" aria-label="Main Navigation">
      <li id="courses_menu_item" class="menu-item">
          <a href="/courses" class="menu-item-title">
  Courses  <span class="menu-item-title-icon"></span> <i class="icon-mini-arrow-down"></i></a>
<div class="menu-item-drop">
  <table cellspacing="0">
    <tr>
      <td class="menu-item-drop-column" id="menu_enrollments">
  <span class="menu-item-heading">
    My Courses
  </span>
  <div class="menu-item-customize">
    <a class="customListOpen" href="#">Customize</a>
  </div>
  <ul class="menu-item-drop-column-list">
    <li class="customListItem" data-id="186101">
  <a href="/courses/186101">
    <span class="name ellipsis" title="Engineering Design and Development 2014 BKitzrow 01 - Engineering Design and Development 2014 BKitzrow 01">Engineering Design and Development 2014 BKitzrow 01</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Teacher</span>
  </a>
</li>
<li class="customListItem" data-id="186097">
  <a href="/courses/186097">
    <span class="name ellipsis" title="Introduction to Engineering Design 2014 BKitzrow 01 - Introduction to Engineering Design 2014 BKitzrow 01">Introduction to Engineering Design 2014 BKitzrow 01</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Teacher</span>
  </a>
</li>
<li class="customListItem" data-id="129337">
  <a href="/courses/129337">
    <span class="name ellipsis" title="PLTW-PTE_EDD 2013 BKitzrow 01 - PLTW-PTE_EDD">PLTW-PTE_EDD 2013 BKitzrow 01</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Teacher</span>
  </a>
</li>
<li class="customListItem" data-id="135806">
  <a href="/courses/135806">
    <span class="name ellipsis" title="PLTW-PTE_IED 2013 BKitzrow 01 - PLTW-PTE_IED">PLTW-PTE_IED 2013 BKitzrow 01</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Teacher</span>
  </a>
</li>
<li class="customListItem" data-id="125288">
  <a href="/courses/125288">
    <span class="name ellipsis" title="PLTW-PTE_POE 2013 BKitzrow 01 - PLTW-PTE_POE">PLTW-PTE_POE 2013 BKitzrow 01</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Teacher</span>
  </a>
</li>
<li class="customListItem" data-id="186099">
  <a href="/courses/186099">
    <span class="name ellipsis" title="Principles of Engineering 2014 BKitzrow 01 - Principles of Engineering 2014 BKitzrow 01">Principles of Engineering 2014 BKitzrow 01</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Teacher</span>
  </a>
</li>
<li class="customListItem" data-id="46491">
  <a href="/courses/46491">
    <span class="name ellipsis" title="Assessment-PLC - 2013 - PLC-ASSESSMENT-2013-01">Assessment-PLC - 2013</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Student</span>
  </a>
</li>
<li class="customListItem" data-id="167642">
  <a href="/courses/167642">
    <span class="name ellipsis" title="CS-CSE - 2014 - Oklahoma State University - 20140615 - PD_CT-CS_CSE">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Student</span>
  </a>
</li>
<li class="customListItem" data-id="46549">
  <a href="/courses/46549">
    <span class="name ellipsis" title="EDD-OT - PD_OT-PTE_EDD-2013-01">EDD-OT</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Student</span>
  </a>
</li>
<li class="customListItem" data-id="46471">
  <a href="/courses/46471">
    <span class="name ellipsis" title="EDD-PLC - EDD-PLC">EDD-PLC</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Student</span>
  </a>
</li>
<li class="customListItem" data-id="46550">
  <a href="/courses/46550">
    <span class="name ellipsis" title="IED-OT - PD_OT-PTE_IED-2013-01">IED-OT</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Student</span>
  </a>
</li>
<li class="customListItem" data-id="46472">
  <a href="/courses/46472">
    <span class="name ellipsis" title="IED-PLC - IED-PLC">IED-PLC</span>
      <span class="subtitle ellipsis enrollment_term menu-item-drop-float-right"></span>
    <span class="subtitle ellipsis">Enrolled as: Student</span>
  </a>
</li>

    <li class="menu-item-view-all"><a href="/courses">View all courses (20)</a></li>
  </ul>
</td>

      

      

    </tr>
  </table>
</div>

      </li>
      <li id="assignments_menu_item" class="menu-item">
        <a href="/assignments" class="menu-item-title">Assignments<span class="menu-item-title-icon"></span> <i class="icon-mini-arrow-down"></i></a>
        <div class="menu-item-drop">
          <table cellspacing="0">
            <tr>
              
  <td class="menu-item-drop-column">
    <span class="menu-item-heading">Recently Graded</span>
    <ul class="menu-item-drop-column-list">
      
<li>
      <a href="/courses/167642/assignments/3604980" data-track-category="assignment dropdown" data-track-label="needs submitting">
    <span class="name-right-wrapper">
      <span class="secondary-right">
      </span>
      <span class="name ellipsis" title=&#x27;Problem 3.2.7 Investigate with Data &#x27;>Problem 3.2.7 Investigate with Data </span>
    </span>
    <span class="subtitle">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
  </a>  
</li>

<li>
      <a href="/courses/167642/assignments/3604992" data-track-category="assignment dropdown" data-track-label="needs submitting">
    <span class="name-right-wrapper">
      <span class="secondary-right">
      </span>
      <span class="name ellipsis" title=&#x27;Activity 4.1.2 Basic Control Circuits&#x27;>Activity 4.1.2 Basic Control Circuits</span>
    </span>
    <span class="subtitle">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
  </a>  
</li>

<li>
      <a href="/courses/167642/assignments/3604733" data-track-category="assignment dropdown" data-track-label="needs submitting">
    <span class="name-right-wrapper">
      <span class="secondary-right">
      </span>
      <span class="name ellipsis" >Daily Attendance Day 8</span>
    </span>
    <span class="subtitle">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
  </a>  
</li>

<li>
      <a href="/courses/167642/assignments/3604573" data-track-category="assignment dropdown" data-track-label="needs submitting">
    <span class="name-right-wrapper">
      <span class="secondary-right">
      </span>
      <span class="name ellipsis" title=&#x27;Core Training Day 7 Reflection: Recruitment [Required Core Training]&#x27;>Core Training Day 7 Reflection: Recruitment [Required Core Training]</span>
    </span>
    <span class="subtitle">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
  </a>  
</li>

<li>
      <a href="/courses/167642/assignments/3604570" data-track-category="assignment dropdown" data-track-label="needs submitting">
    <span class="name-right-wrapper">
      <span class="secondary-right">
      </span>
      <span class="name ellipsis" title=&#x27;Core Training Day 8 Reflection: Colleagues Across Disciplines [Required Core Training]&#x27;>Core Training Day 8 Reflection: Colleagues Across Disciplines [Required Core Training]</span>
    </span>
    <span class="subtitle">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
  </a>  
</li>

<li>
      <a href="/courses/167642/assignments/3604959" data-track-category="assignment dropdown" data-track-label="needs submitting">
    <span class="name-right-wrapper">
      <span class="secondary-right">
      </span>
      <span class="name ellipsis" title=&#x27;Activity 3.2.1 Inferential Statistics &#x27;>Activity 3.2.1 Inferential Statistics </span>
    </span>
    <span class="subtitle">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
  </a>  
</li>

<li>
      <a href="/courses/167642/assignments/3604954" data-track-category="assignment dropdown" data-track-label="needs submitting">
    <span class="name-right-wrapper">
      <span class="secondary-right">
      </span>
      <span class="name ellipsis" title=&#x27;Activity 3.1.5 Histograms and Distributions &#x27;>Activity 3.1.5 Histograms and Distributions </span>
    </span>
    <span class="subtitle">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
  </a>  
</li>

<li>
      <a href="/courses/167642/assignments/3604949" data-track-category="assignment dropdown" data-track-label="needs submitting">
    <span class="name-right-wrapper">
      <span class="secondary-right">
      </span>
      <span class="name ellipsis" title=&#x27;Activity 3.1.4 Pie Charts and Bar Graphs&#x27;>Activity 3.1.4 Pie Charts and Bar Graphs</span>
    </span>
    <span class="subtitle">CS-CSE - 2014 - Oklahoma State University - 20140615</span>
  </a>  
</li>

    </ul>
  </td>

            </tr>
          </table>
        </div>
      </li>
      <li id="grades_menu_item" class="menu-item">
        <a href="/grades" class="menu-item-no-drop">Grades</a>
      </li>
      <li id="calendar_menu_item" class="menu-item">
        <a href="/calendar" class="menu-item-no-drop">Calendar</a>
      </li>
    </ul>
  </div>
</div>
<div id="instructure_ajax_error_box">
  <div style="text-align: right; background-color: #fff;"><a href="#" class="close_instructure_ajax_error_box_link">Close</a></div>
  <iframe id="instructure_ajax_error_result" src="about:blank" style="border: 0;"></iframe>
</div>



<div id="wrapper-container">
  <div id="wrapper">
      <div id="left-side" class="list-view">
          <div class='h1' id="section-tabs-header">
            PD_CT-CS_CSE
          </div>
        <nav role="navigation" aria-label="context"><ul id="section-tabs"><li class='section '><a href="/courses/167642" class="home">Home</a></li><li class='section '><a href="/courses/167642/modules" class="modules">Modules</a></li><li class='section '><a href="/courses/167642/assignments" class="assignments">Assignments</a></li><li class='section '><a href="/courses/167642/grades" class="grades">Grades</a></li><li class='section '><a href="/courses/167642/discussion_topics" class="discussions">Discussions</a></li><li class='section '><a href="/courses/167642/users" class="people">People</a></li><li class='section '><a href="/courses/167642/collaborations" class="collaborations">Collaborations</a></li><li class='section '><a href="/courses/167642/files" class="files active">Files</a></li></ul></nav>
    </div>
    <div id="main">
      <div id="not_right_side">
        <div id="content-wrapper">
          <nav aria-label="breadcrumbs" id="breadcrumbs" role="navigation"><ul><li class="home"><a href="/"><span class="ellipsible">      <i class="icon-home standalone-icon"
         title="My Dashboard">
        <span class="screenreader-only">My Dashboard</span>
      </i>
</span></a></li><li><a href="/courses/167642"><span class="ellipsible">PD_CT-CS_CSE</span></a></li><li><a href="/courses/167642/files"><span class="ellipsible">Files</span></a></li><li><a href="/courses/167642/files/27100082"><span class="ellipsible">1.3.9.P.PY prisoners_dilemma.py</span></a></li></ul></nav>
	  <div id="right-side-wrapper">
	    <aside id="right-side" role="complementary">
	      
	    </aside>
	  </div>
          <div id="content" role="main" class="container-fluid">
                <iframe id="file_content" src="https://cluster20-files.instructure.com/courses/167642/files/27100082/course%20files/Unit%201%20Student/Lesson%201.3/1.3.9.P.PY%20prisoners_dilemma.py?download=1&amp;inline=1&amp;sf_verifier=805a0d43ffd5c9e645da17f07f7838c2&amp;ts=1403787039&amp;user_id=404463" style="width: 100%; height: 400px;"></iframe>

  <div id="sequence_footer" style="display: none;">
    <a class="prev btn" href="#">
      <i class="icon-arrow-left"></i> <span class="text">Previous</span>
      <span class="title ellipsis"></span>
    </a>
    <a class="next btn" href="#">
      <span class="text">Next</span> <i class="icon-arrow-right"></i>
      <span class="title ellipsis"></span>
    </a>
    <a href="/courses/167642/modules/items/sequence/attachment_27100082" style="display: none;" class="sequence_details_url">&nbsp;</a>
    <a href="/courses/167642/modules/items/%7B%7B%20id%20%7D%7D" class="module_item_url" style="display: none;">&nbsp;</a>
    <a href="/courses/167642/modules/%7B%7B%20id%20%7D%7D" class="module_url" style="display: none;">&nbsp;</a>
    <div class="all">
      <a href="/courses/167642/modules">see full course sequence</a>
    </div>
    <div class="clear"></div>
  </div>



          </div>
        </div>
      </div>
    </div>
    <footer role="contentinfo" id="footer">
      <a href="http://www.instructure.com" class="footer-logo">
        <span class="screenreader-only">
          Instructure, makers of the open source learning management system Canvas
        </span>
      </a>
      <span id="footer-links">
        <a href="http://help.instructure.com/" class="support_url help_dialog_trigger" data-track-category="help system" data-track-label="help button">Help</a>
        <a href="http://www.instructure.com/policies/privacy-policy-instructure">Privacy policy</a>
<a href="http://www.instructure.com/policies/terms-of-use">Terms of service</a>
<a href="http://facebook.com/instructure">Facebook</a>
<a href="http://twitter.com/instructure">Twitter</a>

      </span>
    </footer>
  </div>
</div>



  <div style="display:none;"><!-- Everything inside of this should always stay hidden -->
    <div id="ajax_authenticity_token">nYFEKc3is1A4UOvycqliyimnysSozia3VT7/cDheEq5Meq7TVtk2nClB9HLsh6cZ9gaScTc79aDSTGSjOp7iew==</div>
      <a href="/page_views/661aa740-df5e-0131-2d09-12b207192b96" id="page_view_update_path">&nbsp;</a>
      <div id="page_view_id">661aa740-df5e-0131-2d09-12b207192b96</div>
    <div id="domain_root_account_id">359</div>
  </div>
  <div id="cant_record_dialog" style="display: none;">
  <div>
        In order to create video or audio recordings your computer needs to be 
    webcam-enabled.  If you don&#x27;t have a webcam on your computer, you can still
    record audio-only messages by first installing the Google Video Chat
    plugin.

  </div>
  <div style="text-align: center; font-size: 1.5em; margin: 10px;">
    <a href="http://www.google.com/chat/video" target="_blank" class="btn">Install the Video Plugin</a>
  </div>
  <div class="links" style="text-align: right; font-size: 0.8em; display: none;">
    <a href="#" class="cant_record_link">Don&#x27;t have a webcam?</a>
  </div>
</div>
<div id='aria_alerts' class='hide-text affix' role="alert" aria-live="assertive"></div>
<script>
  INST = {"environment":"production","allowMediaComments":true,"kalturaSettings":{"domain":"www.instructuremedia.com","resource_domain":"www.instructuremedia.com","rtmp_domain":"rtmp.instructuremedia.com","partner_id":"101","subpartner_id":"10100","player_ui_conf":"1727899","kcw_ui_conf":"1727883","upload_ui_conf":"1103","max_file_size_bytes":534773760,"do_analytics":false,"use_alt_record_widget":true,"hide_rte_button":false,"js_uploader":true},"googleAnalyticsAccount":"UA-9138420-1","enableScribdHtml5":true,"logPageViews":true,"maxVisibleEditorButtons":3,"editorButtons":[]};
  ENV = {"current_user_id":"404463","current_user":{"id":"404463","display_name":"Bryan Kitzrow","avatar_image_url":"https://pltw.instructure.com/images/thumbnails/27259025/BNZzKzDOqkCG4jcvwbqexgKpbIuUTp6r5txTPYEH","html_url":"https://pltw.instructure.com/about/404463"},"current_user_roles":["user","student","teacher"],"AUTHENTICITY_TOKEN":"SnRGgbtBwiOhiYIz6MSf6rlNmp16vnBpXL1PxUhOvRqbj6x7IHpH77CYnbN26lo5ZuzCKOVLo37bz9QWSo5Nzw==","files_domain":"cluster20-files.instructure.com","badge_counts":{"submissions":0},"context_asset_string":"course_167642","TIMEZONE":"America/Chicago","CONTEXT_TIMEZONE":"America/New_York","LOCALE":"en-US"};

  // TODO: move this out when we have a single require call
  require = {
    translate: true,
    baseUrl: '/optimized',
    paths: {
    "common":"compiled/bundles/common",
    "jqueryui":"vendor/jqueryui",
    "uploadify":"../flash/uploadify/jquery.uploadify-3.1.min",
    "ic-dialog":"vendor/ic-dialog/dist/main.amd",
    "compiled/tinymce":"compiled/tinymce.js?v2",
    "migration_tool":"plugins/migration_tool",
    "instructure_misc_plugin":"plugins/instructure_misc_plugin",
    "analytics":"plugins/analytics",
    "multiple_root_accounts":"plugins/multiple_root_accounts",
    "canvasnet_registration":"plugins/canvasnet_registration",
    "demo_site":"plugins/demo_site",
    "compiled/registration/main_without_extensions":"compiled/registration/main",
    "compiled/registration/main":"compiled/registration/main_with_extensions",
    "compiled/registration/signupDialog_without_extensions":"compiled/registration/signupDialog",
    "compiled/registration/signupDialog":"compiled/registration/signupDialog_with_extensions",
    "compiled/bundles/modules/account_quota_settings_without_extensions":"compiled/bundles/modules/account_quota_settings",
    "compiled/bundles/modules/account_quota_settings":"compiled/bundles/modules/account_quota_settings_with_extensions"},
    packages : [{"name":"ic-ajax","location":"bower/ic-ajax"},{"name":"ic-styled","location":"bower/ic-styled"},{"name":"ic-menu","location":"bower/ic-menu"},{"name":"ic-tabs","location":"bower/ic-tabs/dist/amd"},{"name":"ember-qunit","location":"bower/ember-qunit/dist/amd"}],
    shim: {
    'bower/ember/ember': {
      deps: ['jquery', 'handlebars'],
      exports: 'Ember'
    },
    'bower/ember-data/ember-data': {
      deps: ['ember'],
      exports: 'DS'
    },
    'bower/handlebars/handlebars.runtime': {
      exports: 'Handlebars'
    },
    'vendor/FileAPI/FileAPI.min': {
      deps: ['jquery', 'vendor/FileAPI/config'],
      exports: 'FileAPI'
    },
    'uploadify': {
      deps: ['jquery'],
      exports: '$'
    },
    'vendor/bootstrap-select/bootstrap-select' : {
      deps: ['jquery'],
      exports: '$'
    },
    'vendor/jquery.jcrop': {
      deps: ['jquery'],
      exports: '$'
    },
    'handlebars': {
      deps: ['bower/handlebars/handlebars.runtime.amd'],
      exports: 'Handlebars'
    }
  }

  };
</script>

<script src="/optimized/vendor/require.js?1403712946" type="text/javascript"></script>
<script src="/optimized/compiled/bundles/common.js?1403712972" type="text/javascript"></script>
<script src="/optimized/compiled/bundles/module_sequence_footer.js?1403712961" type="text/javascript"></script>
<script src="/optimized/compiled/bundles/file_inline.js?1403712956" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[
          (function() {
            var inject = function(src) {
              var s = document.createElement('script');
              s.src = src;
              s.type = 'text/javascript';
              document.body.appendChild(s);
            };
            var srcs = ["https://my.pltw.org/sites/default/modules/pltw_lms/includes/pltw.js"];
            require(['jquery'], function() {
              for (var i = 0, l = srcs.length; i < l; i++) {
                inject(srcs[i]);
              }
            });
          })();

//]]>
</script>



<script>
// Determines if the scripts are loaded.
// When we get everything out of the views, and have a single top-level
// `require`, this becomes meaningless and will be abandoned.
(function() {
  var attempts = 0;
  var timeout = 10;
  var check = function() {
    attempts++;
    var done = !window.requirejs.s.contexts._.defQueue.length
    var giveup = attempts === 100; // 1 second
    if (done || giveup) {
      var className = document.documentElement.className;
      document.documentElement.className = className.replace(/scripts-not-loaded/, '');
      return;
    }
    setTimeout(check, timeout);
  };

  check();
}).call(this);
</script>
</body>
</html>

