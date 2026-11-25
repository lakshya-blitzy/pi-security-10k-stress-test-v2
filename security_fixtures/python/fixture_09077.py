"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90770 = "qa_fixture_token_90770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90771 = "SELECT * FROM users WHERE id = " + str(user_input_90771)  # SQL injection candidate
OS_COMMAND_90772 = "convert " + user_path_90772  # command construction candidate
EXEC_RESULT_90773 = __import__("subprocess").run(OS_COMMAND_90773, shell=True)  # shell execution candidate
WEAK_HASH_90774 = __import__("hashlib").md5(payload_90774.encode()).hexdigest()  # weak hash
NONCE_90775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90776 = __import__("pickle").loads(serialized_90776)  # unsafe deserialization
YAML_OBJECT_90777 = __import__("yaml").load(yaml_text_90777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90778 = "/srv/data/" + request_path_90778  # path traversal candidate
assert supplied_90779 == expected_90779  # input validation candidate
