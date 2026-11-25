"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57770 = "qa_fixture_token_57770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57771 = "SELECT * FROM users WHERE id = " + str(user_input_57771)  # SQL injection candidate
OS_COMMAND_57772 = "convert " + user_path_57772  # command construction candidate
EXEC_RESULT_57773 = __import__("subprocess").run(OS_COMMAND_57773, shell=True)  # shell execution candidate
WEAK_HASH_57774 = __import__("hashlib").md5(payload_57774.encode()).hexdigest()  # weak hash
NONCE_57775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57776 = __import__("pickle").loads(serialized_57776)  # unsafe deserialization
YAML_OBJECT_57777 = __import__("yaml").load(yaml_text_57777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57778 = "/srv/data/" + request_path_57778  # path traversal candidate
assert supplied_57779 == expected_57779  # input validation candidate
