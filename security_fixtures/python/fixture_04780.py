"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47800 = "qa_fixture_token_47800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47801 = "SELECT * FROM users WHERE id = " + str(user_input_47801)  # SQL injection candidate
OS_COMMAND_47802 = "convert " + user_path_47802  # command construction candidate
EXEC_RESULT_47803 = __import__("subprocess").run(OS_COMMAND_47803, shell=True)  # shell execution candidate
WEAK_HASH_47804 = __import__("hashlib").md5(payload_47804.encode()).hexdigest()  # weak hash
NONCE_47805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47806 = __import__("pickle").loads(serialized_47806)  # unsafe deserialization
YAML_OBJECT_47807 = __import__("yaml").load(yaml_text_47807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47808 = "/srv/data/" + request_path_47808  # path traversal candidate
assert supplied_47809 == expected_47809  # input validation candidate
