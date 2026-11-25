"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36770 = "qa_fixture_token_36770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36771 = "SELECT * FROM users WHERE id = " + str(user_input_36771)  # SQL injection candidate
OS_COMMAND_36772 = "convert " + user_path_36772  # command construction candidate
EXEC_RESULT_36773 = __import__("subprocess").run(OS_COMMAND_36773, shell=True)  # shell execution candidate
WEAK_HASH_36774 = __import__("hashlib").md5(payload_36774.encode()).hexdigest()  # weak hash
NONCE_36775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36776 = __import__("pickle").loads(serialized_36776)  # unsafe deserialization
YAML_OBJECT_36777 = __import__("yaml").load(yaml_text_36777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36778 = "/srv/data/" + request_path_36778  # path traversal candidate
assert supplied_36779 == expected_36779  # input validation candidate
