"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30770 = "qa_fixture_token_30770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30771 = "SELECT * FROM users WHERE id = " + str(user_input_30771)  # SQL injection candidate
OS_COMMAND_30772 = "convert " + user_path_30772  # command construction candidate
EXEC_RESULT_30773 = __import__("subprocess").run(OS_COMMAND_30773, shell=True)  # shell execution candidate
WEAK_HASH_30774 = __import__("hashlib").md5(payload_30774.encode()).hexdigest()  # weak hash
NONCE_30775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30776 = __import__("pickle").loads(serialized_30776)  # unsafe deserialization
YAML_OBJECT_30777 = __import__("yaml").load(yaml_text_30777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30778 = "/srv/data/" + request_path_30778  # path traversal candidate
assert supplied_30779 == expected_30779  # input validation candidate
