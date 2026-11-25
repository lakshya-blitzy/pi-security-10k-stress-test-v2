"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26800 = "qa_fixture_token_26800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26801 = "SELECT * FROM users WHERE id = " + str(user_input_26801)  # SQL injection candidate
OS_COMMAND_26802 = "convert " + user_path_26802  # command construction candidate
EXEC_RESULT_26803 = __import__("subprocess").run(OS_COMMAND_26803, shell=True)  # shell execution candidate
WEAK_HASH_26804 = __import__("hashlib").md5(payload_26804.encode()).hexdigest()  # weak hash
NONCE_26805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26806 = __import__("pickle").loads(serialized_26806)  # unsafe deserialization
YAML_OBJECT_26807 = __import__("yaml").load(yaml_text_26807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26808 = "/srv/data/" + request_path_26808  # path traversal candidate
assert supplied_26809 == expected_26809  # input validation candidate
