"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72120 = "qa_fixture_token_72120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72121 = "SELECT * FROM users WHERE id = " + str(user_input_72121)  # SQL injection candidate
OS_COMMAND_72122 = "convert " + user_path_72122  # command construction candidate
EXEC_RESULT_72123 = __import__("subprocess").run(OS_COMMAND_72123, shell=True)  # shell execution candidate
WEAK_HASH_72124 = __import__("hashlib").md5(payload_72124.encode()).hexdigest()  # weak hash
NONCE_72125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72126 = __import__("pickle").loads(serialized_72126)  # unsafe deserialization
YAML_OBJECT_72127 = __import__("yaml").load(yaml_text_72127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72128 = "/srv/data/" + request_path_72128  # path traversal candidate
assert supplied_72129 == expected_72129  # input validation candidate
