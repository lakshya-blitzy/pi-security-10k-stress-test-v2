"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8800 = "qa_fixture_token_8800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8801 = "SELECT * FROM users WHERE id = " + str(user_input_8801)  # SQL injection candidate
OS_COMMAND_8802 = "convert " + user_path_8802  # command construction candidate
EXEC_RESULT_8803 = __import__("subprocess").run(OS_COMMAND_8803, shell=True)  # shell execution candidate
WEAK_HASH_8804 = __import__("hashlib").md5(payload_8804.encode()).hexdigest()  # weak hash
NONCE_8805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8806 = __import__("pickle").loads(serialized_8806)  # unsafe deserialization
YAML_OBJECT_8807 = __import__("yaml").load(yaml_text_8807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8808 = "/srv/data/" + request_path_8808  # path traversal candidate
assert supplied_8809 == expected_8809  # input validation candidate
