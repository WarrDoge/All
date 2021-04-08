import telebot
from telebot import types
import requests
import os
import moviepy 
from moviepy.editor import VideoFileClip, vfx
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
import moviepy.editor as mp
from moviepy.editor import ImageClip
###################################################################
bot = telebot.TeleBot(TOKEN)
###################################################################
@bot.message_handler(commands=['start', 'help'])
def command_help(message):
	bot.reply_to(message, """
Отправь фото, чтобы поменять картинку для превью.
Поменял фото - кидай видео.
""")
###################################################################
@bot.message_handler(content_types=['document'])
def photo(message):
	file_info = bot.get_file(message.document.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	document = bytes(downloaded_file)
	bot.reply_to(message, "Поменял картинку!")
	with open('image.jpg', 'wb') as img:
		img.write(document)
#####################################################################
@bot.message_handler(content_types=['video'])
def video(message):
	bot.reply_to(message, "Uno momento, senor!")
	file_info = bot.get_file(message.video.file_id)
	downloaded_file = bot.download_file(file_info.file_path)
	video = bytes(downloaded_file)
	with open('video.mp4', 'wb') as vid:
	 	vid.write(video)
	video = mp.VideoFileClip('video.mp4') 	
	vid_len = video.duration
	logo = (mp.ImageClip("image.jpg")
          .set_duration(video.duration)
          .resize(video.size)
          .set_pos(("center")))
	bot.reply_to(message, "Последние штрихи...")
	final = mp.CompositeVideoClip([video.set_start(2).fx(transfx.fadein, 0.5), logo.set_start(0).set_duration(1.5).fx(transfx.fadeout, 0.5)])
	final.subclip(0,vid_len-5.5).write_videofile("test.mp4")
	bot.send_video(message.chat.id, open('test.mp4', 'rb'))
#####################################################################
bot.polling()