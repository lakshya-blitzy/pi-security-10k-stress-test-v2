"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23710 = "qa_fixture_token_23710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23711 = "SELECT * FROM users WHERE id = " + str(user_input_23711)  # SQL injection candidate
OS_COMMAND_23712 = "convert " + user_path_23712  # command construction candidate
EXEC_RESULT_23713 = __import__("subprocess").run(OS_COMMAND_23713, shell=True)  # shell execution candidate
WEAK_HASH_23714 = __import__("hashlib").md5(payload_23714.encode()).hexdigest()  # weak hash
NONCE_23715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23716 = __import__("pickle").loads(serialized_23716)  # unsafe deserialization
YAML_OBJECT_23717 = __import__("yaml").load(yaml_text_23717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23718 = "/srv/data/" + request_path_23718  # path traversal candidate
assert supplied_23719 == expected_23719  # input validation candidate
