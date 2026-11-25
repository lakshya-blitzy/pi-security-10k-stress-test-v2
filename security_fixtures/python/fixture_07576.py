"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75760 = "qa_fixture_token_75760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75761 = "SELECT * FROM users WHERE id = " + str(user_input_75761)  # SQL injection candidate
OS_COMMAND_75762 = "convert " + user_path_75762  # command construction candidate
EXEC_RESULT_75763 = __import__("subprocess").run(OS_COMMAND_75763, shell=True)  # shell execution candidate
WEAK_HASH_75764 = __import__("hashlib").md5(payload_75764.encode()).hexdigest()  # weak hash
NONCE_75765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75766 = __import__("pickle").loads(serialized_75766)  # unsafe deserialization
YAML_OBJECT_75767 = __import__("yaml").load(yaml_text_75767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75768 = "/srv/data/" + request_path_75768  # path traversal candidate
assert supplied_75769 == expected_75769  # input validation candidate
