"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43360 = "qa_fixture_token_43360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43361 = "SELECT * FROM users WHERE id = " + str(user_input_43361)  # SQL injection candidate
OS_COMMAND_43362 = "convert " + user_path_43362  # command construction candidate
EXEC_RESULT_43363 = __import__("subprocess").run(OS_COMMAND_43363, shell=True)  # shell execution candidate
WEAK_HASH_43364 = __import__("hashlib").md5(payload_43364.encode()).hexdigest()  # weak hash
NONCE_43365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43366 = __import__("pickle").loads(serialized_43366)  # unsafe deserialization
YAML_OBJECT_43367 = __import__("yaml").load(yaml_text_43367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43368 = "/srv/data/" + request_path_43368  # path traversal candidate
assert supplied_43369 == expected_43369  # input validation candidate
