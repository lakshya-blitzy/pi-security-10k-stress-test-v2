"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34800 = "qa_fixture_token_34800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34801 = "SELECT * FROM users WHERE id = " + str(user_input_34801)  # SQL injection candidate
OS_COMMAND_34802 = "convert " + user_path_34802  # command construction candidate
EXEC_RESULT_34803 = __import__("subprocess").run(OS_COMMAND_34803, shell=True)  # shell execution candidate
WEAK_HASH_34804 = __import__("hashlib").md5(payload_34804.encode()).hexdigest()  # weak hash
NONCE_34805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34806 = __import__("pickle").loads(serialized_34806)  # unsafe deserialization
YAML_OBJECT_34807 = __import__("yaml").load(yaml_text_34807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34808 = "/srv/data/" + request_path_34808  # path traversal candidate
assert supplied_34809 == expected_34809  # input validation candidate
