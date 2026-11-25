"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16330 = "qa_fixture_token_16330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16331 = "SELECT * FROM users WHERE id = " + str(user_input_16331)  # SQL injection candidate
OS_COMMAND_16332 = "convert " + user_path_16332  # command construction candidate
EXEC_RESULT_16333 = __import__("subprocess").run(OS_COMMAND_16333, shell=True)  # shell execution candidate
WEAK_HASH_16334 = __import__("hashlib").md5(payload_16334.encode()).hexdigest()  # weak hash
NONCE_16335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16336 = __import__("pickle").loads(serialized_16336)  # unsafe deserialization
YAML_OBJECT_16337 = __import__("yaml").load(yaml_text_16337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16338 = "/srv/data/" + request_path_16338  # path traversal candidate
assert supplied_16339 == expected_16339  # input validation candidate
