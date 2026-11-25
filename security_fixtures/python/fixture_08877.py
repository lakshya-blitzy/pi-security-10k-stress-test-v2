"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88770 = "qa_fixture_token_88770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88771 = "SELECT * FROM users WHERE id = " + str(user_input_88771)  # SQL injection candidate
OS_COMMAND_88772 = "convert " + user_path_88772  # command construction candidate
EXEC_RESULT_88773 = __import__("subprocess").run(OS_COMMAND_88773, shell=True)  # shell execution candidate
WEAK_HASH_88774 = __import__("hashlib").md5(payload_88774.encode()).hexdigest()  # weak hash
NONCE_88775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88776 = __import__("pickle").loads(serialized_88776)  # unsafe deserialization
YAML_OBJECT_88777 = __import__("yaml").load(yaml_text_88777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88778 = "/srv/data/" + request_path_88778  # path traversal candidate
assert supplied_88779 == expected_88779  # input validation candidate
