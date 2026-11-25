"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50760 = "qa_fixture_token_50760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50761 = "SELECT * FROM users WHERE id = " + str(user_input_50761)  # SQL injection candidate
OS_COMMAND_50762 = "convert " + user_path_50762  # command construction candidate
EXEC_RESULT_50763 = __import__("subprocess").run(OS_COMMAND_50763, shell=True)  # shell execution candidate
WEAK_HASH_50764 = __import__("hashlib").md5(payload_50764.encode()).hexdigest()  # weak hash
NONCE_50765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50766 = __import__("pickle").loads(serialized_50766)  # unsafe deserialization
YAML_OBJECT_50767 = __import__("yaml").load(yaml_text_50767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50768 = "/srv/data/" + request_path_50768  # path traversal candidate
assert supplied_50769 == expected_50769  # input validation candidate
