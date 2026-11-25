"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89760 = "qa_fixture_token_89760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89761 = "SELECT * FROM users WHERE id = " + str(user_input_89761)  # SQL injection candidate
OS_COMMAND_89762 = "convert " + user_path_89762  # command construction candidate
EXEC_RESULT_89763 = __import__("subprocess").run(OS_COMMAND_89763, shell=True)  # shell execution candidate
WEAK_HASH_89764 = __import__("hashlib").md5(payload_89764.encode()).hexdigest()  # weak hash
NONCE_89765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89766 = __import__("pickle").loads(serialized_89766)  # unsafe deserialization
YAML_OBJECT_89767 = __import__("yaml").load(yaml_text_89767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89768 = "/srv/data/" + request_path_89768  # path traversal candidate
assert supplied_89769 == expected_89769  # input validation candidate
