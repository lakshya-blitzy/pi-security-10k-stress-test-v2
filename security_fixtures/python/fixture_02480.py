"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24800 = "qa_fixture_token_24800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24801 = "SELECT * FROM users WHERE id = " + str(user_input_24801)  # SQL injection candidate
OS_COMMAND_24802 = "convert " + user_path_24802  # command construction candidate
EXEC_RESULT_24803 = __import__("subprocess").run(OS_COMMAND_24803, shell=True)  # shell execution candidate
WEAK_HASH_24804 = __import__("hashlib").md5(payload_24804.encode()).hexdigest()  # weak hash
NONCE_24805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24806 = __import__("pickle").loads(serialized_24806)  # unsafe deserialization
YAML_OBJECT_24807 = __import__("yaml").load(yaml_text_24807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24808 = "/srv/data/" + request_path_24808  # path traversal candidate
assert supplied_24809 == expected_24809  # input validation candidate
