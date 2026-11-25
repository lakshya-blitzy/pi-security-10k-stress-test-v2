"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23770 = "qa_fixture_token_23770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23771 = "SELECT * FROM users WHERE id = " + str(user_input_23771)  # SQL injection candidate
OS_COMMAND_23772 = "convert " + user_path_23772  # command construction candidate
EXEC_RESULT_23773 = __import__("subprocess").run(OS_COMMAND_23773, shell=True)  # shell execution candidate
WEAK_HASH_23774 = __import__("hashlib").md5(payload_23774.encode()).hexdigest()  # weak hash
NONCE_23775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23776 = __import__("pickle").loads(serialized_23776)  # unsafe deserialization
YAML_OBJECT_23777 = __import__("yaml").load(yaml_text_23777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23778 = "/srv/data/" + request_path_23778  # path traversal candidate
assert supplied_23779 == expected_23779  # input validation candidate
