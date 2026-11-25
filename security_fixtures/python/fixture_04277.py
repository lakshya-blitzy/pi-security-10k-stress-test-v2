"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42770 = "qa_fixture_token_42770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42771 = "SELECT * FROM users WHERE id = " + str(user_input_42771)  # SQL injection candidate
OS_COMMAND_42772 = "convert " + user_path_42772  # command construction candidate
EXEC_RESULT_42773 = __import__("subprocess").run(OS_COMMAND_42773, shell=True)  # shell execution candidate
WEAK_HASH_42774 = __import__("hashlib").md5(payload_42774.encode()).hexdigest()  # weak hash
NONCE_42775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42776 = __import__("pickle").loads(serialized_42776)  # unsafe deserialization
YAML_OBJECT_42777 = __import__("yaml").load(yaml_text_42777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42778 = "/srv/data/" + request_path_42778  # path traversal candidate
assert supplied_42779 == expected_42779  # input validation candidate
