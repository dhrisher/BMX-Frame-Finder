from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.db.models import Func, F
from decimal import *


###################################################################################################################

def frame_home(request):
    if request.method == 'POST':
        height = request.POST['height_slider']
        discipline = request.POST['disc_slider']
        price = request.POST['price_slider']
        order_by = 'suitability'

        return redirect('/search/{}/{}/{}/{}/'.format(height, discipline, price, order_by))

    return render(request, 'framesearch/frame_home.html')

####################################################################################################################


def frame_search(request, height, discipline, price, order_by):
    if request.method == 'POST':

        height = request.POST['height_slider']
        discipline = request.POST['disc_slider']
        price = request.POST['price_slider']
        order_by = request.POST['filter_options']

        return redirect('/search/{}/{}/{}/{}/'.format(height, discipline, price, order_by))

    else:

        # values to set the selected filter option
        order_by_s = ""
        order_by_h = ""
        order_by_l = ""

        # returns a value between 0-93 depending on how extreme the geometry value is
        # 0-93% id the range of the left:x% value of the indicator element
        # upper and lower values are the range that those bmx geometries are typically available in
        # inverse flips a value if higher value equals different discipline
        def process_value(upper_value, lower_value, value, inverse):
            processed_value = (value - lower_value) * (1 / (upper_value - lower_value)) * 93
            if inverse is True:
                processed_value = ((processed_value - 93) * -1)
            return processed_value

        # averages processed valued of geometry, gives overall discipline suitability value
        def discipline_average(cs, ht, st):

            discipline_average_value = (cs + ht + st) / 3

            return discipline_average_value

        def calculate_suitability(frame_value, user_value):
            value = frame_value - user_value
            # remove negatives
            value = abs(value)
            return value

        frames = Frame.objects.all()
        # add processed values to be  used for the stat bar styling
        # multiplied by 93 as 93% is the final left: x% value for the stat bars
        for frame in frames:
            frame.chainstay_processed = process_value(14.0, 12.5, float(frame.chainstay), True)
            frame.seat_tube_processed = process_value(71.5, 69.0, float(frame.seat_tube_angle), False)
            frame.head_tube_processed = process_value(75.5, 74.5, float(frame.head_tube_angle), True)
            frame.discipline_average = discipline_average(float(frame.chainstay_processed),
                                                          float(frame.head_tube_processed),
                                                          float(frame.seat_tube_processed))
            frame.save()

        # only show frames with discipline value +-15 from user selection
        upper_range = process_value(18, 0, discipline, False) + 15
        lower_range = process_value(18, 0, discipline, False) - 15
        frames = frames.filter(discipline_average__gte=lower_range).filter(discipline_average__lte=upper_range)

        # calculate how close the user discipline value is to the frame average
        for frame in frames:
            frame.suitability = calculate_suitability(float(frame.discipline_average), process_value(18, 0, discipline, False))
            frame.save()

        # filter out by price selection
        price_dict = {0: 150, 1: 200, 2: 250, 3: 300, 4: 350, 5: 400, 6: 450, 7:500}
        if price < 8:
            frames = frames.filter(price__lte=price_dict[price])
        else:
            frames = frames.filter(price__gte=500)

        # filter out by height
        # from 5ft to 6ft the frame size will go from 18 - 21 inch
        # between 5-6 ft is 12 increments, between 18 - 21 inch is a 3 inch increments
        # for each unit increment in height there is a 3/12 = 0.25 increase in frame length
        # height to frame length

        frame_length = (height*0.25)+18

        upper_range = frame_length + 0.3
        lower_range = frame_length - 0.3

        # set limit on either end

        if lower_range < 18.0:
            lower_range = 16.0
            upper_range = 18.0
        if upper_range > 21.0:
            upper_range = 30.0
            lower_range = 21.0

        # iterate through each frame size and show the frame if one of the frames matches the chosen range

        list_of_pks = []

        for frame in frames:
            for length in frame.size.all():
                if lower_range <= length.size <= upper_range:
                    my_pk = frame.pk
                    list_of_pks.append(my_pk)

        frames = Frame.objects.filter(pk__in=list_of_pks)

        # ordering by user selection and reset the selected option element

        if order_by == 'low_to_high':
            frames = frames.order_by('price')
            order_by_s = ""
            order_by_h = ""
            order_by_l = "selected"

        elif order_by == 'high_to_low':
            frames = frames.order_by('-price')
            order_by_s = ""
            order_by_h = "selected"
            order_by_l = ""

        else:
            # lower the suitability value the closer the usr value was the frame discipline value
            frames = frames.order_by('suitability')
            order_by_s = "selected"
            order_by_h = ""
            order_by_l = ""

        # Show x items per page.
        paginator = Paginator(frames, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {'page_obj': page_obj, 'height': height, 'discipline': discipline,
                   'price': price, 'order_by_s': order_by_s, 'order_by_h': order_by_h,
                   'order_by_l': order_by_l}

        return render(request, 'framesearch/frame_search.html', context)
