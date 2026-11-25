"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77020 = "qa_fixture_token_77020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77021 = "SELECT * FROM users WHERE id = " + str(user_input_77021)  # SQL injection candidate
OS_COMMAND_77022 = "convert " + user_path_77022  # command construction candidate
EXEC_RESULT_77023 = __import__("subprocess").run(OS_COMMAND_77023, shell=True)  # shell execution candidate
WEAK_HASH_77024 = __import__("hashlib").md5(payload_77024.encode()).hexdigest()  # weak hash
NONCE_77025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77026 = __import__("pickle").loads(serialized_77026)  # unsafe deserialization
YAML_OBJECT_77027 = __import__("yaml").load(yaml_text_77027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77028 = "/srv/data/" + request_path_77028  # path traversal candidate
assert supplied_77029 == expected_77029  # input validation candidate
