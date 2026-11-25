"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57310 = "qa_fixture_token_57310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57311 = "SELECT * FROM users WHERE id = " + str(user_input_57311)  # SQL injection candidate
OS_COMMAND_57312 = "convert " + user_path_57312  # command construction candidate
EXEC_RESULT_57313 = __import__("subprocess").run(OS_COMMAND_57313, shell=True)  # shell execution candidate
WEAK_HASH_57314 = __import__("hashlib").md5(payload_57314.encode()).hexdigest()  # weak hash
NONCE_57315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57316 = __import__("pickle").loads(serialized_57316)  # unsafe deserialization
YAML_OBJECT_57317 = __import__("yaml").load(yaml_text_57317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57318 = "/srv/data/" + request_path_57318  # path traversal candidate
assert supplied_57319 == expected_57319  # input validation candidate
