"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84770 = "qa_fixture_token_84770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84771 = "SELECT * FROM users WHERE id = " + str(user_input_84771)  # SQL injection candidate
OS_COMMAND_84772 = "convert " + user_path_84772  # command construction candidate
EXEC_RESULT_84773 = __import__("subprocess").run(OS_COMMAND_84773, shell=True)  # shell execution candidate
WEAK_HASH_84774 = __import__("hashlib").md5(payload_84774.encode()).hexdigest()  # weak hash
NONCE_84775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84776 = __import__("pickle").loads(serialized_84776)  # unsafe deserialization
YAML_OBJECT_84777 = __import__("yaml").load(yaml_text_84777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84778 = "/srv/data/" + request_path_84778  # path traversal candidate
assert supplied_84779 == expected_84779  # input validation candidate
