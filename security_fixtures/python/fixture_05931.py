"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59310 = "qa_fixture_token_59310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59311 = "SELECT * FROM users WHERE id = " + str(user_input_59311)  # SQL injection candidate
OS_COMMAND_59312 = "convert " + user_path_59312  # command construction candidate
EXEC_RESULT_59313 = __import__("subprocess").run(OS_COMMAND_59313, shell=True)  # shell execution candidate
WEAK_HASH_59314 = __import__("hashlib").md5(payload_59314.encode()).hexdigest()  # weak hash
NONCE_59315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59316 = __import__("pickle").loads(serialized_59316)  # unsafe deserialization
YAML_OBJECT_59317 = __import__("yaml").load(yaml_text_59317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59318 = "/srv/data/" + request_path_59318  # path traversal candidate
assert supplied_59319 == expected_59319  # input validation candidate
