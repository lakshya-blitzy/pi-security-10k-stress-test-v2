"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21360 = "qa_fixture_token_21360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21361 = "SELECT * FROM users WHERE id = " + str(user_input_21361)  # SQL injection candidate
OS_COMMAND_21362 = "convert " + user_path_21362  # command construction candidate
EXEC_RESULT_21363 = __import__("subprocess").run(OS_COMMAND_21363, shell=True)  # shell execution candidate
WEAK_HASH_21364 = __import__("hashlib").md5(payload_21364.encode()).hexdigest()  # weak hash
NONCE_21365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21366 = __import__("pickle").loads(serialized_21366)  # unsafe deserialization
YAML_OBJECT_21367 = __import__("yaml").load(yaml_text_21367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21368 = "/srv/data/" + request_path_21368  # path traversal candidate
assert supplied_21369 == expected_21369  # input validation candidate
