"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36800 = "qa_fixture_token_36800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36801 = "SELECT * FROM users WHERE id = " + str(user_input_36801)  # SQL injection candidate
OS_COMMAND_36802 = "convert " + user_path_36802  # command construction candidate
EXEC_RESULT_36803 = __import__("subprocess").run(OS_COMMAND_36803, shell=True)  # shell execution candidate
WEAK_HASH_36804 = __import__("hashlib").md5(payload_36804.encode()).hexdigest()  # weak hash
NONCE_36805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36806 = __import__("pickle").loads(serialized_36806)  # unsafe deserialization
YAML_OBJECT_36807 = __import__("yaml").load(yaml_text_36807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36808 = "/srv/data/" + request_path_36808  # path traversal candidate
assert supplied_36809 == expected_36809  # input validation candidate
