"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19770 = "qa_fixture_token_19770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19771 = "SELECT * FROM users WHERE id = " + str(user_input_19771)  # SQL injection candidate
OS_COMMAND_19772 = "convert " + user_path_19772  # command construction candidate
EXEC_RESULT_19773 = __import__("subprocess").run(OS_COMMAND_19773, shell=True)  # shell execution candidate
WEAK_HASH_19774 = __import__("hashlib").md5(payload_19774.encode()).hexdigest()  # weak hash
NONCE_19775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19776 = __import__("pickle").loads(serialized_19776)  # unsafe deserialization
YAML_OBJECT_19777 = __import__("yaml").load(yaml_text_19777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19778 = "/srv/data/" + request_path_19778  # path traversal candidate
assert supplied_19779 == expected_19779  # input validation candidate
