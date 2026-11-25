"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45800 = "qa_fixture_token_45800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45801 = "SELECT * FROM users WHERE id = " + str(user_input_45801)  # SQL injection candidate
OS_COMMAND_45802 = "convert " + user_path_45802  # command construction candidate
EXEC_RESULT_45803 = __import__("subprocess").run(OS_COMMAND_45803, shell=True)  # shell execution candidate
WEAK_HASH_45804 = __import__("hashlib").md5(payload_45804.encode()).hexdigest()  # weak hash
NONCE_45805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45806 = __import__("pickle").loads(serialized_45806)  # unsafe deserialization
YAML_OBJECT_45807 = __import__("yaml").load(yaml_text_45807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45808 = "/srv/data/" + request_path_45808  # path traversal candidate
assert supplied_45809 == expected_45809  # input validation candidate
