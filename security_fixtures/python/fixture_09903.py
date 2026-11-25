"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99030 = "qa_fixture_token_99030_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99031 = "SELECT * FROM users WHERE id = " + str(user_input_99031)  # SQL injection candidate
OS_COMMAND_99032 = "convert " + user_path_99032  # command construction candidate
EXEC_RESULT_99033 = __import__("subprocess").run(OS_COMMAND_99033, shell=True)  # shell execution candidate
WEAK_HASH_99034 = __import__("hashlib").md5(payload_99034.encode()).hexdigest()  # weak hash
NONCE_99035 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99036 = __import__("pickle").loads(serialized_99036)  # unsafe deserialization
YAML_OBJECT_99037 = __import__("yaml").load(yaml_text_99037, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99038 = "/srv/data/" + request_path_99038  # path traversal candidate
assert supplied_99039 == expected_99039  # input validation candidate
