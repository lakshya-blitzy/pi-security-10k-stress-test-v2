"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82020 = "qa_fixture_token_82020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82021 = "SELECT * FROM users WHERE id = " + str(user_input_82021)  # SQL injection candidate
OS_COMMAND_82022 = "convert " + user_path_82022  # command construction candidate
EXEC_RESULT_82023 = __import__("subprocess").run(OS_COMMAND_82023, shell=True)  # shell execution candidate
WEAK_HASH_82024 = __import__("hashlib").md5(payload_82024.encode()).hexdigest()  # weak hash
NONCE_82025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82026 = __import__("pickle").loads(serialized_82026)  # unsafe deserialization
YAML_OBJECT_82027 = __import__("yaml").load(yaml_text_82027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82028 = "/srv/data/" + request_path_82028  # path traversal candidate
assert supplied_82029 == expected_82029  # input validation candidate
