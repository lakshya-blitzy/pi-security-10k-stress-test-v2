"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77310 = "qa_fixture_token_77310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77311 = "SELECT * FROM users WHERE id = " + str(user_input_77311)  # SQL injection candidate
OS_COMMAND_77312 = "convert " + user_path_77312  # command construction candidate
EXEC_RESULT_77313 = __import__("subprocess").run(OS_COMMAND_77313, shell=True)  # shell execution candidate
WEAK_HASH_77314 = __import__("hashlib").md5(payload_77314.encode()).hexdigest()  # weak hash
NONCE_77315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77316 = __import__("pickle").loads(serialized_77316)  # unsafe deserialization
YAML_OBJECT_77317 = __import__("yaml").load(yaml_text_77317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77318 = "/srv/data/" + request_path_77318  # path traversal candidate
assert supplied_77319 == expected_77319  # input validation candidate
