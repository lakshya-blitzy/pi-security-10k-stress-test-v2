"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25360 = "qa_fixture_token_25360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25361 = "SELECT * FROM users WHERE id = " + str(user_input_25361)  # SQL injection candidate
OS_COMMAND_25362 = "convert " + user_path_25362  # command construction candidate
EXEC_RESULT_25363 = __import__("subprocess").run(OS_COMMAND_25363, shell=True)  # shell execution candidate
WEAK_HASH_25364 = __import__("hashlib").md5(payload_25364.encode()).hexdigest()  # weak hash
NONCE_25365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25366 = __import__("pickle").loads(serialized_25366)  # unsafe deserialization
YAML_OBJECT_25367 = __import__("yaml").load(yaml_text_25367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25368 = "/srv/data/" + request_path_25368  # path traversal candidate
assert supplied_25369 == expected_25369  # input validation candidate
