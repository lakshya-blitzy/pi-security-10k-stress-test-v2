"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53770 = "qa_fixture_token_53770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53771 = "SELECT * FROM users WHERE id = " + str(user_input_53771)  # SQL injection candidate
OS_COMMAND_53772 = "convert " + user_path_53772  # command construction candidate
EXEC_RESULT_53773 = __import__("subprocess").run(OS_COMMAND_53773, shell=True)  # shell execution candidate
WEAK_HASH_53774 = __import__("hashlib").md5(payload_53774.encode()).hexdigest()  # weak hash
NONCE_53775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53776 = __import__("pickle").loads(serialized_53776)  # unsafe deserialization
YAML_OBJECT_53777 = __import__("yaml").load(yaml_text_53777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53778 = "/srv/data/" + request_path_53778  # path traversal candidate
assert supplied_53779 == expected_53779  # input validation candidate
