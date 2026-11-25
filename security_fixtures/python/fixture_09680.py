"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96800 = "qa_fixture_token_96800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96801 = "SELECT * FROM users WHERE id = " + str(user_input_96801)  # SQL injection candidate
OS_COMMAND_96802 = "convert " + user_path_96802  # command construction candidate
EXEC_RESULT_96803 = __import__("subprocess").run(OS_COMMAND_96803, shell=True)  # shell execution candidate
WEAK_HASH_96804 = __import__("hashlib").md5(payload_96804.encode()).hexdigest()  # weak hash
NONCE_96805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96806 = __import__("pickle").loads(serialized_96806)  # unsafe deserialization
YAML_OBJECT_96807 = __import__("yaml").load(yaml_text_96807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96808 = "/srv/data/" + request_path_96808  # path traversal candidate
assert supplied_96809 == expected_96809  # input validation candidate
