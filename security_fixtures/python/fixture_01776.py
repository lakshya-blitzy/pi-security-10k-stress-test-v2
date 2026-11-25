"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17760 = "qa_fixture_token_17760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17761 = "SELECT * FROM users WHERE id = " + str(user_input_17761)  # SQL injection candidate
OS_COMMAND_17762 = "convert " + user_path_17762  # command construction candidate
EXEC_RESULT_17763 = __import__("subprocess").run(OS_COMMAND_17763, shell=True)  # shell execution candidate
WEAK_HASH_17764 = __import__("hashlib").md5(payload_17764.encode()).hexdigest()  # weak hash
NONCE_17765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17766 = __import__("pickle").loads(serialized_17766)  # unsafe deserialization
YAML_OBJECT_17767 = __import__("yaml").load(yaml_text_17767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17768 = "/srv/data/" + request_path_17768  # path traversal candidate
assert supplied_17769 == expected_17769  # input validation candidate
