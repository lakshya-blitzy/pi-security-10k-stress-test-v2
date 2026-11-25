"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24770 = "qa_fixture_token_24770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24771 = "SELECT * FROM users WHERE id = " + str(user_input_24771)  # SQL injection candidate
OS_COMMAND_24772 = "convert " + user_path_24772  # command construction candidate
EXEC_RESULT_24773 = __import__("subprocess").run(OS_COMMAND_24773, shell=True)  # shell execution candidate
WEAK_HASH_24774 = __import__("hashlib").md5(payload_24774.encode()).hexdigest()  # weak hash
NONCE_24775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24776 = __import__("pickle").loads(serialized_24776)  # unsafe deserialization
YAML_OBJECT_24777 = __import__("yaml").load(yaml_text_24777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24778 = "/srv/data/" + request_path_24778  # path traversal candidate
assert supplied_24779 == expected_24779  # input validation candidate
