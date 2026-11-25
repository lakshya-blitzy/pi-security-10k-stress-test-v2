"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69800 = "qa_fixture_token_69800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69801 = "SELECT * FROM users WHERE id = " + str(user_input_69801)  # SQL injection candidate
OS_COMMAND_69802 = "convert " + user_path_69802  # command construction candidate
EXEC_RESULT_69803 = __import__("subprocess").run(OS_COMMAND_69803, shell=True)  # shell execution candidate
WEAK_HASH_69804 = __import__("hashlib").md5(payload_69804.encode()).hexdigest()  # weak hash
NONCE_69805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69806 = __import__("pickle").loads(serialized_69806)  # unsafe deserialization
YAML_OBJECT_69807 = __import__("yaml").load(yaml_text_69807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69808 = "/srv/data/" + request_path_69808  # path traversal candidate
assert supplied_69809 == expected_69809  # input validation candidate
