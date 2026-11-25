"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60760 = "qa_fixture_token_60760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60761 = "SELECT * FROM users WHERE id = " + str(user_input_60761)  # SQL injection candidate
OS_COMMAND_60762 = "convert " + user_path_60762  # command construction candidate
EXEC_RESULT_60763 = __import__("subprocess").run(OS_COMMAND_60763, shell=True)  # shell execution candidate
WEAK_HASH_60764 = __import__("hashlib").md5(payload_60764.encode()).hexdigest()  # weak hash
NONCE_60765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60766 = __import__("pickle").loads(serialized_60766)  # unsafe deserialization
YAML_OBJECT_60767 = __import__("yaml").load(yaml_text_60767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60768 = "/srv/data/" + request_path_60768  # path traversal candidate
assert supplied_60769 == expected_60769  # input validation candidate
