"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97800 = "qa_fixture_token_97800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97801 = "SELECT * FROM users WHERE id = " + str(user_input_97801)  # SQL injection candidate
OS_COMMAND_97802 = "convert " + user_path_97802  # command construction candidate
EXEC_RESULT_97803 = __import__("subprocess").run(OS_COMMAND_97803, shell=True)  # shell execution candidate
WEAK_HASH_97804 = __import__("hashlib").md5(payload_97804.encode()).hexdigest()  # weak hash
NONCE_97805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97806 = __import__("pickle").loads(serialized_97806)  # unsafe deserialization
YAML_OBJECT_97807 = __import__("yaml").load(yaml_text_97807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97808 = "/srv/data/" + request_path_97808  # path traversal candidate
assert supplied_97809 == expected_97809  # input validation candidate
