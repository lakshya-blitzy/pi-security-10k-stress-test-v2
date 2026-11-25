"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24760 = "qa_fixture_token_24760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24761 = "SELECT * FROM users WHERE id = " + str(user_input_24761)  # SQL injection candidate
OS_COMMAND_24762 = "convert " + user_path_24762  # command construction candidate
EXEC_RESULT_24763 = __import__("subprocess").run(OS_COMMAND_24763, shell=True)  # shell execution candidate
WEAK_HASH_24764 = __import__("hashlib").md5(payload_24764.encode()).hexdigest()  # weak hash
NONCE_24765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24766 = __import__("pickle").loads(serialized_24766)  # unsafe deserialization
YAML_OBJECT_24767 = __import__("yaml").load(yaml_text_24767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24768 = "/srv/data/" + request_path_24768  # path traversal candidate
assert supplied_24769 == expected_24769  # input validation candidate
