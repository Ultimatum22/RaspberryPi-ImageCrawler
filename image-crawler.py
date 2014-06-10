import os
import argparse


class ImageCrawler():
    args = None;

    def __init__(self):
        pass


if __name__ == '__main__':
    crawler = ImageCrawler()

    parser = argparse.ArgumentParser(description='Image Scraper for media panel Raspberry Pi')
    parser.add_argument('-w', help='defines a maximum width (in pixels) for images', metavar='value', type=int)
    parser.add_argument('-v', help='verbose output', action='store_true')
    parser.add_argument('-f', help='force re-scraping (ignores and overwrites all images', action='store_true')
    args = parser.parse_args()

    if args.w:
        print 'max width set %spx.' % str(args.w)

    print 'all done'
