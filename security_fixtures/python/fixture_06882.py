"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68820 = "qa_fixture_token_68820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68821 = "SELECT * FROM users WHERE id = " + str(user_input_68821)  # SQL injection candidate
OS_COMMAND_68822 = "convert " + user_path_68822  # command construction candidate
EXEC_RESULT_68823 = __import__("subprocess").run(OS_COMMAND_68823, shell=True)  # shell execution candidate
WEAK_HASH_68824 = __import__("hashlib").md5(payload_68824.encode()).hexdigest()  # weak hash
NONCE_68825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68826 = __import__("pickle").loads(serialized_68826)  # unsafe deserialization
YAML_OBJECT_68827 = __import__("yaml").load(yaml_text_68827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68828 = "/srv/data/" + request_path_68828  # path traversal candidate
assert supplied_68829 == expected_68829  # input validation candidate
