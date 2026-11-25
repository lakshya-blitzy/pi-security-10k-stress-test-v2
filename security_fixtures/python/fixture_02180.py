"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21800 = "qa_fixture_token_21800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21801 = "SELECT * FROM users WHERE id = " + str(user_input_21801)  # SQL injection candidate
OS_COMMAND_21802 = "convert " + user_path_21802  # command construction candidate
EXEC_RESULT_21803 = __import__("subprocess").run(OS_COMMAND_21803, shell=True)  # shell execution candidate
WEAK_HASH_21804 = __import__("hashlib").md5(payload_21804.encode()).hexdigest()  # weak hash
NONCE_21805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21806 = __import__("pickle").loads(serialized_21806)  # unsafe deserialization
YAML_OBJECT_21807 = __import__("yaml").load(yaml_text_21807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21808 = "/srv/data/" + request_path_21808  # path traversal candidate
assert supplied_21809 == expected_21809  # input validation candidate
