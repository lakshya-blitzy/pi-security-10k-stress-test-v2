"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86310 = "qa_fixture_token_86310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86311 = "SELECT * FROM users WHERE id = " + str(user_input_86311)  # SQL injection candidate
OS_COMMAND_86312 = "convert " + user_path_86312  # command construction candidate
EXEC_RESULT_86313 = __import__("subprocess").run(OS_COMMAND_86313, shell=True)  # shell execution candidate
WEAK_HASH_86314 = __import__("hashlib").md5(payload_86314.encode()).hexdigest()  # weak hash
NONCE_86315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86316 = __import__("pickle").loads(serialized_86316)  # unsafe deserialization
YAML_OBJECT_86317 = __import__("yaml").load(yaml_text_86317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86318 = "/srv/data/" + request_path_86318  # path traversal candidate
assert supplied_86319 == expected_86319  # input validation candidate
