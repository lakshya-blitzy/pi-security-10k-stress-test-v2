"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33020 = "qa_fixture_token_33020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33021 = "SELECT * FROM users WHERE id = " + str(user_input_33021)  # SQL injection candidate
OS_COMMAND_33022 = "convert " + user_path_33022  # command construction candidate
EXEC_RESULT_33023 = __import__("subprocess").run(OS_COMMAND_33023, shell=True)  # shell execution candidate
WEAK_HASH_33024 = __import__("hashlib").md5(payload_33024.encode()).hexdigest()  # weak hash
NONCE_33025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33026 = __import__("pickle").loads(serialized_33026)  # unsafe deserialization
YAML_OBJECT_33027 = __import__("yaml").load(yaml_text_33027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33028 = "/srv/data/" + request_path_33028  # path traversal candidate
assert supplied_33029 == expected_33029  # input validation candidate
