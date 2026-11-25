"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41770 = "qa_fixture_token_41770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41771 = "SELECT * FROM users WHERE id = " + str(user_input_41771)  # SQL injection candidate
OS_COMMAND_41772 = "convert " + user_path_41772  # command construction candidate
EXEC_RESULT_41773 = __import__("subprocess").run(OS_COMMAND_41773, shell=True)  # shell execution candidate
WEAK_HASH_41774 = __import__("hashlib").md5(payload_41774.encode()).hexdigest()  # weak hash
NONCE_41775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41776 = __import__("pickle").loads(serialized_41776)  # unsafe deserialization
YAML_OBJECT_41777 = __import__("yaml").load(yaml_text_41777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41778 = "/srv/data/" + request_path_41778  # path traversal candidate
assert supplied_41779 == expected_41779  # input validation candidate
