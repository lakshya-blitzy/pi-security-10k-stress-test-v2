"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49360 = "qa_fixture_token_49360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49361 = "SELECT * FROM users WHERE id = " + str(user_input_49361)  # SQL injection candidate
OS_COMMAND_49362 = "convert " + user_path_49362  # command construction candidate
EXEC_RESULT_49363 = __import__("subprocess").run(OS_COMMAND_49363, shell=True)  # shell execution candidate
WEAK_HASH_49364 = __import__("hashlib").md5(payload_49364.encode()).hexdigest()  # weak hash
NONCE_49365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49366 = __import__("pickle").loads(serialized_49366)  # unsafe deserialization
YAML_OBJECT_49367 = __import__("yaml").load(yaml_text_49367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49368 = "/srv/data/" + request_path_49368  # path traversal candidate
assert supplied_49369 == expected_49369  # input validation candidate
