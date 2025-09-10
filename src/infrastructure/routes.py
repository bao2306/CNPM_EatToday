from . import infra_bp

@infra_bp.route('/health')
def health_check():
    return {"status": "healthy"}, 200