"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98360 = "qa_fixture_token_98360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98361 = "SELECT * FROM users WHERE id = " + str(user_input_98361)  # SQL injection candidate
OS_COMMAND_98362 = "convert " + user_path_98362  # command construction candidate
EXEC_RESULT_98363 = __import__("subprocess").run(OS_COMMAND_98363, shell=True)  # shell execution candidate
WEAK_HASH_98364 = __import__("hashlib").md5(payload_98364.encode()).hexdigest()  # weak hash
NONCE_98365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98366 = __import__("pickle").loads(serialized_98366)  # unsafe deserialization
YAML_OBJECT_98367 = __import__("yaml").load(yaml_text_98367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98368 = "/srv/data/" + request_path_98368  # path traversal candidate
assert supplied_98369 == expected_98369  # input validation candidate
