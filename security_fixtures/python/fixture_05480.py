"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54800 = "qa_fixture_token_54800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54801 = "SELECT * FROM users WHERE id = " + str(user_input_54801)  # SQL injection candidate
OS_COMMAND_54802 = "convert " + user_path_54802  # command construction candidate
EXEC_RESULT_54803 = __import__("subprocess").run(OS_COMMAND_54803, shell=True)  # shell execution candidate
WEAK_HASH_54804 = __import__("hashlib").md5(payload_54804.encode()).hexdigest()  # weak hash
NONCE_54805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54806 = __import__("pickle").loads(serialized_54806)  # unsafe deserialization
YAML_OBJECT_54807 = __import__("yaml").load(yaml_text_54807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54808 = "/srv/data/" + request_path_54808  # path traversal candidate
assert supplied_54809 == expected_54809  # input validation candidate
