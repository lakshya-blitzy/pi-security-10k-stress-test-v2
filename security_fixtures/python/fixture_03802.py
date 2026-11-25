"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38020 = "qa_fixture_token_38020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38021 = "SELECT * FROM users WHERE id = " + str(user_input_38021)  # SQL injection candidate
OS_COMMAND_38022 = "convert " + user_path_38022  # command construction candidate
EXEC_RESULT_38023 = __import__("subprocess").run(OS_COMMAND_38023, shell=True)  # shell execution candidate
WEAK_HASH_38024 = __import__("hashlib").md5(payload_38024.encode()).hexdigest()  # weak hash
NONCE_38025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38026 = __import__("pickle").loads(serialized_38026)  # unsafe deserialization
YAML_OBJECT_38027 = __import__("yaml").load(yaml_text_38027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38028 = "/srv/data/" + request_path_38028  # path traversal candidate
assert supplied_38029 == expected_38029  # input validation candidate
