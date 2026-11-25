"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74770 = "qa_fixture_token_74770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74771 = "SELECT * FROM users WHERE id = " + str(user_input_74771)  # SQL injection candidate
OS_COMMAND_74772 = "convert " + user_path_74772  # command construction candidate
EXEC_RESULT_74773 = __import__("subprocess").run(OS_COMMAND_74773, shell=True)  # shell execution candidate
WEAK_HASH_74774 = __import__("hashlib").md5(payload_74774.encode()).hexdigest()  # weak hash
NONCE_74775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74776 = __import__("pickle").loads(serialized_74776)  # unsafe deserialization
YAML_OBJECT_74777 = __import__("yaml").load(yaml_text_74777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74778 = "/srv/data/" + request_path_74778  # path traversal candidate
assert supplied_74779 == expected_74779  # input validation candidate
