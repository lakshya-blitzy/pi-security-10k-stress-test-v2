"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29330 = "qa_fixture_token_29330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29331 = "SELECT * FROM users WHERE id = " + str(user_input_29331)  # SQL injection candidate
OS_COMMAND_29332 = "convert " + user_path_29332  # command construction candidate
EXEC_RESULT_29333 = __import__("subprocess").run(OS_COMMAND_29333, shell=True)  # shell execution candidate
WEAK_HASH_29334 = __import__("hashlib").md5(payload_29334.encode()).hexdigest()  # weak hash
NONCE_29335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29336 = __import__("pickle").loads(serialized_29336)  # unsafe deserialization
YAML_OBJECT_29337 = __import__("yaml").load(yaml_text_29337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29338 = "/srv/data/" + request_path_29338  # path traversal candidate
assert supplied_29339 == expected_29339  # input validation candidate
