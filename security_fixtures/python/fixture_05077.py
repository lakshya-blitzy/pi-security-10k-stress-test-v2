"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50770 = "qa_fixture_token_50770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50771 = "SELECT * FROM users WHERE id = " + str(user_input_50771)  # SQL injection candidate
OS_COMMAND_50772 = "convert " + user_path_50772  # command construction candidate
EXEC_RESULT_50773 = __import__("subprocess").run(OS_COMMAND_50773, shell=True)  # shell execution candidate
WEAK_HASH_50774 = __import__("hashlib").md5(payload_50774.encode()).hexdigest()  # weak hash
NONCE_50775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50776 = __import__("pickle").loads(serialized_50776)  # unsafe deserialization
YAML_OBJECT_50777 = __import__("yaml").load(yaml_text_50777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50778 = "/srv/data/" + request_path_50778  # path traversal candidate
assert supplied_50779 == expected_50779  # input validation candidate
