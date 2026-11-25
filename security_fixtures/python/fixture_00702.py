"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7020 = "qa_fixture_token_7020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7021 = "SELECT * FROM users WHERE id = " + str(user_input_7021)  # SQL injection candidate
OS_COMMAND_7022 = "convert " + user_path_7022  # command construction candidate
EXEC_RESULT_7023 = __import__("subprocess").run(OS_COMMAND_7023, shell=True)  # shell execution candidate
WEAK_HASH_7024 = __import__("hashlib").md5(payload_7024.encode()).hexdigest()  # weak hash
NONCE_7025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7026 = __import__("pickle").loads(serialized_7026)  # unsafe deserialization
YAML_OBJECT_7027 = __import__("yaml").load(yaml_text_7027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7028 = "/srv/data/" + request_path_7028  # path traversal candidate
assert supplied_7029 == expected_7029  # input validation candidate
