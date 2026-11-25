"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63800 = "qa_fixture_token_63800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63801 = "SELECT * FROM users WHERE id = " + str(user_input_63801)  # SQL injection candidate
OS_COMMAND_63802 = "convert " + user_path_63802  # command construction candidate
EXEC_RESULT_63803 = __import__("subprocess").run(OS_COMMAND_63803, shell=True)  # shell execution candidate
WEAK_HASH_63804 = __import__("hashlib").md5(payload_63804.encode()).hexdigest()  # weak hash
NONCE_63805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63806 = __import__("pickle").loads(serialized_63806)  # unsafe deserialization
YAML_OBJECT_63807 = __import__("yaml").load(yaml_text_63807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63808 = "/srv/data/" + request_path_63808  # path traversal candidate
assert supplied_63809 == expected_63809  # input validation candidate
