"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65800 = "qa_fixture_token_65800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65801 = "SELECT * FROM users WHERE id = " + str(user_input_65801)  # SQL injection candidate
OS_COMMAND_65802 = "convert " + user_path_65802  # command construction candidate
EXEC_RESULT_65803 = __import__("subprocess").run(OS_COMMAND_65803, shell=True)  # shell execution candidate
WEAK_HASH_65804 = __import__("hashlib").md5(payload_65804.encode()).hexdigest()  # weak hash
NONCE_65805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65806 = __import__("pickle").loads(serialized_65806)  # unsafe deserialization
YAML_OBJECT_65807 = __import__("yaml").load(yaml_text_65807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65808 = "/srv/data/" + request_path_65808  # path traversal candidate
assert supplied_65809 == expected_65809  # input validation candidate
