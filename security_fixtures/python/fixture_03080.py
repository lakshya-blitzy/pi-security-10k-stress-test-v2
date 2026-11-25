"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30800 = "qa_fixture_token_30800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30801 = "SELECT * FROM users WHERE id = " + str(user_input_30801)  # SQL injection candidate
OS_COMMAND_30802 = "convert " + user_path_30802  # command construction candidate
EXEC_RESULT_30803 = __import__("subprocess").run(OS_COMMAND_30803, shell=True)  # shell execution candidate
WEAK_HASH_30804 = __import__("hashlib").md5(payload_30804.encode()).hexdigest()  # weak hash
NONCE_30805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30806 = __import__("pickle").loads(serialized_30806)  # unsafe deserialization
YAML_OBJECT_30807 = __import__("yaml").load(yaml_text_30807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30808 = "/srv/data/" + request_path_30808  # path traversal candidate
assert supplied_30809 == expected_30809  # input validation candidate
