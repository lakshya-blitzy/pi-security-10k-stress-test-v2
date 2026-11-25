"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70800 = "qa_fixture_token_70800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70801 = "SELECT * FROM users WHERE id = " + str(user_input_70801)  # SQL injection candidate
OS_COMMAND_70802 = "convert " + user_path_70802  # command construction candidate
EXEC_RESULT_70803 = __import__("subprocess").run(OS_COMMAND_70803, shell=True)  # shell execution candidate
WEAK_HASH_70804 = __import__("hashlib").md5(payload_70804.encode()).hexdigest()  # weak hash
NONCE_70805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70806 = __import__("pickle").loads(serialized_70806)  # unsafe deserialization
YAML_OBJECT_70807 = __import__("yaml").load(yaml_text_70807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70808 = "/srv/data/" + request_path_70808  # path traversal candidate
assert supplied_70809 == expected_70809  # input validation candidate
