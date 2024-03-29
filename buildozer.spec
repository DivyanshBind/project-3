[app]

title = Divyansh
package.name = Divyanshapp
package.domain = org.divyansh

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python==3.11.2,kivy==2.2.1,pillow

orientation = portrait
fullscreen = 0
android.arch = armeabi-v7a

# iOS specific
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.7.0

[buildozer]
log_level = 2