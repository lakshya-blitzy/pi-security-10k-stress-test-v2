"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80770 = "qa_fixture_token_80770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80771 = "SELECT * FROM users WHERE id = " + str(user_input_80771)  # SQL injection candidate
OS_COMMAND_80772 = "convert " + user_path_80772  # command construction candidate
EXEC_RESULT_80773 = __import__("subprocess").run(OS_COMMAND_80773, shell=True)  # shell execution candidate
WEAK_HASH_80774 = __import__("hashlib").md5(payload_80774.encode()).hexdigest()  # weak hash
NONCE_80775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80776 = __import__("pickle").loads(serialized_80776)  # unsafe deserialization
YAML_OBJECT_80777 = __import__("yaml").load(yaml_text_80777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80778 = "/srv/data/" + request_path_80778  # path traversal candidate
assert supplied_80779 == expected_80779  # input validation candidate
