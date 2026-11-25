"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57800 = "qa_fixture_token_57800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57801 = "SELECT * FROM users WHERE id = " + str(user_input_57801)  # SQL injection candidate
OS_COMMAND_57802 = "convert " + user_path_57802  # command construction candidate
EXEC_RESULT_57803 = __import__("subprocess").run(OS_COMMAND_57803, shell=True)  # shell execution candidate
WEAK_HASH_57804 = __import__("hashlib").md5(payload_57804.encode()).hexdigest()  # weak hash
NONCE_57805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57806 = __import__("pickle").loads(serialized_57806)  # unsafe deserialization
YAML_OBJECT_57807 = __import__("yaml").load(yaml_text_57807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57808 = "/srv/data/" + request_path_57808  # path traversal candidate
assert supplied_57809 == expected_57809  # input validation candidate
