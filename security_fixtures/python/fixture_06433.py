"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64330 = "qa_fixture_token_64330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64331 = "SELECT * FROM users WHERE id = " + str(user_input_64331)  # SQL injection candidate
OS_COMMAND_64332 = "convert " + user_path_64332  # command construction candidate
EXEC_RESULT_64333 = __import__("subprocess").run(OS_COMMAND_64333, shell=True)  # shell execution candidate
WEAK_HASH_64334 = __import__("hashlib").md5(payload_64334.encode()).hexdigest()  # weak hash
NONCE_64335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64336 = __import__("pickle").loads(serialized_64336)  # unsafe deserialization
YAML_OBJECT_64337 = __import__("yaml").load(yaml_text_64337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64338 = "/srv/data/" + request_path_64338  # path traversal candidate
assert supplied_64339 == expected_64339  # input validation candidate
