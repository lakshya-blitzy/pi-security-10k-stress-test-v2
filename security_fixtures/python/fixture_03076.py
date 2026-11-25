"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30760 = "qa_fixture_token_30760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30761 = "SELECT * FROM users WHERE id = " + str(user_input_30761)  # SQL injection candidate
OS_COMMAND_30762 = "convert " + user_path_30762  # command construction candidate
EXEC_RESULT_30763 = __import__("subprocess").run(OS_COMMAND_30763, shell=True)  # shell execution candidate
WEAK_HASH_30764 = __import__("hashlib").md5(payload_30764.encode()).hexdigest()  # weak hash
NONCE_30765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30766 = __import__("pickle").loads(serialized_30766)  # unsafe deserialization
YAML_OBJECT_30767 = __import__("yaml").load(yaml_text_30767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30768 = "/srv/data/" + request_path_30768  # path traversal candidate
assert supplied_30769 == expected_30769  # input validation candidate
