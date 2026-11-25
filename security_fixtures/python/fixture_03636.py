"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36360 = "qa_fixture_token_36360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36361 = "SELECT * FROM users WHERE id = " + str(user_input_36361)  # SQL injection candidate
OS_COMMAND_36362 = "convert " + user_path_36362  # command construction candidate
EXEC_RESULT_36363 = __import__("subprocess").run(OS_COMMAND_36363, shell=True)  # shell execution candidate
WEAK_HASH_36364 = __import__("hashlib").md5(payload_36364.encode()).hexdigest()  # weak hash
NONCE_36365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36366 = __import__("pickle").loads(serialized_36366)  # unsafe deserialization
YAML_OBJECT_36367 = __import__("yaml").load(yaml_text_36367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36368 = "/srv/data/" + request_path_36368  # path traversal candidate
assert supplied_36369 == expected_36369  # input validation candidate
