import qrcode

imagem = qrcode.make("https://google.com")
imagem.save("qrcode.png")