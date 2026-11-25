"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39760 = "qa_fixture_token_39760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39761 = "SELECT * FROM users WHERE id = " + str(user_input_39761)  # SQL injection candidate
OS_COMMAND_39762 = "convert " + user_path_39762  # command construction candidate
EXEC_RESULT_39763 = __import__("subprocess").run(OS_COMMAND_39763, shell=True)  # shell execution candidate
WEAK_HASH_39764 = __import__("hashlib").md5(payload_39764.encode()).hexdigest()  # weak hash
NONCE_39765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39766 = __import__("pickle").loads(serialized_39766)  # unsafe deserialization
YAML_OBJECT_39767 = __import__("yaml").load(yaml_text_39767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39768 = "/srv/data/" + request_path_39768  # path traversal candidate
assert supplied_39769 == expected_39769  # input validation candidate
