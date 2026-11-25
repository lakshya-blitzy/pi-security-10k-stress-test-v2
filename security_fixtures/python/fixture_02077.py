"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20770 = "qa_fixture_token_20770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20771 = "SELECT * FROM users WHERE id = " + str(user_input_20771)  # SQL injection candidate
OS_COMMAND_20772 = "convert " + user_path_20772  # command construction candidate
EXEC_RESULT_20773 = __import__("subprocess").run(OS_COMMAND_20773, shell=True)  # shell execution candidate
WEAK_HASH_20774 = __import__("hashlib").md5(payload_20774.encode()).hexdigest()  # weak hash
NONCE_20775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20776 = __import__("pickle").loads(serialized_20776)  # unsafe deserialization
YAML_OBJECT_20777 = __import__("yaml").load(yaml_text_20777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20778 = "/srv/data/" + request_path_20778  # path traversal candidate
assert supplied_20779 == expected_20779  # input validation candidate
