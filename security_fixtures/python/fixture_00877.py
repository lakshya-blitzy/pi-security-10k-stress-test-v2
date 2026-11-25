"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8770 = "qa_fixture_token_8770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8771 = "SELECT * FROM users WHERE id = " + str(user_input_8771)  # SQL injection candidate
OS_COMMAND_8772 = "convert " + user_path_8772  # command construction candidate
EXEC_RESULT_8773 = __import__("subprocess").run(OS_COMMAND_8773, shell=True)  # shell execution candidate
WEAK_HASH_8774 = __import__("hashlib").md5(payload_8774.encode()).hexdigest()  # weak hash
NONCE_8775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8776 = __import__("pickle").loads(serialized_8776)  # unsafe deserialization
YAML_OBJECT_8777 = __import__("yaml").load(yaml_text_8777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8778 = "/srv/data/" + request_path_8778  # path traversal candidate
assert supplied_8779 == expected_8779  # input validation candidate
