from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import MemoryGameResult, ReactionTestResult, TestInformation, UserResult, Questions, UserAnswer, UserTestTemp
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

# Home and general pages
def home(request):
    """View for the home page"""
    return render(request, 'home.html')

def about(request):
    """View for the about page"""
    return render(request, 'about.html')

def games_list(request):
    """View for displaying the list of available games"""
    return render(request, 'games_list.html')

def test_list(request):
    if request.user.is_authenticated:
        tests = TestInformation.objects.all()  # objects manager ishlatildi
        return render(request, 'test_list.html', {'tests': tests})

    else:
        return redirect("login")

def test_detail(request, test_id):
    test = get_object_or_404(TestInformation, id=test_id)
    questions = Questions.objects.filter(test=test)
    
    if request.method == 'POST':
        correct_answers = 0
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question.correct:
                correct_answers += 1
        
        total_questions = questions.count()
        score = (correct_answers / total_questions * 100) if total_questions > 0 else 0
        wrong_answers = total_questions - correct_answers

        # Foydalanuvchi login bo‘lganini tekshiramiz
        if request.user.is_authenticated:
            UserResult.objects.create(
                user=request.user,
                test = test, 
                test_count=total_questions,
                correct=correct_answers,
                wrong=wrong_answers,
                ball=round(score, 2)
            )

        return render(request, 'test_results.html', {
            'test': test,
            'correct_answers': correct_answers,
            'total_questions': total_questions,
            'score': round(score, 2),
        })
    
    return render(request, 'test_detail.html', {
        'test': test,
        'questions': questions
    })

def Question(request, id) :
    tests = get_object_or_404(TestInformation, id = id)
    questions = Questions.objects.filter(test_direction = tests)
    
    context = {
        "question" : questions,
        "tests" : tests,
    }
    
    return render(request, "start_test.html", context)

def User_Results(request) :
    results = UserResult.objects.filter(user=request.user).order_by('-id')[:10]
    
    context = {
        "results" : results,
    }
    
    return render(request, "test_results.html", context)

# User authentication views
def register_view(request):
    """View for user registration without forms.py"""
    if request.method == 'POST':
        # Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validate form data
        errors = []
        
        if not username:
            errors.append('Username is required')
        elif User.objects.filter(username=username).exists():
            errors.append('Username already exists')
            
        if not email:
            errors.append('Email is required')
        elif User.objects.filter(email=email).exists():
            errors.append('Email already exists')
            
        if not password1:
            errors.append('Password is required')
            
        if password1 != password2:
            errors.append('Passwords do not match')
            
        # If there are errors, display them
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'register.html', {
                'username': username,
                'email': email
            })
            
        # Create user
        try:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            messages.success(request, f'Account created for {username}! You are now logged in.')
            return redirect('home')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'register.html', {
                'username': username,
                'email': email
            })
    
    # For GET request
    return render(request, 'register.html')

def login_view(request):
    """View for user login without forms.py"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            
            # Redirect to next page if specified, otherwise to home
            next_page = request.POST.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html', {'username': username})
    
    # For GET request
    return render(request, 'login.html')

def logout_view(request):
    """View for user logout"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required
def profile_view(request):
    """View for user profile"""
    # Get user's game results
    memory_results = MemoryGameResult.objects.filter(user=request.user).order_by('-created_at')[:5]
    reaction_results = ReactionTestResult.objects.filter(user=request.user).order_by('-created_at')[:5]
    results = UserResult.objects.filter(user=request.user).order_by('-id')[:10]
    
    # Calculate statistics
    memory_count = MemoryGameResult.objects.filter(user=request.user).count()
    reaction_count = ReactionTestResult.objects.filter(user=request.user).count()
    
    # Handle profile update
    if request.method == 'POST':
        # Get form data
        email = request.POST.get('email')
        
        # Validate email
        if not email:
            messages.error(request, 'Email is required')
        else:
            # Update user
            try:
                request.user.email = email
                request.user.save()
                messages.success(request, 'Your profile has been updated!')
            except Exception as e:
                messages.error(request, f'Error updating profile: {str(e)}')
    
    context = {
        'email': request.user.email,
        'memory_results': memory_results,
        'reaction_results': reaction_results,
        'memory_count': memory_count,
        'reaction_count': reaction_count,
        'user_results': results,
        'total_tests': results.count(),
    }
    
    return render(request, 'profile.html', context)

# Game views
def memory_game(request):
    if request.user.is_authenticated:
        """View for rendering the memory game page"""
        return render(request, 'memory_game.html')
    else :
        return redirect('login')
    
def reaction_test(request):
    if request.user.is_authenticated:
        """View for rendering the reaction test game page"""
        return render(request, 'reaction_test.html')
    else :
        return redirect('login')

def game_results_list(request):
    """View for displaying all saved game results"""
    memory_results = MemoryGameResult.objects.all()[:10]
    reaction_results = ReactionTestResult.objects.all()[:10]
    user_test_results = UserResult.objects.select_related('user', 'test').all()[:10]
    
    context = {
        'memory_results': memory_results,
        'reaction_results': reaction_results,
        'user_test_results' : user_test_results
    }
    
    return render(request, 'game_results_list.html', context)

# Game score saving views
@require_POST
def save_memory_score(request):
    """View for saving memory game scores"""
    if request.method == 'POST':
        # Get data directly from POST request
        game_name = request.POST.get('game_name', 'Memory Game')
        time = request.POST.get('time')
        moves_str = request.POST.get('moves')
        difficulty = request.POST.get('difficulty')
        
        # Validate the data
        errors = []
        
        if not time:
            errors.append('Time is required')
        
        if not moves_str:
            errors.append('Moves count is required')
        else:
            try:
                moves = int(moves_str)
                if moves < 1:
                    errors.append('Moves must be a positive number')
            except ValueError:
                errors.append('Moves must be a valid number')
                moves = 0  # Default value
        
        if not difficulty:
            errors.append('Difficulty is required')
        elif difficulty not in ['easy', 'medium', 'hard']:
            errors.append('Invalid difficulty level')
        
        # If there are validation errors
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('memory_game')
        
        # Save the data to the database
        try:
            result = MemoryGameResult(
                game_name=game_name,
                time=time,
                moves=moves,
                difficulty=difficulty
            )
            
            # Associate with user if logged in
            if request.user.is_authenticated:
                result.user = request.user
                
            result.save()
            messages.success(request, 'Your score has been saved successfully!')
            return redirect('game_results_list')
        except Exception as e:
            messages.error(request, f'Error saving your score: {str(e)}')
            return redirect('memory_game')

@require_POST
def save_speed_math_score(request):
    """View for saving speed math game scores"""
    if request.method == 'POST':
        # Get data directly from POST request
        game_name = request.POST.get('game_name', 'Speed Math')
        score_str = request.POST.get('score')
        correct_str = request.POST.get('correct_answers')
        incorrect_str = request.POST.get('incorrect_answers')
        accuracy_str = request.POST.get('accuracy')
        difficulty = request.POST.get('difficulty')
        operation = request.POST.get('operation')
        
        # Validate the data
        errors = []
        
        try:
            score = int(score_str)
            correct_answers = int(correct_str)
            incorrect_answers = int(incorrect_str)
            accuracy = int(accuracy_str)
        except (ValueError, TypeError):
            errors.append('Invalid score data')
            score = 0
            correct_answers = 0
            incorrect_answers = 0
            accuracy = 0
        
        if not difficulty:
            errors.append('Difficulty is required')
        elif difficulty not in ['easy', 'medium', 'hard']:
            errors.append('Invalid difficulty level')
            
        if not operation:
            errors.append('Operation type is required')
        elif operation not in ['addition', 'subtraction', 'multiplication', 'division', 'mixed']:
            errors.append('Invalid operation type')
    

@require_POST
def save_reaction_test(request):
    """View for saving reaction test results"""
    if request.method == 'POST':
        # Get data directly from POST request
        game_name = request.POST.get('game_name', 'Reaction Test')
        reaction_time_str = request.POST.get('reaction_time')
        attempts_str = request.POST.get('attempts')
        average_time_str = request.POST.get('average_time')
        
        # Validate the data
        errors = []
        
        try:
            reaction_time = int(reaction_time_str)
            attempts = int(attempts_str)
            average_time = int(average_time_str)
            
            if reaction_time < 0 or attempts < 1 or average_time < 0:
                errors.append('Invalid reaction test data')
        except (ValueError, TypeError):
            errors.append('Invalid reaction test data')
            reaction_time = 0
            attempts = 0
            average_time = 0
        
        # If there are validation errors
        if errors:
            for error in errors:
                messages.error(request, error)
            return redirect('reaction_test')
        
        # Save the data to the database
        try:
            result = ReactionTestResult(
                game_name=game_name,
                reaction_time=reaction_time,
                attempts=attempts,
                average_time=average_time
            )
            
            # Associate with user if logged in
            if request.user.is_authenticated:
                result.user = request.user
                
            result.save()
            messages.success(request, 'Your reaction test result has been saved successfully!')
            return redirect('game_results_list')
        except Exception as e:
            messages.error(request, f'Error saving your result: {str(e)}')
            return redirect('reaction_test')
