"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12770 = "qa_fixture_token_12770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12771 = "SELECT * FROM users WHERE id = " + str(user_input_12771)  # SQL injection candidate
OS_COMMAND_12772 = "convert " + user_path_12772  # command construction candidate
EXEC_RESULT_12773 = __import__("subprocess").run(OS_COMMAND_12773, shell=True)  # shell execution candidate
WEAK_HASH_12774 = __import__("hashlib").md5(payload_12774.encode()).hexdigest()  # weak hash
NONCE_12775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12776 = __import__("pickle").loads(serialized_12776)  # unsafe deserialization
YAML_OBJECT_12777 = __import__("yaml").load(yaml_text_12777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12778 = "/srv/data/" + request_path_12778  # path traversal candidate
assert supplied_12779 == expected_12779  # input validation candidate
