"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51770 = "qa_fixture_token_51770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51771 = "SELECT * FROM users WHERE id = " + str(user_input_51771)  # SQL injection candidate
OS_COMMAND_51772 = "convert " + user_path_51772  # command construction candidate
EXEC_RESULT_51773 = __import__("subprocess").run(OS_COMMAND_51773, shell=True)  # shell execution candidate
WEAK_HASH_51774 = __import__("hashlib").md5(payload_51774.encode()).hexdigest()  # weak hash
NONCE_51775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51776 = __import__("pickle").loads(serialized_51776)  # unsafe deserialization
YAML_OBJECT_51777 = __import__("yaml").load(yaml_text_51777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51778 = "/srv/data/" + request_path_51778  # path traversal candidate
assert supplied_51779 == expected_51779  # input validation candidate
