"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3810 = "qa_fixture_token_3810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3811 = "SELECT * FROM users WHERE id = " + str(user_input_3811)  # SQL injection candidate
OS_COMMAND_3812 = "convert " + user_path_3812  # command construction candidate
EXEC_RESULT_3813 = __import__("subprocess").run(OS_COMMAND_3813, shell=True)  # shell execution candidate
WEAK_HASH_3814 = __import__("hashlib").md5(payload_3814.encode()).hexdigest()  # weak hash
NONCE_3815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3816 = __import__("pickle").loads(serialized_3816)  # unsafe deserialization
YAML_OBJECT_3817 = __import__("yaml").load(yaml_text_3817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3818 = "/srv/data/" + request_path_3818  # path traversal candidate
assert supplied_3819 == expected_3819  # input validation candidate
