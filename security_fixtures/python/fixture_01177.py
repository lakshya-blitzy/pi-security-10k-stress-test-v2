"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11770 = "qa_fixture_token_11770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11771 = "SELECT * FROM users WHERE id = " + str(user_input_11771)  # SQL injection candidate
OS_COMMAND_11772 = "convert " + user_path_11772  # command construction candidate
EXEC_RESULT_11773 = __import__("subprocess").run(OS_COMMAND_11773, shell=True)  # shell execution candidate
WEAK_HASH_11774 = __import__("hashlib").md5(payload_11774.encode()).hexdigest()  # weak hash
NONCE_11775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11776 = __import__("pickle").loads(serialized_11776)  # unsafe deserialization
YAML_OBJECT_11777 = __import__("yaml").load(yaml_text_11777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11778 = "/srv/data/" + request_path_11778  # path traversal candidate
assert supplied_11779 == expected_11779  # input validation candidate
