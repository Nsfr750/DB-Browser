import os
import logging
import json
from typing import Dict, Any
from database_handlers import get_database_handler

# Sample database configurations
SAMPLE_DATABASES = {
    'sqlite': {
        'path': 'sample_databases/employees.db',
        'description': 'Local SQLite database with employee records'
    },
    'mysql': {
        'path': {
            'type': 'mysql',
            'host': 'localhost',
            'user': 'demo_user',
            'password': 'demo_password',
            'database': 'company_db'
        },
        'description': 'MySQL database on local server'
    },
    'access': {
        'path': 'sample_databases/sales_records.mdb',
        'description': 'Microsoft Access database with sales data'
    },
    'mvo': {
        'path': 'sample_databases/product_inventory.mvo',
        'description': 'Multiversion Object database tracking product inventory'
    }
}

def demonstrate_database_handlers():
    """
    Comprehensive demonstration of database handler capabilities
    Showcases different database types and their unique features
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s: %(message)s',
        filename='database_demo.log',
        filemode='w'
    )
    logger = logging.getLogger('DatabaseDemo')

    def process_database(db_config):
        """
        Process and demonstrate database handler capabilities
        
        :param db_config: Configuration dictionary for the database
        """
        try:
            logger.info(f"Processing Database: {db_config.get('description', 'Unknown')}")
            
            # Determine if it's a file-based or network database
            if isinstance(db_config['path'], str):
                handler = get_database_handler(db_path=db_config['path'])
            else:
                handler = get_database_handler(connection_params=db_config['path'])
            
            if not handler:
                logger.warning(f"No handler found for {db_config}")
                return
            
            # Demonstration steps
            logger.info("🔍 Step 1: Connecting to Database")
            handler.connect()
            
            logger.info("📋 Step 2: Listing Tables")
            tables = handler.get_tables()
            logger.info(f"Tables found: {tables}")
            
            if not tables:
                logger.warning("No tables found in the database")
                return
            
            # Select first table for demonstration
            first_table = tables[0]
            logger.info(f"🔬 Step 3: Querying Table '{first_table}'")
            
            # Execute a basic query
            query_results = handler.execute_query(f"SELECT * FROM {first_table}")
            
            # Display first few rows
            logger.info("First 3 rows:")
            for row in query_results[:3]:
                logger.info(json.dumps(row, indent=2))
            
            # Export to CSV
            logger.info("💾 Step 4: Exporting Table to CSV")
            output_csv = f"{first_table}_export.csv"
            handler.export_to_csv(first_table, output_csv)
            logger.info(f"Exported {first_table} to {output_csv}")
            
            # Close connection
            handler.close()
            
            logger.info("✅ Database Processing Complete\n")
        
        except Exception as e:
            logger.error(f"❌ Error processing database: {e}")

    # Database Demonstration
    logger.info("🚀 Starting Database Handler Demonstrations")
    
    # Demonstrate each database type
    for db_type, db_config in SAMPLE_DATABASES.items():
        logger.info(f"\n🔹 Demonstrating {db_type.upper()} Database")
        process_database(db_config)
    
    logger.info("🏁 Database Handler Demonstrations Complete")

def create_sample_databases():
    """
    Create sample databases for demonstration
    This is a placeholder function - in a real scenario, you'd create actual sample databases
    """
    os.makedirs('sample_databases', exist_ok=True)
    
    # Simulated database creation
    sample_databases = {
        'employees.db': 'SQLite database',
        'sales_records.mdb': 'Microsoft Access database',
        'product_inventory.mvo': 'Multiversion Object database'
    }
    
    for filename, description in sample_databases.items():
        with open(os.path.join('sample_databases', filename), 'w') as f:
            f.write(f"# Placeholder for {description}")

def demo_database_handlers():
    """
    Demonstrate usage of different database handlers
    """
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s: %(message)s'
    )
    logger = logging.getLogger('DatabaseDemo')

    # Paths to sample databases (replace with your actual paths)
    sample_databases = {
        'sqlite': 'sample.db',
        'mysql': {
            'type': 'mysql',
            'host': 'localhost',
            'user': 'root',
            'password': 'password',
            'database': 'testdb'
        },
        'access': 'sample.mdb',
        'mvo': 'sample.mvo'
    }

    def process_database(db_path_or_params):
        """Process and demonstrate database handler capabilities"""
        try:
            # Get appropriate database handler
            handler = get_database_handler(
                db_path=db_path_or_params if isinstance(db_path_or_params, str) else None,
                connection_params=db_path_or_params if isinstance(db_path_or_params, dict) else None
            )

            if not handler:
                logger.warning(f"No handler found for {db_path_or_params}")
                return

            # Connect to the database
            handler.connect()

            # Get tables
            tables = handler.get_tables()
            logger.info(f"Tables found: {tables}")

            # If tables exist, execute a query and export to CSV
            if tables:
                first_table = tables[0]
                logger.info(f"Querying first table: {first_table}")
                
                # Execute query
                query_results = handler.execute_query(f"SELECT * FROM {first_table}")
                logger.info(f"First 3 rows: {query_results[:3]}")

                # Export to CSV
                output_csv = f"{first_table}_export.csv"
                handler.export_to_csv(first_table, output_csv)
                logger.info(f"Exported {first_table} to {output_csv}")

            # Close the connection
            handler.close()

        except Exception as e:
            logger.error(f"Error processing database: {e}")

    # Demonstrate each database type
    logger.info("Starting Database Handler Demonstrations")

    # Uncomment and modify paths/params as needed
    # process_database(sample_databases['sqlite'])
    # process_database(sample_databases['mysql'])
    # process_database(sample_databases['access'])
    # process_database(sample_databases['mvo'])

    logger.info("Database Handler Demonstrations Complete")

if __name__ == '__main__':
    create_sample_databases()
    demonstrate_database_handlers()
