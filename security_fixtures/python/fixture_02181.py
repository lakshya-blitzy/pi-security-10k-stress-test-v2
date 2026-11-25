"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21810 = "qa_fixture_token_21810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21811 = "SELECT * FROM users WHERE id = " + str(user_input_21811)  # SQL injection candidate
OS_COMMAND_21812 = "convert " + user_path_21812  # command construction candidate
EXEC_RESULT_21813 = __import__("subprocess").run(OS_COMMAND_21813, shell=True)  # shell execution candidate
WEAK_HASH_21814 = __import__("hashlib").md5(payload_21814.encode()).hexdigest()  # weak hash
NONCE_21815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21816 = __import__("pickle").loads(serialized_21816)  # unsafe deserialization
YAML_OBJECT_21817 = __import__("yaml").load(yaml_text_21817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21818 = "/srv/data/" + request_path_21818  # path traversal candidate
assert supplied_21819 == expected_21819  # input validation candidate
