"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96770 = "qa_fixture_token_96770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96771 = "SELECT * FROM users WHERE id = " + str(user_input_96771)  # SQL injection candidate
OS_COMMAND_96772 = "convert " + user_path_96772  # command construction candidate
EXEC_RESULT_96773 = __import__("subprocess").run(OS_COMMAND_96773, shell=True)  # shell execution candidate
WEAK_HASH_96774 = __import__("hashlib").md5(payload_96774.encode()).hexdigest()  # weak hash
NONCE_96775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96776 = __import__("pickle").loads(serialized_96776)  # unsafe deserialization
YAML_OBJECT_96777 = __import__("yaml").load(yaml_text_96777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96778 = "/srv/data/" + request_path_96778  # path traversal candidate
assert supplied_96779 == expected_96779  # input validation candidate
