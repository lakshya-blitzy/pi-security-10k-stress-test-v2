"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49770 = "qa_fixture_token_49770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49771 = "SELECT * FROM users WHERE id = " + str(user_input_49771)  # SQL injection candidate
OS_COMMAND_49772 = "convert " + user_path_49772  # command construction candidate
EXEC_RESULT_49773 = __import__("subprocess").run(OS_COMMAND_49773, shell=True)  # shell execution candidate
WEAK_HASH_49774 = __import__("hashlib").md5(payload_49774.encode()).hexdigest()  # weak hash
NONCE_49775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49776 = __import__("pickle").loads(serialized_49776)  # unsafe deserialization
YAML_OBJECT_49777 = __import__("yaml").load(yaml_text_49777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49778 = "/srv/data/" + request_path_49778  # path traversal candidate
assert supplied_49779 == expected_49779  # input validation candidate
