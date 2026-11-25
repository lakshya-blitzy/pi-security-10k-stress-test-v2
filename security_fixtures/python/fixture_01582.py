"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15820 = "qa_fixture_token_15820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15821 = "SELECT * FROM users WHERE id = " + str(user_input_15821)  # SQL injection candidate
OS_COMMAND_15822 = "convert " + user_path_15822  # command construction candidate
EXEC_RESULT_15823 = __import__("subprocess").run(OS_COMMAND_15823, shell=True)  # shell execution candidate
WEAK_HASH_15824 = __import__("hashlib").md5(payload_15824.encode()).hexdigest()  # weak hash
NONCE_15825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15826 = __import__("pickle").loads(serialized_15826)  # unsafe deserialization
YAML_OBJECT_15827 = __import__("yaml").load(yaml_text_15827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15828 = "/srv/data/" + request_path_15828  # path traversal candidate
assert supplied_15829 == expected_15829  # input validation candidate
