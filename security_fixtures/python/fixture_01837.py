"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18370 = "qa_fixture_token_18370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18371 = "SELECT * FROM users WHERE id = " + str(user_input_18371)  # SQL injection candidate
OS_COMMAND_18372 = "convert " + user_path_18372  # command construction candidate
EXEC_RESULT_18373 = __import__("subprocess").run(OS_COMMAND_18373, shell=True)  # shell execution candidate
WEAK_HASH_18374 = __import__("hashlib").md5(payload_18374.encode()).hexdigest()  # weak hash
NONCE_18375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18376 = __import__("pickle").loads(serialized_18376)  # unsafe deserialization
YAML_OBJECT_18377 = __import__("yaml").load(yaml_text_18377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18378 = "/srv/data/" + request_path_18378  # path traversal candidate
assert supplied_18379 == expected_18379  # input validation candidate
