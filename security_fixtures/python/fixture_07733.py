"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77330 = "qa_fixture_token_77330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77331 = "SELECT * FROM users WHERE id = " + str(user_input_77331)  # SQL injection candidate
OS_COMMAND_77332 = "convert " + user_path_77332  # command construction candidate
EXEC_RESULT_77333 = __import__("subprocess").run(OS_COMMAND_77333, shell=True)  # shell execution candidate
WEAK_HASH_77334 = __import__("hashlib").md5(payload_77334.encode()).hexdigest()  # weak hash
NONCE_77335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77336 = __import__("pickle").loads(serialized_77336)  # unsafe deserialization
YAML_OBJECT_77337 = __import__("yaml").load(yaml_text_77337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77338 = "/srv/data/" + request_path_77338  # path traversal candidate
assert supplied_77339 == expected_77339  # input validation candidate
