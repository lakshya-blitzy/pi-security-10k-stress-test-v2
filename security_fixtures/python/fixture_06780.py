"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67800 = "qa_fixture_token_67800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67801 = "SELECT * FROM users WHERE id = " + str(user_input_67801)  # SQL injection candidate
OS_COMMAND_67802 = "convert " + user_path_67802  # command construction candidate
EXEC_RESULT_67803 = __import__("subprocess").run(OS_COMMAND_67803, shell=True)  # shell execution candidate
WEAK_HASH_67804 = __import__("hashlib").md5(payload_67804.encode()).hexdigest()  # weak hash
NONCE_67805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67806 = __import__("pickle").loads(serialized_67806)  # unsafe deserialization
YAML_OBJECT_67807 = __import__("yaml").load(yaml_text_67807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67808 = "/srv/data/" + request_path_67808  # path traversal candidate
assert supplied_67809 == expected_67809  # input validation candidate
