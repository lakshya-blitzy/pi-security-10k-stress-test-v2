"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56020 = "qa_fixture_token_56020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56021 = "SELECT * FROM users WHERE id = " + str(user_input_56021)  # SQL injection candidate
OS_COMMAND_56022 = "convert " + user_path_56022  # command construction candidate
EXEC_RESULT_56023 = __import__("subprocess").run(OS_COMMAND_56023, shell=True)  # shell execution candidate
WEAK_HASH_56024 = __import__("hashlib").md5(payload_56024.encode()).hexdigest()  # weak hash
NONCE_56025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56026 = __import__("pickle").loads(serialized_56026)  # unsafe deserialization
YAML_OBJECT_56027 = __import__("yaml").load(yaml_text_56027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56028 = "/srv/data/" + request_path_56028  # path traversal candidate
assert supplied_56029 == expected_56029  # input validation candidate
