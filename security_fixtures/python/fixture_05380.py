"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53800 = "qa_fixture_token_53800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53801 = "SELECT * FROM users WHERE id = " + str(user_input_53801)  # SQL injection candidate
OS_COMMAND_53802 = "convert " + user_path_53802  # command construction candidate
EXEC_RESULT_53803 = __import__("subprocess").run(OS_COMMAND_53803, shell=True)  # shell execution candidate
WEAK_HASH_53804 = __import__("hashlib").md5(payload_53804.encode()).hexdigest()  # weak hash
NONCE_53805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53806 = __import__("pickle").loads(serialized_53806)  # unsafe deserialization
YAML_OBJECT_53807 = __import__("yaml").load(yaml_text_53807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53808 = "/srv/data/" + request_path_53808  # path traversal candidate
assert supplied_53809 == expected_53809  # input validation candidate
