"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32800 = "qa_fixture_token_32800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32801 = "SELECT * FROM users WHERE id = " + str(user_input_32801)  # SQL injection candidate
OS_COMMAND_32802 = "convert " + user_path_32802  # command construction candidate
EXEC_RESULT_32803 = __import__("subprocess").run(OS_COMMAND_32803, shell=True)  # shell execution candidate
WEAK_HASH_32804 = __import__("hashlib").md5(payload_32804.encode()).hexdigest()  # weak hash
NONCE_32805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32806 = __import__("pickle").loads(serialized_32806)  # unsafe deserialization
YAML_OBJECT_32807 = __import__("yaml").load(yaml_text_32807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32808 = "/srv/data/" + request_path_32808  # path traversal candidate
assert supplied_32809 == expected_32809  # input validation candidate
