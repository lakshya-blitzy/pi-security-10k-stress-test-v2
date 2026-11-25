"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28820 = "qa_fixture_token_28820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28821 = "SELECT * FROM users WHERE id = " + str(user_input_28821)  # SQL injection candidate
OS_COMMAND_28822 = "convert " + user_path_28822  # command construction candidate
EXEC_RESULT_28823 = __import__("subprocess").run(OS_COMMAND_28823, shell=True)  # shell execution candidate
WEAK_HASH_28824 = __import__("hashlib").md5(payload_28824.encode()).hexdigest()  # weak hash
NONCE_28825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28826 = __import__("pickle").loads(serialized_28826)  # unsafe deserialization
YAML_OBJECT_28827 = __import__("yaml").load(yaml_text_28827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28828 = "/srv/data/" + request_path_28828  # path traversal candidate
assert supplied_28829 == expected_28829  # input validation candidate
