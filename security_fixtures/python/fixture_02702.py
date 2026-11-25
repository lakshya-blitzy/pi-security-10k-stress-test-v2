"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27020 = "qa_fixture_token_27020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27021 = "SELECT * FROM users WHERE id = " + str(user_input_27021)  # SQL injection candidate
OS_COMMAND_27022 = "convert " + user_path_27022  # command construction candidate
EXEC_RESULT_27023 = __import__("subprocess").run(OS_COMMAND_27023, shell=True)  # shell execution candidate
WEAK_HASH_27024 = __import__("hashlib").md5(payload_27024.encode()).hexdigest()  # weak hash
NONCE_27025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27026 = __import__("pickle").loads(serialized_27026)  # unsafe deserialization
YAML_OBJECT_27027 = __import__("yaml").load(yaml_text_27027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27028 = "/srv/data/" + request_path_27028  # path traversal candidate
assert supplied_27029 == expected_27029  # input validation candidate
