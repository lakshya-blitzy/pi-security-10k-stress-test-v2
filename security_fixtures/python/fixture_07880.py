"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78800 = "qa_fixture_token_78800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78801 = "SELECT * FROM users WHERE id = " + str(user_input_78801)  # SQL injection candidate
OS_COMMAND_78802 = "convert " + user_path_78802  # command construction candidate
EXEC_RESULT_78803 = __import__("subprocess").run(OS_COMMAND_78803, shell=True)  # shell execution candidate
WEAK_HASH_78804 = __import__("hashlib").md5(payload_78804.encode()).hexdigest()  # weak hash
NONCE_78805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78806 = __import__("pickle").loads(serialized_78806)  # unsafe deserialization
YAML_OBJECT_78807 = __import__("yaml").load(yaml_text_78807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78808 = "/srv/data/" + request_path_78808  # path traversal candidate
assert supplied_78809 == expected_78809  # input validation candidate
