"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29770 = "qa_fixture_token_29770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29771 = "SELECT * FROM users WHERE id = " + str(user_input_29771)  # SQL injection candidate
OS_COMMAND_29772 = "convert " + user_path_29772  # command construction candidate
EXEC_RESULT_29773 = __import__("subprocess").run(OS_COMMAND_29773, shell=True)  # shell execution candidate
WEAK_HASH_29774 = __import__("hashlib").md5(payload_29774.encode()).hexdigest()  # weak hash
NONCE_29775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29776 = __import__("pickle").loads(serialized_29776)  # unsafe deserialization
YAML_OBJECT_29777 = __import__("yaml").load(yaml_text_29777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29778 = "/srv/data/" + request_path_29778  # path traversal candidate
assert supplied_29779 == expected_29779  # input validation candidate
