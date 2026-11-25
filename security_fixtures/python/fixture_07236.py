"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72360 = "qa_fixture_token_72360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72361 = "SELECT * FROM users WHERE id = " + str(user_input_72361)  # SQL injection candidate
OS_COMMAND_72362 = "convert " + user_path_72362  # command construction candidate
EXEC_RESULT_72363 = __import__("subprocess").run(OS_COMMAND_72363, shell=True)  # shell execution candidate
WEAK_HASH_72364 = __import__("hashlib").md5(payload_72364.encode()).hexdigest()  # weak hash
NONCE_72365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72366 = __import__("pickle").loads(serialized_72366)  # unsafe deserialization
YAML_OBJECT_72367 = __import__("yaml").load(yaml_text_72367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72368 = "/srv/data/" + request_path_72368  # path traversal candidate
assert supplied_72369 == expected_72369  # input validation candidate
