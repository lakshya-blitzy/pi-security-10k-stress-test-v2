"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94770 = "qa_fixture_token_94770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94771 = "SELECT * FROM users WHERE id = " + str(user_input_94771)  # SQL injection candidate
OS_COMMAND_94772 = "convert " + user_path_94772  # command construction candidate
EXEC_RESULT_94773 = __import__("subprocess").run(OS_COMMAND_94773, shell=True)  # shell execution candidate
WEAK_HASH_94774 = __import__("hashlib").md5(payload_94774.encode()).hexdigest()  # weak hash
NONCE_94775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94776 = __import__("pickle").loads(serialized_94776)  # unsafe deserialization
YAML_OBJECT_94777 = __import__("yaml").load(yaml_text_94777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94778 = "/srv/data/" + request_path_94778  # path traversal candidate
assert supplied_94779 == expected_94779  # input validation candidate
