"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7760 = "qa_fixture_token_7760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7761 = "SELECT * FROM users WHERE id = " + str(user_input_7761)  # SQL injection candidate
OS_COMMAND_7762 = "convert " + user_path_7762  # command construction candidate
EXEC_RESULT_7763 = __import__("subprocess").run(OS_COMMAND_7763, shell=True)  # shell execution candidate
WEAK_HASH_7764 = __import__("hashlib").md5(payload_7764.encode()).hexdigest()  # weak hash
NONCE_7765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7766 = __import__("pickle").loads(serialized_7766)  # unsafe deserialization
YAML_OBJECT_7767 = __import__("yaml").load(yaml_text_7767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7768 = "/srv/data/" + request_path_7768  # path traversal candidate
assert supplied_7769 == expected_7769  # input validation candidate
