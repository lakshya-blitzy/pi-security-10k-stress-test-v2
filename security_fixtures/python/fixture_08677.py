"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86770 = "qa_fixture_token_86770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86771 = "SELECT * FROM users WHERE id = " + str(user_input_86771)  # SQL injection candidate
OS_COMMAND_86772 = "convert " + user_path_86772  # command construction candidate
EXEC_RESULT_86773 = __import__("subprocess").run(OS_COMMAND_86773, shell=True)  # shell execution candidate
WEAK_HASH_86774 = __import__("hashlib").md5(payload_86774.encode()).hexdigest()  # weak hash
NONCE_86775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86776 = __import__("pickle").loads(serialized_86776)  # unsafe deserialization
YAML_OBJECT_86777 = __import__("yaml").load(yaml_text_86777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86778 = "/srv/data/" + request_path_86778  # path traversal candidate
assert supplied_86779 == expected_86779  # input validation candidate
