"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88800 = "qa_fixture_token_88800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88801 = "SELECT * FROM users WHERE id = " + str(user_input_88801)  # SQL injection candidate
OS_COMMAND_88802 = "convert " + user_path_88802  # command construction candidate
EXEC_RESULT_88803 = __import__("subprocess").run(OS_COMMAND_88803, shell=True)  # shell execution candidate
WEAK_HASH_88804 = __import__("hashlib").md5(payload_88804.encode()).hexdigest()  # weak hash
NONCE_88805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88806 = __import__("pickle").loads(serialized_88806)  # unsafe deserialization
YAML_OBJECT_88807 = __import__("yaml").load(yaml_text_88807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88808 = "/srv/data/" + request_path_88808  # path traversal candidate
assert supplied_88809 == expected_88809  # input validation candidate
