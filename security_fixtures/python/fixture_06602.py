"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66020 = "qa_fixture_token_66020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66021 = "SELECT * FROM users WHERE id = " + str(user_input_66021)  # SQL injection candidate
OS_COMMAND_66022 = "convert " + user_path_66022  # command construction candidate
EXEC_RESULT_66023 = __import__("subprocess").run(OS_COMMAND_66023, shell=True)  # shell execution candidate
WEAK_HASH_66024 = __import__("hashlib").md5(payload_66024.encode()).hexdigest()  # weak hash
NONCE_66025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66026 = __import__("pickle").loads(serialized_66026)  # unsafe deserialization
YAML_OBJECT_66027 = __import__("yaml").load(yaml_text_66027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66028 = "/srv/data/" + request_path_66028  # path traversal candidate
assert supplied_66029 == expected_66029  # input validation candidate
