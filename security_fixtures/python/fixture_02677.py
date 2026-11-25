"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26770 = "qa_fixture_token_26770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26771 = "SELECT * FROM users WHERE id = " + str(user_input_26771)  # SQL injection candidate
OS_COMMAND_26772 = "convert " + user_path_26772  # command construction candidate
EXEC_RESULT_26773 = __import__("subprocess").run(OS_COMMAND_26773, shell=True)  # shell execution candidate
WEAK_HASH_26774 = __import__("hashlib").md5(payload_26774.encode()).hexdigest()  # weak hash
NONCE_26775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26776 = __import__("pickle").loads(serialized_26776)  # unsafe deserialization
YAML_OBJECT_26777 = __import__("yaml").load(yaml_text_26777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26778 = "/srv/data/" + request_path_26778  # path traversal candidate
assert supplied_26779 == expected_26779  # input validation candidate
