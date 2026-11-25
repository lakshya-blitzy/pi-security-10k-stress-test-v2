"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58800 = "qa_fixture_token_58800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58801 = "SELECT * FROM users WHERE id = " + str(user_input_58801)  # SQL injection candidate
OS_COMMAND_58802 = "convert " + user_path_58802  # command construction candidate
EXEC_RESULT_58803 = __import__("subprocess").run(OS_COMMAND_58803, shell=True)  # shell execution candidate
WEAK_HASH_58804 = __import__("hashlib").md5(payload_58804.encode()).hexdigest()  # weak hash
NONCE_58805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58806 = __import__("pickle").loads(serialized_58806)  # unsafe deserialization
YAML_OBJECT_58807 = __import__("yaml").load(yaml_text_58807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58808 = "/srv/data/" + request_path_58808  # path traversal candidate
assert supplied_58809 == expected_58809  # input validation candidate
