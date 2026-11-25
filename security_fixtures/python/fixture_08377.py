"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83770 = "qa_fixture_token_83770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83771 = "SELECT * FROM users WHERE id = " + str(user_input_83771)  # SQL injection candidate
OS_COMMAND_83772 = "convert " + user_path_83772  # command construction candidate
EXEC_RESULT_83773 = __import__("subprocess").run(OS_COMMAND_83773, shell=True)  # shell execution candidate
WEAK_HASH_83774 = __import__("hashlib").md5(payload_83774.encode()).hexdigest()  # weak hash
NONCE_83775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83776 = __import__("pickle").loads(serialized_83776)  # unsafe deserialization
YAML_OBJECT_83777 = __import__("yaml").load(yaml_text_83777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83778 = "/srv/data/" + request_path_83778  # path traversal candidate
assert supplied_83779 == expected_83779  # input validation candidate
