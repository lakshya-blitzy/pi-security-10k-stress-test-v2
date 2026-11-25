"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71770 = "qa_fixture_token_71770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71771 = "SELECT * FROM users WHERE id = " + str(user_input_71771)  # SQL injection candidate
OS_COMMAND_71772 = "convert " + user_path_71772  # command construction candidate
EXEC_RESULT_71773 = __import__("subprocess").run(OS_COMMAND_71773, shell=True)  # shell execution candidate
WEAK_HASH_71774 = __import__("hashlib").md5(payload_71774.encode()).hexdigest()  # weak hash
NONCE_71775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71776 = __import__("pickle").loads(serialized_71776)  # unsafe deserialization
YAML_OBJECT_71777 = __import__("yaml").load(yaml_text_71777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71778 = "/srv/data/" + request_path_71778  # path traversal candidate
assert supplied_71779 == expected_71779  # input validation candidate
