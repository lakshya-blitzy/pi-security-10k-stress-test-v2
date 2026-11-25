"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28770 = "qa_fixture_token_28770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28771 = "SELECT * FROM users WHERE id = " + str(user_input_28771)  # SQL injection candidate
OS_COMMAND_28772 = "convert " + user_path_28772  # command construction candidate
EXEC_RESULT_28773 = __import__("subprocess").run(OS_COMMAND_28773, shell=True)  # shell execution candidate
WEAK_HASH_28774 = __import__("hashlib").md5(payload_28774.encode()).hexdigest()  # weak hash
NONCE_28775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28776 = __import__("pickle").loads(serialized_28776)  # unsafe deserialization
YAML_OBJECT_28777 = __import__("yaml").load(yaml_text_28777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28778 = "/srv/data/" + request_path_28778  # path traversal candidate
assert supplied_28779 == expected_28779  # input validation candidate
