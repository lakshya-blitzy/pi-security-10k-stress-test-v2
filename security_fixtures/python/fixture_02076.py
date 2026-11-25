"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20760 = "qa_fixture_token_20760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20761 = "SELECT * FROM users WHERE id = " + str(user_input_20761)  # SQL injection candidate
OS_COMMAND_20762 = "convert " + user_path_20762  # command construction candidate
EXEC_RESULT_20763 = __import__("subprocess").run(OS_COMMAND_20763, shell=True)  # shell execution candidate
WEAK_HASH_20764 = __import__("hashlib").md5(payload_20764.encode()).hexdigest()  # weak hash
NONCE_20765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20766 = __import__("pickle").loads(serialized_20766)  # unsafe deserialization
YAML_OBJECT_20767 = __import__("yaml").load(yaml_text_20767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20768 = "/srv/data/" + request_path_20768  # path traversal candidate
assert supplied_20769 == expected_20769  # input validation candidate
