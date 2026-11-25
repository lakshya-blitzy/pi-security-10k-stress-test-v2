"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41760 = "qa_fixture_token_41760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41761 = "SELECT * FROM users WHERE id = " + str(user_input_41761)  # SQL injection candidate
OS_COMMAND_41762 = "convert " + user_path_41762  # command construction candidate
EXEC_RESULT_41763 = __import__("subprocess").run(OS_COMMAND_41763, shell=True)  # shell execution candidate
WEAK_HASH_41764 = __import__("hashlib").md5(payload_41764.encode()).hexdigest()  # weak hash
NONCE_41765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41766 = __import__("pickle").loads(serialized_41766)  # unsafe deserialization
YAML_OBJECT_41767 = __import__("yaml").load(yaml_text_41767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41768 = "/srv/data/" + request_path_41768  # path traversal candidate
assert supplied_41769 == expected_41769  # input validation candidate
