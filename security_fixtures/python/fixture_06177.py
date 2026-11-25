"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61770 = "qa_fixture_token_61770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61771 = "SELECT * FROM users WHERE id = " + str(user_input_61771)  # SQL injection candidate
OS_COMMAND_61772 = "convert " + user_path_61772  # command construction candidate
EXEC_RESULT_61773 = __import__("subprocess").run(OS_COMMAND_61773, shell=True)  # shell execution candidate
WEAK_HASH_61774 = __import__("hashlib").md5(payload_61774.encode()).hexdigest()  # weak hash
NONCE_61775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61776 = __import__("pickle").loads(serialized_61776)  # unsafe deserialization
YAML_OBJECT_61777 = __import__("yaml").load(yaml_text_61777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61778 = "/srv/data/" + request_path_61778  # path traversal candidate
assert supplied_61779 == expected_61779  # input validation candidate
