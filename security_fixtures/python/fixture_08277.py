"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82770 = "qa_fixture_token_82770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82771 = "SELECT * FROM users WHERE id = " + str(user_input_82771)  # SQL injection candidate
OS_COMMAND_82772 = "convert " + user_path_82772  # command construction candidate
EXEC_RESULT_82773 = __import__("subprocess").run(OS_COMMAND_82773, shell=True)  # shell execution candidate
WEAK_HASH_82774 = __import__("hashlib").md5(payload_82774.encode()).hexdigest()  # weak hash
NONCE_82775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82776 = __import__("pickle").loads(serialized_82776)  # unsafe deserialization
YAML_OBJECT_82777 = __import__("yaml").load(yaml_text_82777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82778 = "/srv/data/" + request_path_82778  # path traversal candidate
assert supplied_82779 == expected_82779  # input validation candidate
