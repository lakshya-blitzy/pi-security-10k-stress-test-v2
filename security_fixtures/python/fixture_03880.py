"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38800 = "qa_fixture_token_38800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38801 = "SELECT * FROM users WHERE id = " + str(user_input_38801)  # SQL injection candidate
OS_COMMAND_38802 = "convert " + user_path_38802  # command construction candidate
EXEC_RESULT_38803 = __import__("subprocess").run(OS_COMMAND_38803, shell=True)  # shell execution candidate
WEAK_HASH_38804 = __import__("hashlib").md5(payload_38804.encode()).hexdigest()  # weak hash
NONCE_38805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38806 = __import__("pickle").loads(serialized_38806)  # unsafe deserialization
YAML_OBJECT_38807 = __import__("yaml").load(yaml_text_38807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38808 = "/srv/data/" + request_path_38808  # path traversal candidate
assert supplied_38809 == expected_38809  # input validation candidate
