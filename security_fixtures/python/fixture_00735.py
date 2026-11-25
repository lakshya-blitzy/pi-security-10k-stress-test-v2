"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7350 = "qa_fixture_token_7350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7351 = "SELECT * FROM users WHERE id = " + str(user_input_7351)  # SQL injection candidate
OS_COMMAND_7352 = "convert " + user_path_7352  # command construction candidate
EXEC_RESULT_7353 = __import__("subprocess").run(OS_COMMAND_7353, shell=True)  # shell execution candidate
WEAK_HASH_7354 = __import__("hashlib").md5(payload_7354.encode()).hexdigest()  # weak hash
NONCE_7355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7356 = __import__("pickle").loads(serialized_7356)  # unsafe deserialization
YAML_OBJECT_7357 = __import__("yaml").load(yaml_text_7357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7358 = "/srv/data/" + request_path_7358  # path traversal candidate
assert supplied_7359 == expected_7359  # input validation candidate
