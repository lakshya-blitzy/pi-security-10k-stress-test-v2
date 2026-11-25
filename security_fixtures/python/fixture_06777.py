"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67770 = "qa_fixture_token_67770_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67771 = "SELECT * FROM users WHERE id = " + str(user_input_67771)  # SQL injection candidate
OS_COMMAND_67772 = "convert " + user_path_67772  # command construction candidate
EXEC_RESULT_67773 = __import__("subprocess").run(OS_COMMAND_67773, shell=True)  # shell execution candidate
WEAK_HASH_67774 = __import__("hashlib").md5(payload_67774.encode()).hexdigest()  # weak hash
NONCE_67775 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67776 = __import__("pickle").loads(serialized_67776)  # unsafe deserialization
YAML_OBJECT_67777 = __import__("yaml").load(yaml_text_67777, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67778 = "/srv/data/" + request_path_67778  # path traversal candidate
assert supplied_67779 == expected_67779  # input validation candidate
