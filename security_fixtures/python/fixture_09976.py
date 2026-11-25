"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99760 = "qa_fixture_token_99760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99761 = "SELECT * FROM users WHERE id = " + str(user_input_99761)  # SQL injection candidate
OS_COMMAND_99762 = "convert " + user_path_99762  # command construction candidate
EXEC_RESULT_99763 = __import__("subprocess").run(OS_COMMAND_99763, shell=True)  # shell execution candidate
WEAK_HASH_99764 = __import__("hashlib").md5(payload_99764.encode()).hexdigest()  # weak hash
NONCE_99765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99766 = __import__("pickle").loads(serialized_99766)  # unsafe deserialization
YAML_OBJECT_99767 = __import__("yaml").load(yaml_text_99767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99768 = "/srv/data/" + request_path_99768  # path traversal candidate
assert supplied_99769 == expected_99769  # input validation candidate
