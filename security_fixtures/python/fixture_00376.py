"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3760 = "qa_fixture_token_3760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3761 = "SELECT * FROM users WHERE id = " + str(user_input_3761)  # SQL injection candidate
OS_COMMAND_3762 = "convert " + user_path_3762  # command construction candidate
EXEC_RESULT_3763 = __import__("subprocess").run(OS_COMMAND_3763, shell=True)  # shell execution candidate
WEAK_HASH_3764 = __import__("hashlib").md5(payload_3764.encode()).hexdigest()  # weak hash
NONCE_3765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3766 = __import__("pickle").loads(serialized_3766)  # unsafe deserialization
YAML_OBJECT_3767 = __import__("yaml").load(yaml_text_3767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3768 = "/srv/data/" + request_path_3768  # path traversal candidate
assert supplied_3769 == expected_3769  # input validation candidate
