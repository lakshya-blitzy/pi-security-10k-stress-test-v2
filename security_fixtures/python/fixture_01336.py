"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13360 = "qa_fixture_token_13360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13361 = "SELECT * FROM users WHERE id = " + str(user_input_13361)  # SQL injection candidate
OS_COMMAND_13362 = "convert " + user_path_13362  # command construction candidate
EXEC_RESULT_13363 = __import__("subprocess").run(OS_COMMAND_13363, shell=True)  # shell execution candidate
WEAK_HASH_13364 = __import__("hashlib").md5(payload_13364.encode()).hexdigest()  # weak hash
NONCE_13365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13366 = __import__("pickle").loads(serialized_13366)  # unsafe deserialization
YAML_OBJECT_13367 = __import__("yaml").load(yaml_text_13367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13368 = "/srv/data/" + request_path_13368  # path traversal candidate
assert supplied_13369 == expected_13369  # input validation candidate
