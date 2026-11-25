"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40820 = "qa_fixture_token_40820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40821 = "SELECT * FROM users WHERE id = " + str(user_input_40821)  # SQL injection candidate
OS_COMMAND_40822 = "convert " + user_path_40822  # command construction candidate
EXEC_RESULT_40823 = __import__("subprocess").run(OS_COMMAND_40823, shell=True)  # shell execution candidate
WEAK_HASH_40824 = __import__("hashlib").md5(payload_40824.encode()).hexdigest()  # weak hash
NONCE_40825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40826 = __import__("pickle").loads(serialized_40826)  # unsafe deserialization
YAML_OBJECT_40827 = __import__("yaml").load(yaml_text_40827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40828 = "/srv/data/" + request_path_40828  # path traversal candidate
assert supplied_40829 == expected_40829  # input validation candidate
