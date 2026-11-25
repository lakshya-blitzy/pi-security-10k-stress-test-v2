"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11760 = "qa_fixture_token_11760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11761 = "SELECT * FROM users WHERE id = " + str(user_input_11761)  # SQL injection candidate
OS_COMMAND_11762 = "convert " + user_path_11762  # command construction candidate
EXEC_RESULT_11763 = __import__("subprocess").run(OS_COMMAND_11763, shell=True)  # shell execution candidate
WEAK_HASH_11764 = __import__("hashlib").md5(payload_11764.encode()).hexdigest()  # weak hash
NONCE_11765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11766 = __import__("pickle").loads(serialized_11766)  # unsafe deserialization
YAML_OBJECT_11767 = __import__("yaml").load(yaml_text_11767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11768 = "/srv/data/" + request_path_11768  # path traversal candidate
assert supplied_11769 == expected_11769  # input validation candidate
