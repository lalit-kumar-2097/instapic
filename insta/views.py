import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import requests
from django.conf import settings


#insta_loader imports:
import instaloader
import pandas as pd
from datetime import datetime
import hashlib
import os
import csv
import wget

from django.utils.html import format_html, mark_safe

def convert_string_to_html_element(html_string):
    return mark_safe(format_html(html_string))



if not settings.configured:
    settings.configure()


def get_MD5(str):
    with open(str, 'rb') as f:
        data = f.read()
        md5hash = hashlib.md5(data).hexdigest()
    new_name = F'{md5hash}.jpg'
    print(new_name)
    return(new_name)


def display_images(request):
    if request.method == 'POST':
        # get image URLs from the POST request
        image_urls = request.POST.get('image_urls').split(',')
        print(image_urls)
        # fetch the images from the URLs
        images = []
        for url in image_urls:
            response = requests.get(url)
            image = response.content
            images.append(image)                    
        # images = b'images'
        # return the images as a JSON response
        return JsonResponse({'images': b'images'.decode('utf-8')}, safe=False)

    # render the initial template
    return render(request, 'index.html')


L = instaloader.Instaloader(download_videos=False)
SINCE = datetime(1990, 5, 10)
df = pd.DataFrame(columns=["post_id","type","MD5","URL"])
print(df)


# def instapic(request):
#     if request.method == 'POST':
#         post_ids = request.POST.get('instapic')
#         post_ids = post_ids.split(',')        
#         post_ids_response = f'<html> <p>{post_ids}<html> <p>'
#         links = []
#         post_id_render = []
#         for post_id in post_ids:
#             post = instaloader.Post.from_shortcode(L.context, shortcode= post_id)
#             if post.typename == 'GraphImage':
#                 links.append(post.url)
#                 wget.download(post.url, out = 'resources/temp.jpg')
#                 new_name = 'resources/'+get_MD5('resources/temp.jpg')
#                 print(post_id)
#                 os.rename('resources/temp.jpg',new_name)
#                 post_id_render.append(post_id)
#         print(links)
#         context = {"links": zip(links,post_id_render)}
#         return render(request, 'insta_download.html', context) 
#         #     if post.typename == 'GraphImage':        
#         #         L.download_pic(url = post.url, filename = f"{post_id}", mtime= SINCE)                
#         # return HttpResponse(post_ids_response)

#     else:
#         return render(request, "instapic.html")


    # if post.typename == 'GraphImage':        
    #             L.download_pic(url = post.url, filename = f"{post_id}", mtime= SINCE)



# def instapic(request):
#     if request.method == 'POST':
#         post_ids = request.POST.get('instapic')
#         post_ids = post_ids.split(',')
#         list_dict = []
#         for post_id in post_ids:
#             post = instaloader.Post.from_shortcode(L.context, shortcode= post_id)
#             if post.typename == 'GraphImage':
#                 wget.download(post.url, out = 'resources/insta/resources/temp.jpg')
#                 MD5 = get_MD5('resources/insta/resources/temp.jpg').replace('.jpg','')
#                 new_name = 'resources/insta/resources/'+get_MD5('resources/insta/resources/temp.jpg')
#                 os.rename('resources/insta/resources/temp.jpg',new_name)
#                 #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
#                 temp_dict = {'post_id': post_id,
#                              "Type": "Image",
#                              "MD5": MD5,
#                              "URL": post.url,
#                              'File': new_name
#                              }
#                 list_dict.append(temp_dict)
#         print(list_dict)
#         data = {'data': list_dict}
#         # return render(request, 'my_json_page.html',{'data': json_data})
#         # return JsonResponse(data,safe=True)
#         return render(request, 'my_json_page.html',data)
#     else:
#         return render(request, "instapic.html")             
    




# def instapic(request):
#     if request.method == 'POST':
#         post_ids = request.POST.get('instapic')
#         post_ids = post_ids.split(',')
#         list_dict = []
#         for post_id in post_ids:
#             post = instaloader.Post.from_shortcode(L.context, shortcode= post_id)
#             if post.typename == 'GraphImage':
#                 wget.download(post.url, out = 'resources/insta/resources/temp.jpg')
#                 MD5 = get_MD5('resources/insta/resources/temp.jpg').replace('.jpg','')
#                 new_name = 'resources/insta/resources/'+get_MD5('resources/insta/resources/temp.jpg')
#                 os.rename('resources/insta/resources/temp.jpg',new_name)
#                 element = '<img src="'+new_name+'" alt = ""></img>'
#                 element = convert_string_to_html_element(element)
#                 #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
#                 temp_dict = {'post_id': post_id,
#                              "DATA": {
#                                 "post_id": post_id,
#                                 "Type": "Image",
#                                 "MD5": MD5,
#                                 "URL": post.url,
#                                 'File': new_name,
#                                 'Element': element
#                              }
#                 }
#                 list_dict.append(temp_dict)

#             if post.typename == 'GraphSidecar':
#                 for node in post.get_sidecar_nodes():
#                     if node.is_video == True:
#                         print("It's a video")
#                         wget.download(node.video_url, out = 'resources/insta/resources/temp.mp4')
#                         MD5 = get_MD5('resources/insta/resources/temp.mp4').replace('.jpg','')
#                         new_name = 'resources/insta/resources/'+MD5+".mp4"
#                         os.rename('resources/insta/resources/temp.mp4',new_name)
#                         element = '<video src="'+new_name+'" controls></video>'
#                         element = convert_string_to_html_element(element)
#                         #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
#                         temp_dict = {'post_id': post_id,
#                                     "DATA": {
#                                         "post_id": post_id,
#                                         "Type": "Video",
#                                         "MD5": MD5,
#                                         "URL": post.url,
#                                         'File': new_name,
#                                         'Element': element
#                                     }
#                         }
#                         list_dict.append(temp_dict)
#                     else:
#                         print("It's a pic")
#                         wget.download(node.display_url, out = 'resources/insta/resources/temp.jpg')
#                         MD5 = get_MD5('resources/insta/resources/temp.jpg').replace('.jpg','')
#                         new_name = 'resources/insta/resources/'+get_MD5('resources/insta/resources/temp.jpg')
#                         os.rename('resources/insta/resources/temp.jpg',new_name)
#                         element = '<img src="'+new_name+'" alt = ""></img>'
#                         element = convert_string_to_html_element(element)
#                         #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
#                         temp_dict = {'post_id': post_id,
#                                     "DATA": {
#                                         "post_id": post_id,
#                                         "Type": "Image",
#                                         "MD5": MD5,
#                                         "URL": post.url,
#                                         'File': new_name,
#                                         'Element': element
#                                     }
#                         }
#                         list_dict.append(temp_dict)



#             if post.is_video == True:
#                 wget.download(post.video_url, out = 'resources/insta/resources/temp.mp4')
#                 MD5 = get_MD5('resources/insta/resources/temp.mp4').replace('.jpg','')
#                 new_name = 'resources/insta/resources/'+MD5+".mp4"
#                 os.rename('resources/insta/resources/temp.mp4',new_name)
#                 element = '<video src="'+new_name+'" controls></video>'
#                 element = convert_string_to_html_element(element)
#                 #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
#                 temp_dict = {'post_id': post_id,
#                              "DATA": {
#                                 "post_id": post_id,
#                                 "Type": "Video",
#                                 "MD5": MD5,
#                                 "URL": post.url,
#                                 'File': new_name,
#                                 'Element': element
#                              }
#                 }
#                 list_dict.append(temp_dict)

#         print(list_dict)
#         data = {'data': list_dict}
#         # return render(request, 'my_json_page.html',{'data': json_data})
#         # return JsonResponse(data,safe=True)
#         return render(request, 'my_json_page.html',data)
#     else:
#         return render(request, "instapic.html")     




# 126 - 224

# def instapic(request):
#     if request.method == 'POST':

#         post_data = [{'post_id': 'CqRIOcoImOn', 'DATA': {'post_id': 'CqRIOcoImOn', 'Type': 'Image', 'MD5': '19e37f925e97ca0d358cd3e9d172b001', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/337587305_733010468425066_2858168715770964536_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=NDQtcbytpQ4AX8LNYW1&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfA34x4VKJRruS49MF0iSpPfHuO-bopBKKuRDMCJ-KqBMg&oe=64286B19&_nc_sid=4f375e', 'File': 'resources/insta/resources/19e37f925e97ca0d358cd3e9d172b001.jpg', 'Element': '<img src="resources/insta/resources/19e37f925e97ca0d358cd3e9d172b001.jpg" alt = ""></img>'}}, {'post_id': 'CqRIOcoImOn', 'DATA': {'post_id': 'CqRIOcoImOn', 'Type': 'Image', 'MD5': 'b1e3686bb0da3fd3b5909af6b1596fa9', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/337587305_733010468425066_2858168715770964536_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=NDQtcbytpQ4AX8LNYW1&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfA34x4VKJRruS49MF0iSpPfHuO-bopBKKuRDMCJ-KqBMg&oe=64286B19&_nc_sid=4f375e', 'File': 'resources/insta/resources/b1e3686bb0da3fd3b5909af6b1596fa9.jpg', 'Element': '<img src="resources/insta/resources/b1e3686bb0da3fd3b5909af6b1596fa9.jpg" alt = ""></img>'}}, {'post_id': 'CqRIOcoImOn', 'DATA': {'post_id': 'CqRIOcoImOn', 'Type': 'Image', 'MD5': '399ae64b945f26028ce1c7bd0e4ac982', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/337587305_733010468425066_2858168715770964536_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=NDQtcbytpQ4AX8LNYW1&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfA34x4VKJRruS49MF0iSpPfHuO-bopBKKuRDMCJ-KqBMg&oe=64286B19&_nc_sid=4f375e', 'File': 'resources/insta/resources/399ae64b945f26028ce1c7bd0e4ac982.jpg', 'Element': '<img src="resources/insta/resources/399ae64b945f26028ce1c7bd0e4ac982.jpg" alt = ""></img>'}}, {'post_id': 'CqRIOcoImOn', 'DATA': {'post_id': 'CqRIOcoImOn', 'Type': 'Image', 'MD5': '5a3ccd081f33814a40d81d0ada1f469e', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/337587305_733010468425066_2858168715770964536_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=NDQtcbytpQ4AX8LNYW1&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfA34x4VKJRruS49MF0iSpPfHuO-bopBKKuRDMCJ-KqBMg&oe=64286B19&_nc_sid=4f375e', 'File': 'resources/insta/resources/5a3ccd081f33814a40d81d0ada1f469e.jpg', 'Element': '<img src="resources/insta/resources/5a3ccd081f33814a40d81d0ada1f469e.jpg" alt = ""></img>'}}, {'post_id': 'CqRIOcoImOn', 'DATA': {'post_id': 'CqRIOcoImOn', 'Type': 'Image', 'MD5': '2eb5ec48a39c25029926e2564316a0c9', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/337587305_733010468425066_2858168715770964536_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=NDQtcbytpQ4AX8LNYW1&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfA34x4VKJRruS49MF0iSpPfHuO-bopBKKuRDMCJ-KqBMg&oe=64286B19&_nc_sid=4f375e', 'File': 'resources/insta/resources/2eb5ec48a39c25029926e2564316a0c9.jpg', 'Element': '<img src="resources/insta/resources/2eb5ec48a39c25029926e2564316a0c9.jpg" alt = ""></img>'}}, {'post_id': 'CpdAlMVDtPN', 'DATA': {'post_id': 'CpdAlMVDtPN', 'Type': 'Video', 'MD5': '230ef6b7321b5ed6f5bc32ddf83ffc15', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/333882241_975686290483005_6679486576832057790_n.jpg?stp=dst-jpg_e15&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=VDnznV2syZ8AX-HFHvN&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfB5NLPt01Q4hgp2eWk9VkVg4ElW9Dp_8qR2q5yKs5CtyA&oe=6423D7AB&_nc_sid=4f375e', 'File': 'resources/insta/resources/230ef6b7321b5ed6f5bc32ddf83ffc15.mp4', 'Element': '<video src="resources/insta/resources/230ef6b7321b5ed6f5bc32ddf83ffc15.mp4" controls></video>'}}, {'post_id': 'CqJisLSo-JK', 'DATA': {'post_id': 'CqJisLSo-JK', 'Type': 'Image', 'MD5': '184fe0d0582883b7a5de5af16bfb4626', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/326885738_191616303600341_8024498034522822109_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=PsN76ptvDCwAX_AK-WT&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfCKaDijJJpGHZ00Bf6LtoNEoaufWAmOFoNJUSUdhpgASA&oe=64281408&_nc_sid=4f375e', 'File': 'resources/insta/resources/184fe0d0582883b7a5de5af16bfb4626.jpg', 'Element': '<img src="resources/insta/resources/184fe0d0582883b7a5de5af16bfb4626.jpg" alt = ""></img>'}}, {'post_id': 'CqJisLSo-JK', 'DATA': {'post_id': 'CqJisLSo-JK', 'Type': 'Image', 'MD5': 'df3c3e33e59a12fb31e3a995a09baf22', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/326885738_191616303600341_8024498034522822109_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=PsN76ptvDCwAX_AK-WT&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfCKaDijJJpGHZ00Bf6LtoNEoaufWAmOFoNJUSUdhpgASA&oe=64281408&_nc_sid=4f375e', 'File': 'resources/insta/resources/df3c3e33e59a12fb31e3a995a09baf22.jpg', 'Element': '<img src="resources/insta/resources/df3c3e33e59a12fb31e3a995a09baf22.jpg" alt = ""></img>'}}, {'post_id': 'CqJisLSo-JK', 'DATA': {'post_id': 'CqJisLSo-JK', 'Type': 'Image', 'MD5': '3d1ce879cf3636d65b89cb5eadb5667f', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/326885738_191616303600341_8024498034522822109_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=PsN76ptvDCwAX_AK-WT&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfCKaDijJJpGHZ00Bf6LtoNEoaufWAmOFoNJUSUdhpgASA&oe=64281408&_nc_sid=4f375e', 'File': 'resources/insta/resources/3d1ce879cf3636d65b89cb5eadb5667f.jpg', 'Element': '<img src="resources/insta/resources/3d1ce879cf3636d65b89cb5eadb5667f.jpg" alt = ""></img>'}}, {'post_id': 'CqJisLSo-JK', 'DATA': {'post_id': 'CqJisLSo-JK', 'Type': 'Image', 'MD5': '4846ec79aa8c7c11ad7931654bdb4ed3', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/326885738_191616303600341_8024498034522822109_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=PsN76ptvDCwAX_AK-WT&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfCKaDijJJpGHZ00Bf6LtoNEoaufWAmOFoNJUSUdhpgASA&oe=64281408&_nc_sid=4f375e', 'File': 'resources/insta/resources/4846ec79aa8c7c11ad7931654bdb4ed3.jpg', 'Element': '<img src="resources/insta/resources/4846ec79aa8c7c11ad7931654bdb4ed3.jpg" alt = ""></img>'}}, {'post_id': 'CqJisLSo-JK', 'DATA': {'post_id': 'CqJisLSo-JK', 'Type': 'Image', 'MD5': 'f87ab331f141caf4fdce60c1d792d02d', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/326885738_191616303600341_8024498034522822109_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=PsN76ptvDCwAX_AK-WT&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfCKaDijJJpGHZ00Bf6LtoNEoaufWAmOFoNJUSUdhpgASA&oe=64281408&_nc_sid=4f375e', 'File': 'resources/insta/resources/f87ab331f141caf4fdce60c1d792d02d.jpg', 'Element': '<img src="resources/insta/resources/f87ab331f141caf4fdce60c1d792d02d.jpg" alt = ""></img>'}}]
#         post_data = [{'post_id': 'CqRIOcoImOn', 'DATA': [
#             {
#                 'post_id': 'CqRIOcoImOn', 'Type': 'Image', 'MD5': '19e37f925e97ca0d358cd3e9d172b001', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/337587305_733010468425066_2858168715770964536_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=NDQtcbytpQ4AX8LNYW1&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfA34x4VKJRruS49MF0iSpPfHuO-bopBKKuRDMCJ-KqBMg&oe=64286B19&_nc_sid=4f375e', 'File': 'resources/insta/resources/19e37f925e97ca0d358cd3e9d172b001.jpg', 'Element': '<img src="resources/insta/resources/19e37f925e97ca0d358cd3e9d172b001.jpg" alt = ""></img>'
#             },
#             {
#                 'post_id': 'CqRIOcoImOn', 'Type': 'Image', 'MD5': '19e37f925e97ca0d358cd3e9d172b001_2', 'URL': 'https://scontent-bom1-1.cdninstagram.com/v/t51.2885-15/337587305_733010468425066_2858168715770964536_n.jpg?stp=dst-jpg_e35_s1080x1080&_nc_ht=scontent-bom1-1.cdninstagram.com&_nc_cat=1&_nc_ohc=NDQtcbytpQ4AX8LNYW1&edm=AP_V10EBAAAA&ccb=7-5&oh=00_AfA34x4VKJRruS49MF0iSpPfHuO-bopBKKuRDMCJ-KqBMg&oe=64286B19&_nc_sid=4f375e', 'File': 'resources/insta/resources/19e37f925e97ca0d358cd3e9d172b001_2.jpg', 'Element': '<img src="resources/insta/resources/19e37f925e97ca0d358cd3e9d172b001_2.jpg" alt = ""></img>'
#             }
#         ]},
#          {
#             'post_id': 'CpdAlMVDtPN', 'DATA': [
#             {
#                 'post_id': 'CpdAlMVDtPN', 'Type': 'Image', 'MD5': "230ef6b7321b5ed6f5bc32ddf83ffc15", "URL": "https://instagram.com/p/CpdAlMVDtPN", "File": "resources/insta/resources/230ef6b7321b5ed6f5bc32ddf83ffc15.jpg", "Element": "<img>html tag 3"
#             }
#             ]
#          }
#         ]
#         data = [1, 2, 3, 2, "CqRIOcoImOn", 4, 5, 4, 6]
#         data = list(set(data))
#         print(data)
#         context  = {'data': data, "posts":post_data}
#         print(context)
#         return render(request, 'my_json_page1.html',context)
#     else:
#         return render(request, "instapic.html") 
    



my_list = [1, 2, 3, 2, 1, 4, 5, 4, 6]
unique_values = list(set(my_list))
print(unique_values)
print(type(unique_values))






def instapic(request):
    if request.method == 'POST':
        post_ids = request.POST.get('instapic')
        post_ids = post_ids.split(',')
        list_dict = []
        for post_id in post_ids:
            post = instaloader.Post.from_shortcode(L.context, shortcode= post_id)
            temp_json = {"post_id": post_id, "DATA": []}
            if post.typename == 'GraphImage':
                wget.download(post.url, out = 'resources/insta/resources/temp.jpg')
                MD5 = get_MD5('resources/insta/resources/temp.jpg').replace('.jpg','')
                new_name = 'resources/insta/resources/'+get_MD5('resources/insta/resources/temp.jpg')
                os.rename('resources/insta/resources/temp.jpg',new_name)
                element = '<img src="'+new_name+'" alt = ""></img>'
                element = convert_string_to_html_element(element)
                #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
                temp_dict = {
                                "post_id": post_id,
                                "Type": "Image",
                                "MD5": MD5,
                                "URL": post.url,
                                'File': new_name,
                                'Element': element
                             }
                temp_json["DATA"].append(temp_dict)


            if post.typename == 'GraphSidecar':
                for node in post.get_sidecar_nodes():
                    if node.is_video == True:
                        print("It's a video")
                        wget.download(node.video_url, out = 'resources/insta/resources/temp.mp4')
                        MD5 = get_MD5('resources/insta/resources/temp.mp4').replace('.jpg','')
                        new_name = 'resources/insta/resources/'+MD5+".mp4"
                        os.rename('resources/insta/resources/temp.mp4',new_name)
                        element = '<video src="'+new_name+'" controls></video>'
                        element = convert_string_to_html_element(element)
                        #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
                        temp_dict = {
                                        "post_id": post_id,
                                        "Type": "Video",
                                        "MD5": MD5,
                                        "URL": post.url,
                                        'File': new_name,
                                        'Element': element
                                    }
                        temp_json["DATA"].append(temp_dict)

                    else:
                        print("It's a pic")
                        wget.download(node.display_url, out = 'resources/insta/resources/temp.jpg')
                        MD5 = get_MD5('resources/insta/resources/temp.jpg').replace('.jpg','')
                        new_name = 'resources/insta/resources/'+get_MD5('resources/insta/resources/temp.jpg')
                        os.rename('resources/insta/resources/temp.jpg',new_name)
                        element = '<img src="'+new_name+'" alt = ""></img>'
                        element = convert_string_to_html_element(element)
                        #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
                        temp_dict = {
                                        "post_id": post_id,
                                        "Type": "Image",
                                        "MD5": MD5,
                                        "URL": post.url,
                                        'File': new_name,
                                        'Element': element
                                    }
                        temp_json["DATA"].append(temp_dict)




            if post.is_video == True:
                wget.download(post.video_url, out = 'resources/insta/resources/temp.mp4')
                MD5 = get_MD5('resources/insta/resources/temp.mp4').replace('.jpg','')
                new_name = 'resources/insta/resources/'+MD5+".mp4"
                os.rename('resources/insta/resources/temp.mp4',new_name)
                element = '<video src="'+new_name+'" controls></video>'
                element = convert_string_to_html_element(element)
                #file_entries, post_id, type= 'Image', MD5, URL = post.url, file_loc = new_name                
                temp_dict = {
                                "post_id": post_id,
                                "Type": "Video",
                                "MD5": MD5,
                                "URL": post.url,
                                'File': new_name,
                                'Element': element
                             }
                temp_json["DATA"].append(temp_dict)
            list_dict.append(temp_json)    

        print(list_dict)
        data = {'data': list_dict}
        # return render(request, 'my_json_page.html',{'data': json_data})
        # return JsonResponse(data,safe=True)
        return render(request, 'my_json_page1.html',data)
    else:
        return render(request, "instapic.html")     
