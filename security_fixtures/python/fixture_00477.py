"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4770 = "qa_fixture_token_4770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4771 = "SELECT * FROM users WHERE id = " + str(user_input_4771)  # SQL injection candidate
OS_COMMAND_4772 = "convert " + user_path_4772  # command construction candidate
EXEC_RESULT_4773 = __import__("subprocess").run(OS_COMMAND_4773, shell=True)  # shell execution candidate
WEAK_HASH_4774 = __import__("hashlib").md5(payload_4774.encode()).hexdigest()  # weak hash
NONCE_4775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4776 = __import__("pickle").loads(serialized_4776)  # unsafe deserialization
YAML_OBJECT_4777 = __import__("yaml").load(yaml_text_4777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4778 = "/srv/data/" + request_path_4778  # path traversal candidate
assert supplied_4779 == expected_4779  # input validation candidate
