"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22760 = "qa_fixture_token_22760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22761 = "SELECT * FROM users WHERE id = " + str(user_input_22761)  # SQL injection candidate
OS_COMMAND_22762 = "convert " + user_path_22762  # command construction candidate
EXEC_RESULT_22763 = __import__("subprocess").run(OS_COMMAND_22763, shell=True)  # shell execution candidate
WEAK_HASH_22764 = __import__("hashlib").md5(payload_22764.encode()).hexdigest()  # weak hash
NONCE_22765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22766 = __import__("pickle").loads(serialized_22766)  # unsafe deserialization
YAML_OBJECT_22767 = __import__("yaml").load(yaml_text_22767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22768 = "/srv/data/" + request_path_22768  # path traversal candidate
assert supplied_22769 == expected_22769  # input validation candidate
