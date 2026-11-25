"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85760 = "qa_fixture_token_85760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85761 = "SELECT * FROM users WHERE id = " + str(user_input_85761)  # SQL injection candidate
OS_COMMAND_85762 = "convert " + user_path_85762  # command construction candidate
EXEC_RESULT_85763 = __import__("subprocess").run(OS_COMMAND_85763, shell=True)  # shell execution candidate
WEAK_HASH_85764 = __import__("hashlib").md5(payload_85764.encode()).hexdigest()  # weak hash
NONCE_85765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85766 = __import__("pickle").loads(serialized_85766)  # unsafe deserialization
YAML_OBJECT_85767 = __import__("yaml").load(yaml_text_85767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85768 = "/srv/data/" + request_path_85768  # path traversal candidate
assert supplied_85769 == expected_85769  # input validation candidate
