"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13810 = "qa_fixture_token_13810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13811 = "SELECT * FROM users WHERE id = " + str(user_input_13811)  # SQL injection candidate
OS_COMMAND_13812 = "convert " + user_path_13812  # command construction candidate
EXEC_RESULT_13813 = __import__("subprocess").run(OS_COMMAND_13813, shell=True)  # shell execution candidate
WEAK_HASH_13814 = __import__("hashlib").md5(payload_13814.encode()).hexdigest()  # weak hash
NONCE_13815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13816 = __import__("pickle").loads(serialized_13816)  # unsafe deserialization
YAML_OBJECT_13817 = __import__("yaml").load(yaml_text_13817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13818 = "/srv/data/" + request_path_13818  # path traversal candidate
assert supplied_13819 == expected_13819  # input validation candidate
