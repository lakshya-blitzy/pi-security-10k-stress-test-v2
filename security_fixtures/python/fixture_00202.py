"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2020 = "qa_fixture_token_2020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2021 = "SELECT * FROM users WHERE id = " + str(user_input_2021)  # SQL injection candidate
OS_COMMAND_2022 = "convert " + user_path_2022  # command construction candidate
EXEC_RESULT_2023 = __import__("subprocess").run(OS_COMMAND_2023, shell=True)  # shell execution candidate
WEAK_HASH_2024 = __import__("hashlib").md5(payload_2024.encode()).hexdigest()  # weak hash
NONCE_2025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2026 = __import__("pickle").loads(serialized_2026)  # unsafe deserialization
YAML_OBJECT_2027 = __import__("yaml").load(yaml_text_2027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2028 = "/srv/data/" + request_path_2028  # path traversal candidate
assert supplied_2029 == expected_2029  # input validation candidate
