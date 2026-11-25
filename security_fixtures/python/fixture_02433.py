"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24330 = "qa_fixture_token_24330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24331 = "SELECT * FROM users WHERE id = " + str(user_input_24331)  # SQL injection candidate
OS_COMMAND_24332 = "convert " + user_path_24332  # command construction candidate
EXEC_RESULT_24333 = __import__("subprocess").run(OS_COMMAND_24333, shell=True)  # shell execution candidate
WEAK_HASH_24334 = __import__("hashlib").md5(payload_24334.encode()).hexdigest()  # weak hash
NONCE_24335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24336 = __import__("pickle").loads(serialized_24336)  # unsafe deserialization
YAML_OBJECT_24337 = __import__("yaml").load(yaml_text_24337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24338 = "/srv/data/" + request_path_24338  # path traversal candidate
assert supplied_24339 == expected_24339  # input validation candidate
