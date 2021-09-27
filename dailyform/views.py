from django.shortcuts import render,redirect,get_object_or_404,reverse,HttpResponseRedirect
from . models import DailyFormModel,SaveQuestion,LikeApp
from . forms import DailyFormModelForm,SaveQuestionForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date,datetime


# Create your views here.
def home_page(request):
    today=date.today()
    user_count=User.objects.count()
    return render(request, "home.html", {'user_count':user_count, 'today':today})

@login_required(login_url="user:login")
def dailylist(request):
    if DailyFormModel.objects.filter(user=request.user).count()>=2:
        startday = DailyFormModel.objects.filter(user=request.user).first().created_date
        lastday = DailyFormModel.objects.filter(user=request.user).last().created_date
        lastday =  date.strftime(lastday, "%d")
        form=DailyFormModelForm(request.POST or None)
        if form.is_valid():
            dailyformmodel = form.save(commit=False)
            dailyformmodel.user = request.user
            created_date = form.cleaned_data.get('created_date')
            created_date = date.today().strftime("%d")
            if created_date != lastday:
                dailyformmodel.save()
                return redirect('daily')
            else:
                messages.info(request, 'You can only submit one form on the same day')
        return render(request, 'daily.html', {'form':form, 'startday':startday, 'lastday':lastday})
    elif DailyFormModel.objects.filter(user=request.user).count() == 1:
        howmanydays = DailyFormModel.objects.filter(user=request.user).count()
        startday = DailyFormModel.objects.filter(user=request.user).first().created_date
        startday = date.strftime(startday, "%d")
        form = DailyFormModelForm(request.POST or None)
        if form.is_valid():
            dailyformmodel = form.save(commit=False)
            dailyformmodel.user = request.user
            created_date = form.cleaned_data.get('created_date')
            created_date = date.today().strftime("%d")
            if created_date != startday:
                dailyformmodel.save()
                return redirect('daily')
            else:
                messages.info(request, 'You can only submit one form on the same day')
        return render(request, 'daily.html', {'form':form, 'startday':startday})
    elif DailyFormModel.objects.filter(user=request.user).count() == 0:
        form = DailyFormModelForm(request.POST or None)
        if form.is_valid():
            dailyformmodel = form.save(commit=False)
            dailyformmodel.user = request.user
            dailyformmodel.save()
            return redirect('daily')
        return render(request, 'daily.html', {'form': form})


@login_required(login_url="user:login")
def usergraphics(request):
    if DailyFormModel.objects.filter(user=request.user).exists():
        howmanydays=DailyFormModel.objects.filter(user=request.user).count()
        total = DailyFormModel.objects.filter(user=request.user).count()
        totalsleepingmin6hours = DailyFormModel.objects.filter(user=request.user, sleeping='1').count()
        totalsleeping6hours = DailyFormModel.objects.filter(user=request.user, sleeping='2').count()
        totalsleepingmax6hours = DailyFormModel.objects.filter(user=request.user, sleeping='3').count()
        percenttotalsleepingmin6hours = (100 * (totalsleepingmin6hours)) / total
        percenttotalsleepingmin6hours = round(percenttotalsleepingmin6hours,2)
        percenttotalsleeping6hours = (100 * (totalsleeping6hours)) / total
        percenttotalsleeping6hours = round(percenttotalsleeping6hours,2)
        percenttotalsleepingmax6hours = (100 * (totalsleepingmax6hours)) / total
        percenttotalsleepingmax6hours = round(percenttotalsleepingmax6hours,2)
        totaldrinkingwatermin2liters = DailyFormModel.objects.filter(user=request.user, drinkingwater='1').count()
        totaldrinkingwater2liters = DailyFormModel.objects.filter(user=request.user, drinkingwater='2').count()
        totaldrinkingwatermax2liters = DailyFormModel.objects.filter(user=request.user, drinkingwater='3').count()
        percenttotaldrinkingwatermin2liters = (100*(totaldrinkingwatermin2liters))/total
        percenttotaldrinkingwatermin2liters = round(percenttotaldrinkingwatermin2liters,2)
        percenttotaldrinkingwater2liters = (100*(totaldrinkingwater2liters))/total
        percenttotaldrinkingwater2liters = round(percenttotaldrinkingwater2liters,2)
        percenttotaldrinkingwatermax2liters = (100*(totaldrinkingwatermax2liters))/total
        percenttotaldrinkingwatermax2liters = round(percenttotaldrinkingwatermax2liters, 2)
        totalstepsmin5steps = DailyFormModel.objects.filter(user=request.user, steps='1').count()
        totalsteps5steps = DailyFormModel.objects.filter(user=request.user, steps='2').count()
        totalstepsmax5steps = DailyFormModel.objects.filter(user=request.user, steps='3').count()
        percenttotalstepsmin5steps = (100*(totalstepsmin5steps))/total
        percenttotalstepsmin5steps = round(percenttotalstepsmin5steps,2)
        percenttotalsteps5steps = (100*(totalsteps5steps))/total
        percenttotalsteps5steps = round(percenttotalsteps5steps,2)
        percenttotalstepsmax5steps = (100*(totalstepsmax5steps))/total
        percenttotalstepsmax5steps = round(percenttotalstepsmax5steps,2)
        totalsportsmin15minutes = DailyFormModel.objects.filter(user=request.user, sports='1').count()
        totalsports15minutes = DailyFormModel.objects.filter(user=request.user, sports='2').count()
        totalsportsmax15minutes = DailyFormModel.objects.filter(user=request.user, sports='3').count()
        percenttotalsportsmin15minutes = (100 * (totalsportsmin15minutes)) / total
        percenttotalsportsmin15minutes = round(percenttotalsportsmin15minutes, 2)
        percenttotalsports15minutes = (100 * (totalsports15minutes)) / total
        percenttotalsports15minutes = round(percenttotalsports15minutes, 2)
        percenttotalsportsmax15minutes = (100 * (totalsportsmax15minutes)) / total
        percenttotalsportsmax15minutes = round(percenttotalsportsmax15minutes, 2)
        totaleatingvegetables = DailyFormModel.objects.filter(user=request.user, eating='1').count()
        totaleatingvegetablesandmeat = DailyFormModel.objects.filter(user=request.user, eating='2').count()
        totaleatingmeat = DailyFormModel.objects.filter(user=request.user, eating=3).count()
        percenttotaleatingvegetables = (100*totaleatingvegetables)/total
        percenttotaleatingvegetables = round(percenttotaleatingvegetables, 2)
        percenttotaleatingvegetablesandmeat = (100*totaleatingvegetablesandmeat)/total
        percenttotaleatingvegetablesandmeat = round(percenttotaleatingvegetablesandmeat, 2)
        percenttotaleatingmeat = (100*totaleatingmeat)/total
        percenttotaleatingmeat = round(percenttotaleatingmeat, 2)
        totalstudymin1hour = DailyFormModel.objects.filter(user=request.user, study='1').count()
        totalstudybetween1and3hours = DailyFormModel.objects.filter(user=request.user, study='2').count()
        totalstudymax3hours = DailyFormModel.objects.filter(user=request.user, study=3).count()
        percenttotalstudymin1hour = (100*totalstudymin1hour)/total
        percenttotalstudymin1hour = round(percenttotalstudymin1hour, 2)
        percenttotalstudybetween1and3hours = (100*totalstudybetween1and3hours)/total
        percenttotalstudybetween1and3hours = round(percenttotalstudybetween1and3hours, 2)
        percenttotalstudymax3hours = (100*totalstudymax3hours)/total
        percenttotalstudymax3hours = round(percenttotalstudymax3hours, 2)
        form = SaveQuestionForm(request.POST or None)
        if form.is_valid():
            savequestion = form.save(commit=False)
            savequestion.user = request.user
            savequestion.save()
            return redirect('graphics')
        return render(request, 'graphics.html', {'total':total, 'totalsleepingmin6hours':totalsleepingmin6hours,
                                                 'totalsleeping6hours':totalsleeping6hours, 'totalsleepingmax6hours':totalsleepingmax6hours,
                                                 'percenttotalsleepingmin6hours':percenttotalsleepingmin6hours,
                                                 'percenttotalsleeping6hours':percenttotalsleeping6hours,
                                                 'percenttotalsleepingmax6hours':percenttotalsleepingmax6hours,
                                                 'totaldrinkingwatermin2liters':totaldrinkingwatermin2liters,
                                                 'totaldrinkingwater2liters':totaldrinkingwater2liters,
                                                 'totaldrinkingwatermax2liters':totaldrinkingwatermax2liters,
                                                 'percenttotaldrinkingwatermin2liters':percenttotaldrinkingwatermin2liters,
                                                 'percenttotaldrinkingwater2liters':percenttotaldrinkingwater2liters,
                                                 'percenttotaldrinkingwatermax2liters': percenttotaldrinkingwatermax2liters,
                                                 'percenttotalstepsmin5steps':percenttotalstepsmin5steps, 'percenttotalsteps5steps':percenttotalsteps5steps,
                                                 'percenttotalstepsmax5steps':percenttotalstepsmax5steps, 'percenttotalsportsmin15minutes':percenttotalsportsmin15minutes,
                                                 'percenttotalsports15minutes':percenttotalsports15minutes, 'percenttotalsportsmax15minutes':percenttotalsportsmax15minutes,
                                                 'percenttotaleatingvegetables':percenttotaleatingvegetables,
                                                 'percenttotaleatingvegetablesandmeat':percenttotaleatingvegetablesandmeat,
                                                 'percenttotaleatingmeat':percenttotaleatingmeat, 'percenttotalstudymin1hour':percenttotalstudymin1hour,
                                                 'percenttotalstudybetween1and3hours':percenttotalstudybetween1and3hours,
                                                 'percenttotalstudymax3hours':percenttotalstudymax3hours,
                                                 'form':form, 'howmanydays':howmanydays})
    else:
        form = SaveQuestionForm(request.POST or None)
        if form.is_valid():
            savequestion = form.save(commit=False)
            savequestion.user = request.user
            savequestion.save()
            return redirect('graphics')
        return render(request, "graphics.html", {"form":form})

def deletestartday(request):
    if DailyFormModel.objects.filter(user=request.user).exists():
        dailyformmodel=DailyFormModel.objects.filter(user=request.user)
        dailyformmodel.delete()
        return redirect("daily")
    else:
        return redirect("daily")

