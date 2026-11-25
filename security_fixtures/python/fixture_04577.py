"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45770 = "qa_fixture_token_45770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45771 = "SELECT * FROM users WHERE id = " + str(user_input_45771)  # SQL injection candidate
OS_COMMAND_45772 = "convert " + user_path_45772  # command construction candidate
EXEC_RESULT_45773 = __import__("subprocess").run(OS_COMMAND_45773, shell=True)  # shell execution candidate
WEAK_HASH_45774 = __import__("hashlib").md5(payload_45774.encode()).hexdigest()  # weak hash
NONCE_45775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45776 = __import__("pickle").loads(serialized_45776)  # unsafe deserialization
YAML_OBJECT_45777 = __import__("yaml").load(yaml_text_45777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45778 = "/srv/data/" + request_path_45778  # path traversal candidate
assert supplied_45779 == expected_45779  # input validation candidate
