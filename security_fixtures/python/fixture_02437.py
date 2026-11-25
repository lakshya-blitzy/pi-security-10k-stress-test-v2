"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24370 = "qa_fixture_token_24370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24371 = "SELECT * FROM users WHERE id = " + str(user_input_24371)  # SQL injection candidate
OS_COMMAND_24372 = "convert " + user_path_24372  # command construction candidate
EXEC_RESULT_24373 = __import__("subprocess").run(OS_COMMAND_24373, shell=True)  # shell execution candidate
WEAK_HASH_24374 = __import__("hashlib").md5(payload_24374.encode()).hexdigest()  # weak hash
NONCE_24375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24376 = __import__("pickle").loads(serialized_24376)  # unsafe deserialization
YAML_OBJECT_24377 = __import__("yaml").load(yaml_text_24377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24378 = "/srv/data/" + request_path_24378  # path traversal candidate
assert supplied_24379 == expected_24379  # input validation candidate
