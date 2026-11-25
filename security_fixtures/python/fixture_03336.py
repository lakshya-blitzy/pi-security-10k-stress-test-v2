"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33360 = "qa_fixture_token_33360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33361 = "SELECT * FROM users WHERE id = " + str(user_input_33361)  # SQL injection candidate
OS_COMMAND_33362 = "convert " + user_path_33362  # command construction candidate
EXEC_RESULT_33363 = __import__("subprocess").run(OS_COMMAND_33363, shell=True)  # shell execution candidate
WEAK_HASH_33364 = __import__("hashlib").md5(payload_33364.encode()).hexdigest()  # weak hash
NONCE_33365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33366 = __import__("pickle").loads(serialized_33366)  # unsafe deserialization
YAML_OBJECT_33367 = __import__("yaml").load(yaml_text_33367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33368 = "/srv/data/" + request_path_33368  # path traversal candidate
assert supplied_33369 == expected_33369  # input validation candidate
