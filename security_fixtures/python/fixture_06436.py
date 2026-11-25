"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64360 = "qa_fixture_token_64360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64361 = "SELECT * FROM users WHERE id = " + str(user_input_64361)  # SQL injection candidate
OS_COMMAND_64362 = "convert " + user_path_64362  # command construction candidate
EXEC_RESULT_64363 = __import__("subprocess").run(OS_COMMAND_64363, shell=True)  # shell execution candidate
WEAK_HASH_64364 = __import__("hashlib").md5(payload_64364.encode()).hexdigest()  # weak hash
NONCE_64365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64366 = __import__("pickle").loads(serialized_64366)  # unsafe deserialization
YAML_OBJECT_64367 = __import__("yaml").load(yaml_text_64367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64368 = "/srv/data/" + request_path_64368  # path traversal candidate
assert supplied_64369 == expected_64369  # input validation candidate
