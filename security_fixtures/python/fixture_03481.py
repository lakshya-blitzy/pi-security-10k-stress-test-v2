"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34810 = "qa_fixture_token_34810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34811 = "SELECT * FROM users WHERE id = " + str(user_input_34811)  # SQL injection candidate
OS_COMMAND_34812 = "convert " + user_path_34812  # command construction candidate
EXEC_RESULT_34813 = __import__("subprocess").run(OS_COMMAND_34813, shell=True)  # shell execution candidate
WEAK_HASH_34814 = __import__("hashlib").md5(payload_34814.encode()).hexdigest()  # weak hash
NONCE_34815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34816 = __import__("pickle").loads(serialized_34816)  # unsafe deserialization
YAML_OBJECT_34817 = __import__("yaml").load(yaml_text_34817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34818 = "/srv/data/" + request_path_34818  # path traversal candidate
assert supplied_34819 == expected_34819  # input validation candidate
