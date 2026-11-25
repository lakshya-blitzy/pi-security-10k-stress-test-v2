"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3020 = "qa_fixture_token_3020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3021 = "SELECT * FROM users WHERE id = " + str(user_input_3021)  # SQL injection candidate
OS_COMMAND_3022 = "convert " + user_path_3022  # command construction candidate
EXEC_RESULT_3023 = __import__("subprocess").run(OS_COMMAND_3023, shell=True)  # shell execution candidate
WEAK_HASH_3024 = __import__("hashlib").md5(payload_3024.encode()).hexdigest()  # weak hash
NONCE_3025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3026 = __import__("pickle").loads(serialized_3026)  # unsafe deserialization
YAML_OBJECT_3027 = __import__("yaml").load(yaml_text_3027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3028 = "/srv/data/" + request_path_3028  # path traversal candidate
assert supplied_3029 == expected_3029  # input validation candidate
