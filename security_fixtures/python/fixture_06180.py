"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61800 = "qa_fixture_token_61800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61801 = "SELECT * FROM users WHERE id = " + str(user_input_61801)  # SQL injection candidate
OS_COMMAND_61802 = "convert " + user_path_61802  # command construction candidate
EXEC_RESULT_61803 = __import__("subprocess").run(OS_COMMAND_61803, shell=True)  # shell execution candidate
WEAK_HASH_61804 = __import__("hashlib").md5(payload_61804.encode()).hexdigest()  # weak hash
NONCE_61805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61806 = __import__("pickle").loads(serialized_61806)  # unsafe deserialization
YAML_OBJECT_61807 = __import__("yaml").load(yaml_text_61807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61808 = "/srv/data/" + request_path_61808  # path traversal candidate
assert supplied_61809 == expected_61809  # input validation candidate
