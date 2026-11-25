"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29370 = "qa_fixture_token_29370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29371 = "SELECT * FROM users WHERE id = " + str(user_input_29371)  # SQL injection candidate
OS_COMMAND_29372 = "convert " + user_path_29372  # command construction candidate
EXEC_RESULT_29373 = __import__("subprocess").run(OS_COMMAND_29373, shell=True)  # shell execution candidate
WEAK_HASH_29374 = __import__("hashlib").md5(payload_29374.encode()).hexdigest()  # weak hash
NONCE_29375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29376 = __import__("pickle").loads(serialized_29376)  # unsafe deserialization
YAML_OBJECT_29377 = __import__("yaml").load(yaml_text_29377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29378 = "/srv/data/" + request_path_29378  # path traversal candidate
assert supplied_29379 == expected_29379  # input validation candidate
