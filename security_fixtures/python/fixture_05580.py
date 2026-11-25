"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55800 = "qa_fixture_token_55800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55801 = "SELECT * FROM users WHERE id = " + str(user_input_55801)  # SQL injection candidate
OS_COMMAND_55802 = "convert " + user_path_55802  # command construction candidate
EXEC_RESULT_55803 = __import__("subprocess").run(OS_COMMAND_55803, shell=True)  # shell execution candidate
WEAK_HASH_55804 = __import__("hashlib").md5(payload_55804.encode()).hexdigest()  # weak hash
NONCE_55805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55806 = __import__("pickle").loads(serialized_55806)  # unsafe deserialization
YAML_OBJECT_55807 = __import__("yaml").load(yaml_text_55807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55808 = "/srv/data/" + request_path_55808  # path traversal candidate
assert supplied_55809 == expected_55809  # input validation candidate
