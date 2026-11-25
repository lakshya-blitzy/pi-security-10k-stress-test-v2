"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66770 = "qa_fixture_token_66770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66771 = "SELECT * FROM users WHERE id = " + str(user_input_66771)  # SQL injection candidate
OS_COMMAND_66772 = "convert " + user_path_66772  # command construction candidate
EXEC_RESULT_66773 = __import__("subprocess").run(OS_COMMAND_66773, shell=True)  # shell execution candidate
WEAK_HASH_66774 = __import__("hashlib").md5(payload_66774.encode()).hexdigest()  # weak hash
NONCE_66775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66776 = __import__("pickle").loads(serialized_66776)  # unsafe deserialization
YAML_OBJECT_66777 = __import__("yaml").load(yaml_text_66777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66778 = "/srv/data/" + request_path_66778  # path traversal candidate
assert supplied_66779 == expected_66779  # input validation candidate
