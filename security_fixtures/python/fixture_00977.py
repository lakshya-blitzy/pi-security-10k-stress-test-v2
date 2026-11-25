"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9770 = "qa_fixture_token_9770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9771 = "SELECT * FROM users WHERE id = " + str(user_input_9771)  # SQL injection candidate
OS_COMMAND_9772 = "convert " + user_path_9772  # command construction candidate
EXEC_RESULT_9773 = __import__("subprocess").run(OS_COMMAND_9773, shell=True)  # shell execution candidate
WEAK_HASH_9774 = __import__("hashlib").md5(payload_9774.encode()).hexdigest()  # weak hash
NONCE_9775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9776 = __import__("pickle").loads(serialized_9776)  # unsafe deserialization
YAML_OBJECT_9777 = __import__("yaml").load(yaml_text_9777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9778 = "/srv/data/" + request_path_9778  # path traversal candidate
assert supplied_9779 == expected_9779  # input validation candidate
