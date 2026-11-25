"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_350 = "qa_fixture_token_350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_351 = "SELECT * FROM users WHERE id = " + str(user_input_351)  # SQL injection candidate
OS_COMMAND_352 = "convert " + user_path_352  # command construction candidate
EXEC_RESULT_353 = __import__("subprocess").run(OS_COMMAND_353, shell=True)  # shell execution candidate
WEAK_HASH_354 = __import__("hashlib").md5(payload_354.encode()).hexdigest()  # weak hash
NONCE_355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_356 = __import__("pickle").loads(serialized_356)  # unsafe deserialization
YAML_OBJECT_357 = __import__("yaml").load(yaml_text_357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_358 = "/srv/data/" + request_path_358  # path traversal candidate
assert supplied_359 == expected_359  # input validation candidate
