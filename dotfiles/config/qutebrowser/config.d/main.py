# {{@@ env['dotdrop_warning'] @@}}
# flake8: noqa: E266
## Autogenerated config.py
## Documentation:
##   qute://help/configuring.html
##   qute://help/settings.html


STARTPAGE = 'file:///home/{{@@ env["USER"] @@}}/.config/qutebrowser/home.html'
# STARTPAGE = 'qute://help/img/cheatsheet-big.png'

c = c  # noqa
config = config  # noqa

## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
# config.load_autoconfig()

## Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## Type: Dict
# c.aliases = {'w': 'session-save', 'q': 'quit', 'wq': 'quit --save'}
c.aliases = {'q': 'quit',
             'youtube-dl': 'spawn youtube-dl -o "$HOME/Downloads/%(title)s-%(id)s.%(ext)s" {url}',
             'vlc': 'spawn --userscript ~/.config/qutebrowser/userscripts/videos_vlc.sh'}

## How often (in milliseconds) to auto-save config/cookies/etc.
## Type: Int
# c.auto_save.interval = 15000

## Always restore open sites when qutebrowser is reopened.
## Type: Bool
# c.auto_save.session = False
c.auto_save.session = True

## The backend to use to display websites. qutebrowser supports two
## different web rendering engines / backends, QtWebKit and QtWebEngine.
## QtWebKit was discontinued by the Qt project with Qt 5.6, but picked up
## as a well maintained fork: https://github.com/annulen/webkit/wiki -
## qutebrowser only supports the fork. QtWebEngine is Qt's official
## successor to QtWebKit. It's slightly more resource hungry that
## QtWebKit and has a couple of missing features in qutebrowser, but is
## generally the preferred choice. This setting requires a restart.
## Type: String
## Valid values:
##   - webengine: Use QtWebEngine (based on Chromium)
##   - webkit: Use QtWebKit (based on WebKit, similar to Safari)
# c.backend = 'webengine'

## How many commands to save in the command history. 0: no history / -1:
## unlimited
## Type: Int
# c.completion.cmd_history_max_items = 100

## Delay (in milliseconds) before updating completions after typing a
## character.
## Type: Int
# c.completion.delay = 0

## Height (in pixels or as percentage of the window) of the completion.
## Type: PercOrInt
# c.completion.height = '50%'

## Minimum amount of characters needed to update completions.
## Type: Int
# c.completion.min_chars = 1

## Move on to the next part when there's only one possible completion
## left.
## Type: Bool
# c.completion.quick = True

## When to show the autocompletion window.
## Type: String
## Valid values:
##   - always: Whenever a completion is available.
##   - auto: Whenever a completion is requested.
##   - never: Never.
# c.completion.show = 'always'

## How to format timestamps (e.g. for the history completion).
## Type: TimestampTemplate
# c.completion.timestamp_format = '%Y-%m-%d'

## Execute the best-matching command on a partial match.
## Type: Bool
# c.completion.use_best_match = False

## How many URLs to show in the web history. 0: no history / -1:
## unlimited
## Type: Int
# c.completion.web_history_max_items = -1

## Whether quitting the application requires a confirmation.
## Type: ConfirmQuit
## Valid values:
##   - always: Always show a confirmation.
##   - multiple-tabs: Show a confirmation if multiple tabs are opened.
##   - downloads: Show a confirmation if downloads are running
##   - never: Never show a confirmation.
# c.confirm_quit = ['never']
c.confirm_quit = ['downloads']

## Whether support for the HTML 5 web application cache feature is
## enabled. An application cache acts like an HTTP cache in some sense.
## For documents that use the application cache via JavaScript, the
## loader engine will first ask the application cache for the contents,
## before hitting the network.
## Type: Bool
# c.content.cache.appcache = True

## The maximum number of pages to hold in the global memory page cache.
## The Page Cache allows for a nicer user experience when navigating
## forth or back to pages in the forward/back history, by pausing and
## resuming up to _n_ pages. For more information about the feature,
## please refer to: http://webkit.org/blog/427/webkit-page-cache-i-the-
## basics/
## Type: Int
# c.content.cache.maximum_pages = 0

## Size of the HTTP network cache. Null to use the default value. With
## QtWebEngine, the maximum supported value is 2147483647 (~2 GB).
## Type: Int
# c.content.cache.size = None

## Control which cookies to accept.
## Type: String
## Valid values:
##   - all: Accept all cookies.
##   - no-3rdparty: Accept cookies from the same origin only.
##   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain.
##   - never: Don't accept cookies at all.
# c.content.cookies.accept = 'no-3rdparty'

## Store cookies. Note this option needs a restart with QtWebEngine on Qt
## < 5.9.
## Type: Bool
# c.content.cookies.store = True

# Default encoding to use for websites. The encoding must be a string
# describing an encoding such as _utf-8_, _iso-8859-1_, etc.
# Type: String
# c.content.default_encoding = 'iso-8859-1'
c.content.default_encoding = 'utf-8'

# Enable extra tools for Web developers. This needs to be enabled for
# `:inspector` to work and also adds an _Inspect_ entry to the context
# menu. For QtWebEngine, see `--enable-webengine-inspector` in
# `qutebrowser --help` instead.
# Type: Bool
# c.content.developer_extras = False

## Try to pre-fetch DNS entries to speed up browsing.
## Type: Bool
# c.content.dns_prefetch = True

## Expand each subframe to its contents. This will flatten all the frames
## to become one scrollable page.
## Type: Bool
# c.content.frame_flattening = False

## Allow websites to request geolocations.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.geolocation = 'ask'

## Value to send in the `Accept-Language` header.
## Type: String
# c.content.headers.accept_language = 'en-US,en'
c.content.headers.accept_language = 'en-US,en;q=0.5'

## Set custom headers for qutebrowser HTTP requests.
## Type: Dict
# c.content.headers.custom = {}

## Value to send in the `DNT` header. When this is set to true,
## qutebrowser asks websites to not track your identity. If set to null,
## the DNT header is not sent at all.
## Type: Bool
# c.content.headers.do_not_track = True

## Send the Referer header. The Referer header tells websites from which
## website you were coming from when visting them.
## Type: String
## Valid values:
##   - always: Always send the Referer.
##   - never: Never send the Referer. This is not recommended, as some sites may break.
##   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites.
# c.content.headers.referer = 'same-domain'

## User agent to send. Unset to send the default.
## Type: String
# c.content.headers.user_agent = None
c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

## Whether host blocking is enabled.
## Type: Bool
# c.content.host_blocking.enabled = True

## Enable or disable hyperlink auditing (`<a ping>`).
## Type: Bool
# c.content.hyperlink_auditing = False

## Whether images are automatically loaded in web pages.
## Type: Bool
# c.content.images = True

## Show javascript alerts.
## Type: Bool
# c.content.javascript.alert = True

## Whether JavaScript can read from or write to the clipboard. With
## QtWebEngine, writing the clipboard as response to a user interaction
## is always allowed.
## Type: Bool
# c.content.javascript.can_access_clipboard = False

## Whether JavaScript can close tabs.
## Type: Bool
# c.content.javascript.can_close_tabs = False

## Whether JavaScript can open new tabs without user interaction.
## Type: Bool
# c.content.javascript.can_open_tabs_automatically = False

## Enables or disables JavaScript.
## Type: Bool
# c.content.javascript.enabled = True

## Log levels to use for JavaScript console logging messages. When a
## JavaScript message with the level given in the dictionary key is
## logged, the corresponding dictionary value selects the qutebrowser
## logger to use. On QtWebKit, the "unknown" setting is always used.
## Type: Dict
# c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}

## Use the standard JavaScript modal dialog for `alert()` and `confirm()`
## Type: Bool
# c.content.javascript.modal_dialog = False

## Show javascript prompts.
## Type: Bool
# c.content.javascript.prompt = True

## Whether locally loaded documents are allowed to access other local
## urls.
## Type: Bool
# c.content.local_content_can_access_file_urls = True

## Whether locally loaded documents are allowed to access remote urls.
## Type: Bool
# c.content.local_content_can_access_remote_urls = False

## Whether support for HTML 5 local storage and Web SQL is enabled.
## Type: Bool
# c.content.local_storage = True

## Allow websites to record audio/video.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.media_capture = 'ask'

## Location of a netrc-file for HTTP authentication. If unset, `~/.netrc`
## is used.
## Type: File
# c.content.netrc_file = None

## Allow websites to show notifications.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.notifications = 'ask'

## Enable pdf.js to view PDF files in the browser. Note that the files
## can still be downloaded by clicking the download button in the pdf.js
## viewer.
## Type: Bool
# c.content.pdfjs = False

## Enables or disables plugins in Web pages.
## Type: Bool
# c.content.plugins = False
c.content.plugins = True

## Whether the background color and images are also drawn when the page
## is printed.
## Type: Bool
# c.content.print_element_backgrounds = True

## Open new windows in private browsing mode which does not record
## visited pages.
## Type: Bool
# c.content.private_browsing = False

## The proxy to use. In addition to the listed values, you can use a
## `socks://...` or `http://...` URL.
## Type: Proxy
## Valid values:
##   - system: Use the system wide proxy.
##   - none: Don't use any proxy
# c.content.proxy = 'system'

## Send DNS requests over the configured proxy.
## Type: Bool
# c.content.proxy_dns_requests = True

## Validate SSL handshakes.
## Type: BoolAsk
## Valid values:
##   - true
##   - false
##   - ask
# c.content.ssl_strict = 'ask'

## A list of user stylesheet filenames to use.
## Type: List of File, or File
# c.content.user_stylesheets = []

## Enables or disables WebGL.
## Type: Bool
# c.content.webgl = True

## Limit fullscreen to the browser window (does not expand to fill the
## screen).
## Type: Bool
# c.content.windowed_fullscreen = False

## Whether load requests should be monitored for cross-site scripting
## attempts. Suspicious scripts will be blocked and reported in the
## inspector's JavaScript console. Enabling this feature might have an
## impact on performance.
## Type: Bool
# c.content.xss_auditing = False

## The directory to save downloads to. If unset, a sensible os-specific
## default is used.
## Type: Directory
# c.downloads.location.directory = None

## Prompt the user for the download location. If set to false,
## `downloads.location.directory` will be used.
## Type: Bool
# c.downloads.location.prompt = True

## Remember the last used download directory.
## Type: Bool
# c.downloads.location.remember = True

## What to display in the download filename input.
## Type: String
## Valid values:
##   - path: Show only the download path.
##   - filename: Show only download filename.
##   - both: Show download path and filename.
# c.downloads.location.suggestion = 'path'

## The default program used to open downloads. If null, the default
## internal handler is used. Any `{}` in the string will be expanded to
## the filename, else the filename will be appended.
## Type: String
# c.downloads.open_dispatcher = None

## Where to show the downloaded files.
## Type: VerticalPosition
## Valid values:
##   - top
##   - bottom
# c.downloads.position = 'top'

## Number of milliseconds to wait before removing finished downloads. If
## set to -1, downloads are never removed.
## Type: Int
# c.downloads.remove_finished = -1

## The editor (and arguments) to use for the `open-editor` command. `{}`
## gets replaced by the filename of the file to be edited.
## Type: ShellCommand
# c.editor.command = ['gvim', '-f', '{file}', '-c', 'normal {line}G{column0}l']
c.editor.command = ['subl', '-a', '{}']

## Encoding to use for the editor.
## Type: Encoding
# c.editor.encoding = 'utf-8'

## The maximum time in minutes between two history items for them to be
## considered being from the same browsing session. Items with less time
## between them are grouped when being displayed in `:history`. Use -1 to
## disable separation.
## Type: Int
# c.history_gap_interval = 30

## Find text on a page case-insensitively.
## Type: String
## Valid values:
##   - always: Search case-insensitively
##   - never: Search case-sensitively
##   - smart: Search case-sensitively if there are capital chars
# c.search.ignore_case = 'smart'

## Forward unbound keys to the webview in normal mode.
## Type: String
## Valid values:
##   - all: Forward all unbound keys.
##   - auto: Forward unbound non-alphanumeric keys.
##   - none: Don't forward any keys.
# c.input.forward_unbound_keys = 'auto'

## Leave insert mode if a non-editable element is clicked.
## Type: Bool
# c.input.insert_mode.auto_leave = True

## Automatically enter insert mode if an editable element is focused
## after loading the page.
## Type: Bool
# c.input.insert_mode.auto_load = False

## Switch to insert mode when clicking flash and other plugins.
## Type: Bool
# c.input.insert_mode.plugins = False

## Include hyperlinks in the keyboard focus chain when tabbing.
## Type: Bool
# c.input.links_included_in_focus_chain = True

## Timeout (in milliseconds) for partially typed key bindings. If the
## current input forms only partial matches, the keystring will be
## cleared after this time.
## Type: Int
# c.input.partial_timeout = 5000

## Enable Opera-like mouse rocker gestures. This disables the context
## menu.
## Type: Bool
# c.input.rocker_gestures = False

## Enable Spatial Navigation. Spatial navigation consists in the ability
## to navigate between focusable elements in a Web page, such as
## hyperlinks and form controls, by using Left, Right, Up and Down arrow
## keys. For example, if a user presses the Right key, heuristics
## determine whether there is an element he might be trying to reach
## towards the right and which element he probably wants.
## Type: Bool
# c.input.spatial_navigation = False

## Keychains that shouldn't be shown in the keyhint dialog. Globs are
## supported, so `;*` will blacklist all keychains starting with `;`. Use
## `*` to disable keyhints.
## Type: List of String
# c.keyhint.blacklist = []

## Time from pressing a key to seeing the keyhint dialog (ms).
## Type: Int
# c.keyhint.delay = 500

# Time (in ms) to show messages in the statusbar for. Set to 0 to never
# clear messages.
# Type: Int
# c.messages.timeout = 2000
c.messages.timeout = 5000

## How to open links in an existing instance if a new one is launched.
## This happens when e.g. opening a link from a terminal. See
## `new_instance_open_target_window` to customize in which window the
## link is opened in.
## Type: String
## Valid values:
##   - tab: Open a new tab in the existing window and activate the window.
##   - tab-bg: Open a new background tab in the existing window and activate the window.
##   - tab-silent: Open a new tab in the existing window without activating the window.
##   - tab-bg-silent: Open a new background tab in the existing window without activating the window.
##   - window: Open in a new window.
# c.new_instance_open_target = 'tab'

## Which window to choose when opening links as new tabs. When
## `new_instance_open_target` is not set to `window`, this is ignored.
## Type: String
## Valid values:
##   - first-opened: Open new tabs in the first (oldest) opened window.
##   - last-opened: Open new tabs in the last (newest) opened window.
##   - last-focused: Open new tabs in the most recently focused window.
##   - last-visible: Open new tabs in the most recently visible window.
# c.new_instance_open_target_window = 'last-focused'

## Show a filebrowser in upload/download prompts.
## Type: Bool
# c.prompt.filebrowser = True

## Additional arguments to pass to Qt, without leading `--`. With
## QtWebEngine, some Chromium arguments (see
## https://peter.sh/experiments/chromium-command-line-switches/ for a
## list) will work. This setting requires a restart.
## Type: List of String
# c.qt.args = []

## Force a Qt platform to use. This sets the `QT_QPA_PLATFORM`
## environment variable and is useful to force using the XCB plugin when
## running QtWebEngine on Wayland.
## Type: String
# c.qt.force_platform = None

## Force software rendering for QtWebEngine. This is needed for
## QtWebEngine to work with Nouveau drivers. This setting requires a
## restart.
## Type: Bool
# c.qt.force_software_rendering = False

## Turn on Qt HighDPI scaling. This is equivalent to setting
## QT_AUTO_SCREEN_SCALE_FACTOR=1 in the environment. It's off by default
## as it can cause issues with some bitmap fonts. As an alternative to
## this, it's possible to set font sizes and the `zoom.default` setting.
## Type: Bool
# c.qt.highdpi = False

## Enable smooth scrolling for web pages. Note smooth scrolling does not
## work with the `:scroll-px` command.
## Type: Bool
# c.scrolling.smooth = False

## When to find text on a page case-insensitively.
## Type: String
## Valid values:
##   - always: Search case-insensitively.
##   - never: Search case-sensitively.
##   - smart: Search case-sensitively if there are capital characters.
# c.search.ignore_case = 'smart'

## Find text on a page incrementally, renewing the search for each typed
## character.
## Type: Bool
# c.search.incremental = True

## The name of the session to save by default. If this is set to null,
## the session which was last loaded is saved.
## Type: SessionName
# c.session.default_name = None

## Load a restored tab as soon as it takes focus.
## Type: Bool
# c.session.lazy_restore = False
c.session.lazy_restore = True

## Spell checking languages. You can check for available languages and
## install dictionaries using scripts/install_dict.py. Run the script
## with -h/--help for instructions.
## Type: List of String
## Valid values:
##   - af-ZA: Afrikaans (South Africa)
##   - bg-BG: Bulgarian (Bulgaria)
##   - ca-ES: Catalan (Spain)
##   - cs-CZ: Czech (Czech Republic)
##   - da-DK: Danish (Denmark)
##   - de-DE: German (Germany)
##   - el-GR: Greek (Greece)
##   - en-CA: English (Canada)
##   - en-GB: English (United Kingdom)
##   - en-US: English (United States)
##   - es-ES: Spanish (Spain)
##   - et-EE: Estonian (Estonia)
##   - fa-IR: Farsi (Iran)
##   - fo-FO: Faroese (Faroe Islands)
##   - fr-FR: French (France)
##   - he-IL: Hebrew (Israel)
##   - hi-IN: Hindi (India)
##   - hr-HR: Croatian (Croatia)
##   - hu-HU: Hungarian (Hungary)
##   - id-ID: Indonesian (Indonesia)
##   - it-IT: Italian (Italy)
##   - ko: Korean
##   - lt-LT: Lithuanian (Lithuania)
##   - lv-LV: Latvian (Latvia)
##   - nb-NO: Norwegian (Norway)
##   - nl-NL: Dutch (Netherlands)
##   - pl-PL: Polish (Poland)
##   - pt-BR: Portuguese (Brazil)
##   - pt-PT: Portuguese (Portugal)
##   - ro-RO: Romanian (Romania)
##   - ru-RU: Russian (Russia)
##   - sh: Serbo-Croatian
##   - sk-SK: Slovak (Slovakia)
##   - sl-SI: Slovenian (Slovenia)
##   - sq: Albanian
##   - sr: Serbian
##   - sv-SE: Swedish (Sweden)
##   - ta-IN: Tamil (India)
##   - tg-TG: Tajik (Tajikistan)
##   - tr-TR: Turkish (Turkey)
##   - uk-UA: Ukrainian (Ukraine)
##   - vi-VN: Vietnamese (Viet Nam)
# c.spellcheck.languages = []

## Open new tabs (middleclick/ctrl+click) in the background.
## Type: Bool
# c.tabs.background = False
c.tabs.background = True

## On which mouse button to close tabs.
## Type: String
## Valid values:
##   - right: Close tabs on right-click.
##   - middle: Close tabs on middle-click.
##   - none: Don't close tabs using the mouse.
# c.tabs.close_mouse_button = 'middle'

## How to behave when the close mouse button is pressed on the tab bar.
## Type: String
## Valid values:
##   - new-tab: Open a new tab.
##   - close-current: Close the current tab.
##   - close-last: Close the last tab.
##   - ignore: Don't do anything.
# c.tabs.close_mouse_button_on_bar = 'new-tab'

## Behavior when the last tab is closed.
## Type: String
## Valid values:
##   - ignore: Don't do anything.
##   - blank: Load a blank page.
##   - startpage: Load the start page.
##   - default-page: Load the default page.
##   - close: Close the window.
# c.tabs.last_close = 'ignore'
c.tabs.last_close = 'startpage'

## Switch between tabs using the mouse wheel.
## Type: Bool
# c.tabs.mousewheel_switching = True

## How new tabs opened from another tab are positioned.
## Type: NewTabPosition
## Valid values:
##   - prev: Before the current tab.
##   - next: After the current tab.
##   - first: At the beginning.
##   - last: At the end.
# c.tabs.new_position.related = 'next'

## How new tabs which aren't opened from another tab are positioned.
## Type: NewTabPosition
## Valid values:
##   - prev: Before the current tab.
##   - next: After the current tab.
##   - first: At the beginning.
##   - last: At the end.
# c.tabs.new_position.unrelated = 'last'

## When switching tabs, what input mode is applied.
## Type: String
## Valid values:
##   - persist: Retain the current mode.
##   - restore: Restore previously saved mode.
##   - normal: Always revert to normal mode.
# c.tabs.mode_on_change = normal

## Shrink pinned tabs down to their contents.
## Type: Bool
# c.tabs.pinned.shrink = True

## Which tab to select when the focused tab is removed.
## Type: SelectOnRemove
## Valid values:
##   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
##   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
##   - last-used: Select the previously selected tab.
# c.tabs.select_on_remove = 'next'

## Open a new window for every tab.
## Type: Bool
# c.tabs.tabs_are_windows = False

## Whether to wrap when changing tabs.
## Type: Bool
# c.tabs.wrap = True

## Whether to start a search when something else than a URL is entered.
## Type: String
## Valid values:
##   - naive: Use simple/naive check.
##   - dns: Use DNS requests (might be slow!).
##   - never: Never search automatically.
# c.url.auto_search = 'naive'

## The page to open if :open -t/-b/-w is used without URL. Use
## `about:blank` for a blank page.
## Type: FuzzyUrl
# c.url.default_page = 'https://start.duckduckgo.com/'
c.url.default_page = STARTPAGE

## The URL segments where `:navigate increment/decrement` will search for
## a number.
## Type: FlagList
## Valid values:
##   - host
##   - path
##   - query
##   - anchor
# c.url.incdec_segments = ['path', 'query']

## The page(s) to open at the start.
## Type: List of FuzzyUrl, or FuzzyUrl
# c.url.start_pages = ['https://start.duckduckgo.com']
c.url.start_pages = [STARTPAGE]

## The URL parameters to strip with `:yank url`.
## Type: List of String
# c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']

## The default zoom level.
## Type: Perc
# c.zoom.default = '100%'

## The available zoom levels.
## Type: List of Perc
# c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']

## How much to divide the mouse wheel movements to translate them into
## zoom increments.
## Type: Int
# c.zoom.mouse_divider = 512

## Whether the zoom factor on a frame applies only to the text or to all
## content.
## Type: Bool
# c.zoom.text_only = False
