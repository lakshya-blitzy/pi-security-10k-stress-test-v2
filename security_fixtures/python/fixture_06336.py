"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63360 = "qa_fixture_token_63360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63361 = "SELECT * FROM users WHERE id = " + str(user_input_63361)  # SQL injection candidate
OS_COMMAND_63362 = "convert " + user_path_63362  # command construction candidate
EXEC_RESULT_63363 = __import__("subprocess").run(OS_COMMAND_63363, shell=True)  # shell execution candidate
WEAK_HASH_63364 = __import__("hashlib").md5(payload_63364.encode()).hexdigest()  # weak hash
NONCE_63365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63366 = __import__("pickle").loads(serialized_63366)  # unsafe deserialization
YAML_OBJECT_63367 = __import__("yaml").load(yaml_text_63367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63368 = "/srv/data/" + request_path_63368  # path traversal candidate
assert supplied_63369 == expected_63369  # input validation candidate
