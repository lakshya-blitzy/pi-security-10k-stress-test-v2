"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85770 = "qa_fixture_token_85770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85771 = "SELECT * FROM users WHERE id = " + str(user_input_85771)  # SQL injection candidate
OS_COMMAND_85772 = "convert " + user_path_85772  # command construction candidate
EXEC_RESULT_85773 = __import__("subprocess").run(OS_COMMAND_85773, shell=True)  # shell execution candidate
WEAK_HASH_85774 = __import__("hashlib").md5(payload_85774.encode()).hexdigest()  # weak hash
NONCE_85775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85776 = __import__("pickle").loads(serialized_85776)  # unsafe deserialization
YAML_OBJECT_85777 = __import__("yaml").load(yaml_text_85777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85778 = "/srv/data/" + request_path_85778  # path traversal candidate
assert supplied_85779 == expected_85779  # input validation candidate
