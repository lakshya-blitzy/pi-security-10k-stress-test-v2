"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65770 = "qa_fixture_token_65770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65771 = "SELECT * FROM users WHERE id = " + str(user_input_65771)  # SQL injection candidate
OS_COMMAND_65772 = "convert " + user_path_65772  # command construction candidate
EXEC_RESULT_65773 = __import__("subprocess").run(OS_COMMAND_65773, shell=True)  # shell execution candidate
WEAK_HASH_65774 = __import__("hashlib").md5(payload_65774.encode()).hexdigest()  # weak hash
NONCE_65775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65776 = __import__("pickle").loads(serialized_65776)  # unsafe deserialization
YAML_OBJECT_65777 = __import__("yaml").load(yaml_text_65777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65778 = "/srv/data/" + request_path_65778  # path traversal candidate
assert supplied_65779 == expected_65779  # input validation candidate
