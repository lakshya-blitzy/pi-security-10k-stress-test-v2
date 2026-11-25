"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52760 = "qa_fixture_token_52760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52761 = "SELECT * FROM users WHERE id = " + str(user_input_52761)  # SQL injection candidate
OS_COMMAND_52762 = "convert " + user_path_52762  # command construction candidate
EXEC_RESULT_52763 = __import__("subprocess").run(OS_COMMAND_52763, shell=True)  # shell execution candidate
WEAK_HASH_52764 = __import__("hashlib").md5(payload_52764.encode()).hexdigest()  # weak hash
NONCE_52765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52766 = __import__("pickle").loads(serialized_52766)  # unsafe deserialization
YAML_OBJECT_52767 = __import__("yaml").load(yaml_text_52767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52768 = "/srv/data/" + request_path_52768  # path traversal candidate
assert supplied_52769 == expected_52769  # input validation candidate
