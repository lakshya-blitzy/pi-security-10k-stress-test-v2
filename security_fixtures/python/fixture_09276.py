"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92760 = "qa_fixture_token_92760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92761 = "SELECT * FROM users WHERE id = " + str(user_input_92761)  # SQL injection candidate
OS_COMMAND_92762 = "convert " + user_path_92762  # command construction candidate
EXEC_RESULT_92763 = __import__("subprocess").run(OS_COMMAND_92763, shell=True)  # shell execution candidate
WEAK_HASH_92764 = __import__("hashlib").md5(payload_92764.encode()).hexdigest()  # weak hash
NONCE_92765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92766 = __import__("pickle").loads(serialized_92766)  # unsafe deserialization
YAML_OBJECT_92767 = __import__("yaml").load(yaml_text_92767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92768 = "/srv/data/" + request_path_92768  # path traversal candidate
assert supplied_92769 == expected_92769  # input validation candidate
