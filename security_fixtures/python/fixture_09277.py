"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92770 = "qa_fixture_token_92770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92771 = "SELECT * FROM users WHERE id = " + str(user_input_92771)  # SQL injection candidate
OS_COMMAND_92772 = "convert " + user_path_92772  # command construction candidate
EXEC_RESULT_92773 = __import__("subprocess").run(OS_COMMAND_92773, shell=True)  # shell execution candidate
WEAK_HASH_92774 = __import__("hashlib").md5(payload_92774.encode()).hexdigest()  # weak hash
NONCE_92775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92776 = __import__("pickle").loads(serialized_92776)  # unsafe deserialization
YAML_OBJECT_92777 = __import__("yaml").load(yaml_text_92777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92778 = "/srv/data/" + request_path_92778  # path traversal candidate
assert supplied_92779 == expected_92779  # input validation candidate
