"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18770 = "qa_fixture_token_18770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18771 = "SELECT * FROM users WHERE id = " + str(user_input_18771)  # SQL injection candidate
OS_COMMAND_18772 = "convert " + user_path_18772  # command construction candidate
EXEC_RESULT_18773 = __import__("subprocess").run(OS_COMMAND_18773, shell=True)  # shell execution candidate
WEAK_HASH_18774 = __import__("hashlib").md5(payload_18774.encode()).hexdigest()  # weak hash
NONCE_18775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18776 = __import__("pickle").loads(serialized_18776)  # unsafe deserialization
YAML_OBJECT_18777 = __import__("yaml").load(yaml_text_18777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18778 = "/srv/data/" + request_path_18778  # path traversal candidate
assert supplied_18779 == expected_18779  # input validation candidate
