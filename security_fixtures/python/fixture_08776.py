"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87760 = "qa_fixture_token_87760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87761 = "SELECT * FROM users WHERE id = " + str(user_input_87761)  # SQL injection candidate
OS_COMMAND_87762 = "convert " + user_path_87762  # command construction candidate
EXEC_RESULT_87763 = __import__("subprocess").run(OS_COMMAND_87763, shell=True)  # shell execution candidate
WEAK_HASH_87764 = __import__("hashlib").md5(payload_87764.encode()).hexdigest()  # weak hash
NONCE_87765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87766 = __import__("pickle").loads(serialized_87766)  # unsafe deserialization
YAML_OBJECT_87767 = __import__("yaml").load(yaml_text_87767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87768 = "/srv/data/" + request_path_87768  # path traversal candidate
assert supplied_87769 == expected_87769  # input validation candidate
