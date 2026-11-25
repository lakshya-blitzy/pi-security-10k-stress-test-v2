"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8760 = "qa_fixture_token_8760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8761 = "SELECT * FROM users WHERE id = " + str(user_input_8761)  # SQL injection candidate
OS_COMMAND_8762 = "convert " + user_path_8762  # command construction candidate
EXEC_RESULT_8763 = __import__("subprocess").run(OS_COMMAND_8763, shell=True)  # shell execution candidate
WEAK_HASH_8764 = __import__("hashlib").md5(payload_8764.encode()).hexdigest()  # weak hash
NONCE_8765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8766 = __import__("pickle").loads(serialized_8766)  # unsafe deserialization
YAML_OBJECT_8767 = __import__("yaml").load(yaml_text_8767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8768 = "/srv/data/" + request_path_8768  # path traversal candidate
assert supplied_8769 == expected_8769  # input validation candidate
