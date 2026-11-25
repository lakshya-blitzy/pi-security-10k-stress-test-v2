"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49350 = "qa_fixture_token_49350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49351 = "SELECT * FROM users WHERE id = " + str(user_input_49351)  # SQL injection candidate
OS_COMMAND_49352 = "convert " + user_path_49352  # command construction candidate
EXEC_RESULT_49353 = __import__("subprocess").run(OS_COMMAND_49353, shell=True)  # shell execution candidate
WEAK_HASH_49354 = __import__("hashlib").md5(payload_49354.encode()).hexdigest()  # weak hash
NONCE_49355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49356 = __import__("pickle").loads(serialized_49356)  # unsafe deserialization
YAML_OBJECT_49357 = __import__("yaml").load(yaml_text_49357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49358 = "/srv/data/" + request_path_49358  # path traversal candidate
assert supplied_49359 == expected_49359  # input validation candidate
