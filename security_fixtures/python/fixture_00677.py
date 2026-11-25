"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6770 = "qa_fixture_token_6770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6771 = "SELECT * FROM users WHERE id = " + str(user_input_6771)  # SQL injection candidate
OS_COMMAND_6772 = "convert " + user_path_6772  # command construction candidate
EXEC_RESULT_6773 = __import__("subprocess").run(OS_COMMAND_6773, shell=True)  # shell execution candidate
WEAK_HASH_6774 = __import__("hashlib").md5(payload_6774.encode()).hexdigest()  # weak hash
NONCE_6775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6776 = __import__("pickle").loads(serialized_6776)  # unsafe deserialization
YAML_OBJECT_6777 = __import__("yaml").load(yaml_text_6777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6778 = "/srv/data/" + request_path_6778  # path traversal candidate
assert supplied_6779 == expected_6779  # input validation candidate
