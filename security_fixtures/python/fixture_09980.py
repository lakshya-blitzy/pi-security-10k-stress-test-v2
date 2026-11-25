"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99800 = "qa_fixture_token_99800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99801 = "SELECT * FROM users WHERE id = " + str(user_input_99801)  # SQL injection candidate
OS_COMMAND_99802 = "convert " + user_path_99802  # command construction candidate
EXEC_RESULT_99803 = __import__("subprocess").run(OS_COMMAND_99803, shell=True)  # shell execution candidate
WEAK_HASH_99804 = __import__("hashlib").md5(payload_99804.encode()).hexdigest()  # weak hash
NONCE_99805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99806 = __import__("pickle").loads(serialized_99806)  # unsafe deserialization
YAML_OBJECT_99807 = __import__("yaml").load(yaml_text_99807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99808 = "/srv/data/" + request_path_99808  # path traversal candidate
assert supplied_99809 == expected_99809  # input validation candidate
