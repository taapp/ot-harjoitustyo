from repositories.series_repository import series_repository

def main():
    series = series_repository.get_default_series()
    series.print_all_questions()
    
if __name__=='__main__':
    main()