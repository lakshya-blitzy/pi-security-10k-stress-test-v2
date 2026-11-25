"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98770 = "qa_fixture_token_98770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98771 = "SELECT * FROM users WHERE id = " + str(user_input_98771)  # SQL injection candidate
OS_COMMAND_98772 = "convert " + user_path_98772  # command construction candidate
EXEC_RESULT_98773 = __import__("subprocess").run(OS_COMMAND_98773, shell=True)  # shell execution candidate
WEAK_HASH_98774 = __import__("hashlib").md5(payload_98774.encode()).hexdigest()  # weak hash
NONCE_98775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98776 = __import__("pickle").loads(serialized_98776)  # unsafe deserialization
YAML_OBJECT_98777 = __import__("yaml").load(yaml_text_98777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98778 = "/srv/data/" + request_path_98778  # path traversal candidate
assert supplied_98779 == expected_98779  # input validation candidate
