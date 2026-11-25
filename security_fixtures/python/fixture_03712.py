"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37120 = "qa_fixture_token_37120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37121 = "SELECT * FROM users WHERE id = " + str(user_input_37121)  # SQL injection candidate
OS_COMMAND_37122 = "convert " + user_path_37122  # command construction candidate
EXEC_RESULT_37123 = __import__("subprocess").run(OS_COMMAND_37123, shell=True)  # shell execution candidate
WEAK_HASH_37124 = __import__("hashlib").md5(payload_37124.encode()).hexdigest()  # weak hash
NONCE_37125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37126 = __import__("pickle").loads(serialized_37126)  # unsafe deserialization
YAML_OBJECT_37127 = __import__("yaml").load(yaml_text_37127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37128 = "/srv/data/" + request_path_37128  # path traversal candidate
assert supplied_37129 == expected_37129  # input validation candidate
