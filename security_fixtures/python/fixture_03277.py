"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32770 = "qa_fixture_token_32770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32771 = "SELECT * FROM users WHERE id = " + str(user_input_32771)  # SQL injection candidate
OS_COMMAND_32772 = "convert " + user_path_32772  # command construction candidate
EXEC_RESULT_32773 = __import__("subprocess").run(OS_COMMAND_32773, shell=True)  # shell execution candidate
WEAK_HASH_32774 = __import__("hashlib").md5(payload_32774.encode()).hexdigest()  # weak hash
NONCE_32775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32776 = __import__("pickle").loads(serialized_32776)  # unsafe deserialization
YAML_OBJECT_32777 = __import__("yaml").load(yaml_text_32777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32778 = "/srv/data/" + request_path_32778  # path traversal candidate
assert supplied_32779 == expected_32779  # input validation candidate
