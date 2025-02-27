from app import db
from app.models.master import Master

class MasterDataManager:
    """
    Class for managing master data in the application.
    Makes it easy to maintain and add new data categories.
    """
    
    @staticmethod
    def clear_existing_data():
        """Clear all existing master data."""
        Master.query.delete()
    
    @staticmethod
    def add_master_records(master_type, master_type_name, data, has_value=False):
        """
        Add master records to the database.
        
        Args:
            master_type (str): Type code for the master data
            master_type_name (str): Display name for the master data type
            data (list): List of tuples containing the data
            has_value (bool): Whether the data includes a value field
        """
        for item in data:
            master_data = {
                'master_type': master_type,
                'master_type_name': master_type_name,
                'master_code': item[0],
                'master_name': item[1]
            }
            
            if has_value:
                master_data['master_value'] = item[2]
                master_data['master_unit'] = '￥'
                
            db.session.add(Master(**master_data))
    
    @classmethod
    def insert_master_data(cls):
        """Insert all master data into the database."""
        try:
            # Clear existing data
            cls.clear_existing_data()
            
            # Add all categories of master data
            cls.insert_job_titles()
            cls.insert_levels()
            cls.insert_unit_prices()
            cls.insert_services_categories()
            cls.insert_business_categories()
            
            # Commit all changes
            db.session.commit()
            print("Master data inserted successfully")
            
        except Exception as e:
            db.session.rollback()
            print(f"Error inserting master data: {str(e)}")
            raise
    
    @classmethod
    def insert_job_titles(cls):
        """Insert job title master data."""
        job_titles = [
            ('ceo', 'CEO'),
            ('dm', 'Delivery Manager'),
            ('pm', 'Project Manager'),
            ('pl', 'Project Leader'),
            ('be', 'Backend Engineer'),
            ('fe', 'Frontend Engineer'),
            ('brse', 'Bridge System Engineer'),
            ('comtor', 'Communicator'),
            ('qatester', 'Quality Assurance / Tester'),
            ('ba', 'Business Analyst'),
            ('sa', 'Solution Architect'),
            ('devops', 'DevOps Engineer'),
            ('uiux', 'UI/UX Designer'),
            ('aiml', 'AI/ML Engineer'),
            ('mobile', 'Mobile Engineer')
        ]
        cls.add_master_records('job_title', 'Job Title', job_titles)
    
    @classmethod
    def insert_levels(cls):
        """Insert level master data."""
        levels = [
            ('junior', 'Junior'),
            ('middle', 'Middle'),
            ('lead', 'Leader'),
            ('senior', 'Senior')
        ]
        cls.add_master_records('level', 'Level', levels)
    
    @classmethod
    def insert_unit_prices(cls):
        """Insert unit price master data."""
        unit_prices = [
            ('pm_junior', 'Junior Project Manager', '900000'),
            ('pm_middle', 'Middle Project Manager', '1000000'),
            ('pm_lead', 'Lead Project Manager', '1100000'),
            ('pm_senior', 'Senior Project Manager', '1200000'),
            ('pl_junior', 'Junior Project Leader', '700000'),
            ('pl_middle', 'Middle Project Leader', '800000'),
            ('pl_lead', 'Lead Project Leader', '900000'),
            ('pl_senior', 'Senior Project Leader', '1000000'),
            ('brse_junior', 'Junior Bridge System Engineer', '750000'),
            ('brse_middle', 'Middle Bridge System Engineer', '990000'),
            ('brse_lead', 'Lead Bridge System Engineer', '1200000'),
            ('brse_senior', 'Senior Bridge System Engineer', '1560000'),
            ('comtor_junior', 'Junior Communicator', '650000'),
            ('comtor_middle', 'Middle Communicator', '650000'),
            ('comtor_lead', 'Lead Communicator', '650000'),
            ('comtor_senior', 'Senior Communicator', '650000'),
            ('be_junior', 'Junior Backend Engineer', '300000'),
            ('be_middle', 'Middle Backend Engineer', '450000'),
            ('be_lead', 'Lead Backend Engineer', '750000'),
            ('be_senior', 'Senior Backend Engineer', '1050000'),
            ('fe_junior', 'Junior Frontend Engineer', '300000'),
            ('fe_middle', 'Middle Frontend Engineer', '450000'),
            ('fe_lead', 'Lead Frontend Engineer', '750000'),
            ('fe_senior', 'Senior Frontend Engineer', '1050000'),
            ('qatester_junior', 'Junior QA/Tester', '350000'),
            ('qatester_middle', 'Middle QA/Tester', '400000'),
            ('qatester_lead', 'Lead QA/Tester', '550000'),
            ('qatester_senior', 'Senior QA/Tester', '750000'),
            ('ba_junior', 'Junior Business Analyst', '300000'),
            ('ba_middle', 'Middle Business Analyst', '450000'),
            ('ba_lead', 'Lead Business Analyst', '750000'),
            ('ba_senior', 'Senior Business Analyst', '1050000'),
            ('sa_junior', 'Junior Solution Architect', '300000'),
            ('sa_middle', 'Middle Solution Architect', '450000'),
            ('sa_lead', 'Lead Solution Architect', '750000'),
            ('sa_senior', 'Senior Solution Architect', '1050000'),
            ('devops_junior', 'Junior DevOps Engineer', '300000'),
            ('devops_middle', 'Middle DevOps Engineer', '450000'),
            ('devops_lead', 'Lead DevOps Engineer', '750000'),
            ('devops_senior', 'Senior DevOps Engineer', '1050000'),
            ('uiux_junior', 'Junior UI/UX Designer', '300000'),
            ('uiux_middle', 'Middle UI/UX Designer', '450000'),
            ('uiux_lead', 'Lead UI/UX Designer', '750000'),
            ('uiux_senior', 'Senior UI/UX Designer', '1050000'),
            ('aiml_junior', 'Junior AI/ML Engineer', '300000'),
            ('aiml_middle', 'Middle AI/ML Engineer', '450000'),
            ('aiml_lead', 'Lead AI/ML Engineer', '750000'),
            ('aiml_senior', 'Senior AI/ML Engineer', '1050000'),
            ('mobile_junior', 'Junior Mobile Engineer', '300000'),
            ('mobile_middle', 'Middle Mobile Engineer', '450000'),
            ('mobile_lead', 'Lead Mobile Engineer', '750000'),
            ('mobile_senior', 'Senior Mobile Engineer', '1050000')
        ]
        cls.add_master_records('unit_price', 'Unit Price', unit_prices, has_value=True)
    
    @classmethod
    def insert_services_categories(cls):
        """Insert services category master data."""
        services_categories = [
            ('art_design', 'Art & Design (アート&デザイン)'),
            ('auto_vehicles', 'Auto & Vehicles (自動車)'),
            ('beauty', 'Beauty (美容)'),
            ('books_reference', 'Books & Reference (書籍&参考書)'),
            ('business', 'Business (ビジネス)'),
            ('comics', 'Comics (コミック)'),
            ('communication', 'Communication (通信)'),
            ('dating', 'Dating (出会い)'),
            ('education', 'Education (教育)'),
            ('entertainment', 'Entertainment (エンタメ)'),
            ('events', 'Events (イベント)'),
            ('finance', 'Finance (ファイナンス)'),
            ('food_drink', 'Food & Drink (フード&ドリンク)'),
            ('game', 'Game (ゲーム)'),
            ('health_fitness', 'Health & Fitness (健康&フィットネス)'),
            ('house_home', 'House & Home (住まい&インテリア)'),
            ('libraries_demo', 'Libraries & Demo (ライブラリ&デモ)'),
            ('lifestyle', 'Lifestyle (ライフスタイル)'),
            ('maps_navigation', 'Maps & Navigation (地図&ナビ)'),
            ('medical', 'Medical (医療)'),
            ('music_audio', 'Music & Audio (音楽&オーディオ)'),
            ('news_magazines', 'News & Magazines (ニュース&雑誌)'),
            ('parenting', 'Parenting (出産&育児)'),
            ('parents_children', 'Parents & Children (親子向け)'),
            ('personalization', 'Personalization (カスタマイズ)'),
            ('photography', 'Photography (写真)'),
            ('productivity', 'Productivity (仕事効率化)'),
            ('shopping', 'Shopping (ショッピング)'),
            ('social', 'Social (ソーシャルネットワーク)'),
            ('sports', 'Sports (スポーツ)'),
            ('tools', 'Tools (ツール)'),
            ('travel_local', 'Travel & Local (旅行&地域)'),
            ('video_players_editors', 'Video Players & Editors (動画プレイヤー&エディタ)'),
            ('weather', 'Weather (天気)')
        ]
        cls.add_master_records('services_category', 'Services Category', services_categories)
    
    @classmethod
    def insert_business_categories(cls):
        """Insert business category master data."""
        business_categories = [
            ('BtoB', 'BtoB: Business to Business (企業と企業)'),
            ('BtoC', 'BtoC: Business to Consumer (企業と消費者)'),
            ('BtoE', 'BtoE: Business to Employee (企業と従業員)'),
            ('BtoG', 'BtoG: Business to Government (企業と行政)'),
            ('CtoC', 'CtoC: Consumer to Consumer (消費者と消費者)'),
            ('GtoC', 'GtoC: Government to Consumer (行政と消費者)')
        ]
        cls.add_master_records('business_category', 'Business Category', business_categories)


# Usage example
# if __name__ == '__main__':
#     MasterDataManager.insert_master_data()