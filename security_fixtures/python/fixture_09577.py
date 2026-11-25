"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95770 = "qa_fixture_token_95770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95771 = "SELECT * FROM users WHERE id = " + str(user_input_95771)  # SQL injection candidate
OS_COMMAND_95772 = "convert " + user_path_95772  # command construction candidate
EXEC_RESULT_95773 = __import__("subprocess").run(OS_COMMAND_95773, shell=True)  # shell execution candidate
WEAK_HASH_95774 = __import__("hashlib").md5(payload_95774.encode()).hexdigest()  # weak hash
NONCE_95775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95776 = __import__("pickle").loads(serialized_95776)  # unsafe deserialization
YAML_OBJECT_95777 = __import__("yaml").load(yaml_text_95777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95778 = "/srv/data/" + request_path_95778  # path traversal candidate
assert supplied_95779 == expected_95779  # input validation candidate
