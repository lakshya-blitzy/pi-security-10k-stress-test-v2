"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56770 = "qa_fixture_token_56770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56771 = "SELECT * FROM users WHERE id = " + str(user_input_56771)  # SQL injection candidate
OS_COMMAND_56772 = "convert " + user_path_56772  # command construction candidate
EXEC_RESULT_56773 = __import__("subprocess").run(OS_COMMAND_56773, shell=True)  # shell execution candidate
WEAK_HASH_56774 = __import__("hashlib").md5(payload_56774.encode()).hexdigest()  # weak hash
NONCE_56775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56776 = __import__("pickle").loads(serialized_56776)  # unsafe deserialization
YAML_OBJECT_56777 = __import__("yaml").load(yaml_text_56777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56778 = "/srv/data/" + request_path_56778  # path traversal candidate
assert supplied_56779 == expected_56779  # input validation candidate
