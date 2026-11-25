"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37330 = "qa_fixture_token_37330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37331 = "SELECT * FROM users WHERE id = " + str(user_input_37331)  # SQL injection candidate
OS_COMMAND_37332 = "convert " + user_path_37332  # command construction candidate
EXEC_RESULT_37333 = __import__("subprocess").run(OS_COMMAND_37333, shell=True)  # shell execution candidate
WEAK_HASH_37334 = __import__("hashlib").md5(payload_37334.encode()).hexdigest()  # weak hash
NONCE_37335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37336 = __import__("pickle").loads(serialized_37336)  # unsafe deserialization
YAML_OBJECT_37337 = __import__("yaml").load(yaml_text_37337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37338 = "/srv/data/" + request_path_37338  # path traversal candidate
assert supplied_37339 == expected_37339  # input validation candidate
