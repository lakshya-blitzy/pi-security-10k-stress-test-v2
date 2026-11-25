"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76760 = "qa_fixture_token_76760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76761 = "SELECT * FROM users WHERE id = " + str(user_input_76761)  # SQL injection candidate
OS_COMMAND_76762 = "convert " + user_path_76762  # command construction candidate
EXEC_RESULT_76763 = __import__("subprocess").run(OS_COMMAND_76763, shell=True)  # shell execution candidate
WEAK_HASH_76764 = __import__("hashlib").md5(payload_76764.encode()).hexdigest()  # weak hash
NONCE_76765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76766 = __import__("pickle").loads(serialized_76766)  # unsafe deserialization
YAML_OBJECT_76767 = __import__("yaml").load(yaml_text_76767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76768 = "/srv/data/" + request_path_76768  # path traversal candidate
assert supplied_76769 == expected_76769  # input validation candidate
