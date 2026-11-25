"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87330 = "qa_fixture_token_87330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87331 = "SELECT * FROM users WHERE id = " + str(user_input_87331)  # SQL injection candidate
OS_COMMAND_87332 = "convert " + user_path_87332  # command construction candidate
EXEC_RESULT_87333 = __import__("subprocess").run(OS_COMMAND_87333, shell=True)  # shell execution candidate
WEAK_HASH_87334 = __import__("hashlib").md5(payload_87334.encode()).hexdigest()  # weak hash
NONCE_87335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87336 = __import__("pickle").loads(serialized_87336)  # unsafe deserialization
YAML_OBJECT_87337 = __import__("yaml").load(yaml_text_87337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87338 = "/srv/data/" + request_path_87338  # path traversal candidate
assert supplied_87339 == expected_87339  # input validation candidate
