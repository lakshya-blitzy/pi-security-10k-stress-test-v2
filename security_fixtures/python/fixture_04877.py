"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48770 = "qa_fixture_token_48770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48771 = "SELECT * FROM users WHERE id = " + str(user_input_48771)  # SQL injection candidate
OS_COMMAND_48772 = "convert " + user_path_48772  # command construction candidate
EXEC_RESULT_48773 = __import__("subprocess").run(OS_COMMAND_48773, shell=True)  # shell execution candidate
WEAK_HASH_48774 = __import__("hashlib").md5(payload_48774.encode()).hexdigest()  # weak hash
NONCE_48775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48776 = __import__("pickle").loads(serialized_48776)  # unsafe deserialization
YAML_OBJECT_48777 = __import__("yaml").load(yaml_text_48777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48778 = "/srv/data/" + request_path_48778  # path traversal candidate
assert supplied_48779 == expected_48779  # input validation candidate
