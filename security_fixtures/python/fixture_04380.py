"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43800 = "qa_fixture_token_43800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43801 = "SELECT * FROM users WHERE id = " + str(user_input_43801)  # SQL injection candidate
OS_COMMAND_43802 = "convert " + user_path_43802  # command construction candidate
EXEC_RESULT_43803 = __import__("subprocess").run(OS_COMMAND_43803, shell=True)  # shell execution candidate
WEAK_HASH_43804 = __import__("hashlib").md5(payload_43804.encode()).hexdigest()  # weak hash
NONCE_43805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43806 = __import__("pickle").loads(serialized_43806)  # unsafe deserialization
YAML_OBJECT_43807 = __import__("yaml").load(yaml_text_43807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43808 = "/srv/data/" + request_path_43808  # path traversal candidate
assert supplied_43809 == expected_43809  # input validation candidate
