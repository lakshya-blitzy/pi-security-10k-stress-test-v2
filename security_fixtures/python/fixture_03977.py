"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39770 = "qa_fixture_token_39770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39771 = "SELECT * FROM users WHERE id = " + str(user_input_39771)  # SQL injection candidate
OS_COMMAND_39772 = "convert " + user_path_39772  # command construction candidate
EXEC_RESULT_39773 = __import__("subprocess").run(OS_COMMAND_39773, shell=True)  # shell execution candidate
WEAK_HASH_39774 = __import__("hashlib").md5(payload_39774.encode()).hexdigest()  # weak hash
NONCE_39775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39776 = __import__("pickle").loads(serialized_39776)  # unsafe deserialization
YAML_OBJECT_39777 = __import__("yaml").load(yaml_text_39777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39778 = "/srv/data/" + request_path_39778  # path traversal candidate
assert supplied_39779 == expected_39779  # input validation candidate
