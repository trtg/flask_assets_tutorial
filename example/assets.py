from flask_assets import Bundle

common_css = Bundle(
        'vendor/bootstrap/css/bootstrap.css',
        Bundle(
            'css/layout.less',
            filters='less'
            ),
        filters='cssmin',output='public/css/common.css')

common_js = Bundle(
        'vendor/jquery/jquery-1.8.3.min.js',
        'vendor/bootstrap/js/bootstrap.min.js',
        Bundle(
            'js/main.js',
            filters='closure_js'
            ),
        output='public/js/common.js')
