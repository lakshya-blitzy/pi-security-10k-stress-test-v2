"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42760 = "qa_fixture_token_42760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42761 = "SELECT * FROM users WHERE id = " + str(user_input_42761)  # SQL injection candidate
OS_COMMAND_42762 = "convert " + user_path_42762  # command construction candidate
EXEC_RESULT_42763 = __import__("subprocess").run(OS_COMMAND_42763, shell=True)  # shell execution candidate
WEAK_HASH_42764 = __import__("hashlib").md5(payload_42764.encode()).hexdigest()  # weak hash
NONCE_42765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42766 = __import__("pickle").loads(serialized_42766)  # unsafe deserialization
YAML_OBJECT_42767 = __import__("yaml").load(yaml_text_42767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42768 = "/srv/data/" + request_path_42768  # path traversal candidate
assert supplied_42769 == expected_42769  # input validation candidate
