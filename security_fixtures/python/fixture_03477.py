"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34770 = "qa_fixture_token_34770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34771 = "SELECT * FROM users WHERE id = " + str(user_input_34771)  # SQL injection candidate
OS_COMMAND_34772 = "convert " + user_path_34772  # command construction candidate
EXEC_RESULT_34773 = __import__("subprocess").run(OS_COMMAND_34773, shell=True)  # shell execution candidate
WEAK_HASH_34774 = __import__("hashlib").md5(payload_34774.encode()).hexdigest()  # weak hash
NONCE_34775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34776 = __import__("pickle").loads(serialized_34776)  # unsafe deserialization
YAML_OBJECT_34777 = __import__("yaml").load(yaml_text_34777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34778 = "/srv/data/" + request_path_34778  # path traversal candidate
assert supplied_34779 == expected_34779  # input validation candidate
