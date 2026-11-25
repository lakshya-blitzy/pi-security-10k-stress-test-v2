"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71310 = "qa_fixture_token_71310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71311 = "SELECT * FROM users WHERE id = " + str(user_input_71311)  # SQL injection candidate
OS_COMMAND_71312 = "convert " + user_path_71312  # command construction candidate
EXEC_RESULT_71313 = __import__("subprocess").run(OS_COMMAND_71313, shell=True)  # shell execution candidate
WEAK_HASH_71314 = __import__("hashlib").md5(payload_71314.encode()).hexdigest()  # weak hash
NONCE_71315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71316 = __import__("pickle").loads(serialized_71316)  # unsafe deserialization
YAML_OBJECT_71317 = __import__("yaml").load(yaml_text_71317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71318 = "/srv/data/" + request_path_71318  # path traversal candidate
assert supplied_71319 == expected_71319  # input validation candidate
