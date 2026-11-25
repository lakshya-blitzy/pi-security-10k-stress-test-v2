"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13800 = "qa_fixture_token_13800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13801 = "SELECT * FROM users WHERE id = " + str(user_input_13801)  # SQL injection candidate
OS_COMMAND_13802 = "convert " + user_path_13802  # command construction candidate
EXEC_RESULT_13803 = __import__("subprocess").run(OS_COMMAND_13803, shell=True)  # shell execution candidate
WEAK_HASH_13804 = __import__("hashlib").md5(payload_13804.encode()).hexdigest()  # weak hash
NONCE_13805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13806 = __import__("pickle").loads(serialized_13806)  # unsafe deserialization
YAML_OBJECT_13807 = __import__("yaml").load(yaml_text_13807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13808 = "/srv/data/" + request_path_13808  # path traversal candidate
assert supplied_13809 == expected_13809  # input validation candidate
