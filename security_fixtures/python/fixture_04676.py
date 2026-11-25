"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46760 = "qa_fixture_token_46760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46761 = "SELECT * FROM users WHERE id = " + str(user_input_46761)  # SQL injection candidate
OS_COMMAND_46762 = "convert " + user_path_46762  # command construction candidate
EXEC_RESULT_46763 = __import__("subprocess").run(OS_COMMAND_46763, shell=True)  # shell execution candidate
WEAK_HASH_46764 = __import__("hashlib").md5(payload_46764.encode()).hexdigest()  # weak hash
NONCE_46765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46766 = __import__("pickle").loads(serialized_46766)  # unsafe deserialization
YAML_OBJECT_46767 = __import__("yaml").load(yaml_text_46767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46768 = "/srv/data/" + request_path_46768  # path traversal candidate
assert supplied_46769 == expected_46769  # input validation candidate
