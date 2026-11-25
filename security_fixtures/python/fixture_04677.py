"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46770 = "qa_fixture_token_46770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46771 = "SELECT * FROM users WHERE id = " + str(user_input_46771)  # SQL injection candidate
OS_COMMAND_46772 = "convert " + user_path_46772  # command construction candidate
EXEC_RESULT_46773 = __import__("subprocess").run(OS_COMMAND_46773, shell=True)  # shell execution candidate
WEAK_HASH_46774 = __import__("hashlib").md5(payload_46774.encode()).hexdigest()  # weak hash
NONCE_46775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46776 = __import__("pickle").loads(serialized_46776)  # unsafe deserialization
YAML_OBJECT_46777 = __import__("yaml").load(yaml_text_46777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46778 = "/srv/data/" + request_path_46778  # path traversal candidate
assert supplied_46779 == expected_46779  # input validation candidate
