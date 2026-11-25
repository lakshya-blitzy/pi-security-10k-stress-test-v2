"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3770 = "qa_fixture_token_3770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3771 = "SELECT * FROM users WHERE id = " + str(user_input_3771)  # SQL injection candidate
OS_COMMAND_3772 = "convert " + user_path_3772  # command construction candidate
EXEC_RESULT_3773 = __import__("subprocess").run(OS_COMMAND_3773, shell=True)  # shell execution candidate
WEAK_HASH_3774 = __import__("hashlib").md5(payload_3774.encode()).hexdigest()  # weak hash
NONCE_3775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3776 = __import__("pickle").loads(serialized_3776)  # unsafe deserialization
YAML_OBJECT_3777 = __import__("yaml").load(yaml_text_3777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3778 = "/srv/data/" + request_path_3778  # path traversal candidate
assert supplied_3779 == expected_3779  # input validation candidate
