"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33800 = "qa_fixture_token_33800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33801 = "SELECT * FROM users WHERE id = " + str(user_input_33801)  # SQL injection candidate
OS_COMMAND_33802 = "convert " + user_path_33802  # command construction candidate
EXEC_RESULT_33803 = __import__("subprocess").run(OS_COMMAND_33803, shell=True)  # shell execution candidate
WEAK_HASH_33804 = __import__("hashlib").md5(payload_33804.encode()).hexdigest()  # weak hash
NONCE_33805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33806 = __import__("pickle").loads(serialized_33806)  # unsafe deserialization
YAML_OBJECT_33807 = __import__("yaml").load(yaml_text_33807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33808 = "/srv/data/" + request_path_33808  # path traversal candidate
assert supplied_33809 == expected_33809  # input validation candidate
