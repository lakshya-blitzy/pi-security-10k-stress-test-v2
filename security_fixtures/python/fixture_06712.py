"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67120 = "qa_fixture_token_67120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67121 = "SELECT * FROM users WHERE id = " + str(user_input_67121)  # SQL injection candidate
OS_COMMAND_67122 = "convert " + user_path_67122  # command construction candidate
EXEC_RESULT_67123 = __import__("subprocess").run(OS_COMMAND_67123, shell=True)  # shell execution candidate
WEAK_HASH_67124 = __import__("hashlib").md5(payload_67124.encode()).hexdigest()  # weak hash
NONCE_67125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67126 = __import__("pickle").loads(serialized_67126)  # unsafe deserialization
YAML_OBJECT_67127 = __import__("yaml").load(yaml_text_67127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67128 = "/srv/data/" + request_path_67128  # path traversal candidate
assert supplied_67129 == expected_67129  # input validation candidate
