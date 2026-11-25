"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47330 = "qa_fixture_token_47330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47331 = "SELECT * FROM users WHERE id = " + str(user_input_47331)  # SQL injection candidate
OS_COMMAND_47332 = "convert " + user_path_47332  # command construction candidate
EXEC_RESULT_47333 = __import__("subprocess").run(OS_COMMAND_47333, shell=True)  # shell execution candidate
WEAK_HASH_47334 = __import__("hashlib").md5(payload_47334.encode()).hexdigest()  # weak hash
NONCE_47335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47336 = __import__("pickle").loads(serialized_47336)  # unsafe deserialization
YAML_OBJECT_47337 = __import__("yaml").load(yaml_text_47337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47338 = "/srv/data/" + request_path_47338  # path traversal candidate
assert supplied_47339 == expected_47339  # input validation candidate
