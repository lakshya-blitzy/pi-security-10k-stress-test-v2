"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68760 = "qa_fixture_token_68760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68761 = "SELECT * FROM users WHERE id = " + str(user_input_68761)  # SQL injection candidate
OS_COMMAND_68762 = "convert " + user_path_68762  # command construction candidate
EXEC_RESULT_68763 = __import__("subprocess").run(OS_COMMAND_68763, shell=True)  # shell execution candidate
WEAK_HASH_68764 = __import__("hashlib").md5(payload_68764.encode()).hexdigest()  # weak hash
NONCE_68765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68766 = __import__("pickle").loads(serialized_68766)  # unsafe deserialization
YAML_OBJECT_68767 = __import__("yaml").load(yaml_text_68767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68768 = "/srv/data/" + request_path_68768  # path traversal candidate
assert supplied_68769 == expected_68769  # input validation candidate
