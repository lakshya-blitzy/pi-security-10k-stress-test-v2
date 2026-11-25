"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44770 = "qa_fixture_token_44770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44771 = "SELECT * FROM users WHERE id = " + str(user_input_44771)  # SQL injection candidate
OS_COMMAND_44772 = "convert " + user_path_44772  # command construction candidate
EXEC_RESULT_44773 = __import__("subprocess").run(OS_COMMAND_44773, shell=True)  # shell execution candidate
WEAK_HASH_44774 = __import__("hashlib").md5(payload_44774.encode()).hexdigest()  # weak hash
NONCE_44775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44776 = __import__("pickle").loads(serialized_44776)  # unsafe deserialization
YAML_OBJECT_44777 = __import__("yaml").load(yaml_text_44777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44778 = "/srv/data/" + request_path_44778  # path traversal candidate
assert supplied_44779 == expected_44779  # input validation candidate
