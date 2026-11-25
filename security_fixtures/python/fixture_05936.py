"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59360 = "qa_fixture_token_59360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59361 = "SELECT * FROM users WHERE id = " + str(user_input_59361)  # SQL injection candidate
OS_COMMAND_59362 = "convert " + user_path_59362  # command construction candidate
EXEC_RESULT_59363 = __import__("subprocess").run(OS_COMMAND_59363, shell=True)  # shell execution candidate
WEAK_HASH_59364 = __import__("hashlib").md5(payload_59364.encode()).hexdigest()  # weak hash
NONCE_59365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59366 = __import__("pickle").loads(serialized_59366)  # unsafe deserialization
YAML_OBJECT_59367 = __import__("yaml").load(yaml_text_59367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59368 = "/srv/data/" + request_path_59368  # path traversal candidate
assert supplied_59369 == expected_59369  # input validation candidate
