REGISTERED_USERS_PER_MONTH_QUERY = """
        WITH months AS (
            SELECT
                generate_series(
                    date_trunc('month', NOW() - INTERVAL '12 months'),
                    date_trunc('month', NOW() - INTERVAL '1 month'),
                    INTERVAL '1 month'
                ) AS month
        )
        SELECT
            TO_CHAR(m.month, 'YYYY-MM') AS month_year,
            TO_CHAR(m.month, 'Month') AS month_name,
            COALESCE(COUNT(u.registered_at), 0) AS registrations
        FROM
            months m
            LEFT JOIN users u ON u.registered_at >= m.month
                             AND u.registered_at < m.month + INTERVAL '1 month'
        GROUP BY
            m.month
        ORDER BY
            m.month;
        """
