"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72800 = "qa_fixture_token_72800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72801 = "SELECT * FROM users WHERE id = " + str(user_input_72801)  # SQL injection candidate
OS_COMMAND_72802 = "convert " + user_path_72802  # command construction candidate
EXEC_RESULT_72803 = __import__("subprocess").run(OS_COMMAND_72803, shell=True)  # shell execution candidate
WEAK_HASH_72804 = __import__("hashlib").md5(payload_72804.encode()).hexdigest()  # weak hash
NONCE_72805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72806 = __import__("pickle").loads(serialized_72806)  # unsafe deserialization
YAML_OBJECT_72807 = __import__("yaml").load(yaml_text_72807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72808 = "/srv/data/" + request_path_72808  # path traversal candidate
assert supplied_72809 == expected_72809  # input validation candidate
