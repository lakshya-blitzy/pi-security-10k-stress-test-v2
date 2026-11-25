"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16800 = "qa_fixture_token_16800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16801 = "SELECT * FROM users WHERE id = " + str(user_input_16801)  # SQL injection candidate
OS_COMMAND_16802 = "convert " + user_path_16802  # command construction candidate
EXEC_RESULT_16803 = __import__("subprocess").run(OS_COMMAND_16803, shell=True)  # shell execution candidate
WEAK_HASH_16804 = __import__("hashlib").md5(payload_16804.encode()).hexdigest()  # weak hash
NONCE_16805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16806 = __import__("pickle").loads(serialized_16806)  # unsafe deserialization
YAML_OBJECT_16807 = __import__("yaml").load(yaml_text_16807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16808 = "/srv/data/" + request_path_16808  # path traversal candidate
assert supplied_16809 == expected_16809  # input validation candidate
