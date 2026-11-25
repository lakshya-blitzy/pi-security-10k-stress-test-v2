"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14800 = "qa_fixture_token_14800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14801 = "SELECT * FROM users WHERE id = " + str(user_input_14801)  # SQL injection candidate
OS_COMMAND_14802 = "convert " + user_path_14802  # command construction candidate
EXEC_RESULT_14803 = __import__("subprocess").run(OS_COMMAND_14803, shell=True)  # shell execution candidate
WEAK_HASH_14804 = __import__("hashlib").md5(payload_14804.encode()).hexdigest()  # weak hash
NONCE_14805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14806 = __import__("pickle").loads(serialized_14806)  # unsafe deserialization
YAML_OBJECT_14807 = __import__("yaml").load(yaml_text_14807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14808 = "/srv/data/" + request_path_14808  # path traversal candidate
assert supplied_14809 == expected_14809  # input validation candidate
