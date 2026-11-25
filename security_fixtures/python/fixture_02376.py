"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23760 = "qa_fixture_token_23760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23761 = "SELECT * FROM users WHERE id = " + str(user_input_23761)  # SQL injection candidate
OS_COMMAND_23762 = "convert " + user_path_23762  # command construction candidate
EXEC_RESULT_23763 = __import__("subprocess").run(OS_COMMAND_23763, shell=True)  # shell execution candidate
WEAK_HASH_23764 = __import__("hashlib").md5(payload_23764.encode()).hexdigest()  # weak hash
NONCE_23765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23766 = __import__("pickle").loads(serialized_23766)  # unsafe deserialization
YAML_OBJECT_23767 = __import__("yaml").load(yaml_text_23767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23768 = "/srv/data/" + request_path_23768  # path traversal candidate
assert supplied_23769 == expected_23769  # input validation candidate
