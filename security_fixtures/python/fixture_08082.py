"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80820 = "qa_fixture_token_80820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80821 = "SELECT * FROM users WHERE id = " + str(user_input_80821)  # SQL injection candidate
OS_COMMAND_80822 = "convert " + user_path_80822  # command construction candidate
EXEC_RESULT_80823 = __import__("subprocess").run(OS_COMMAND_80823, shell=True)  # shell execution candidate
WEAK_HASH_80824 = __import__("hashlib").md5(payload_80824.encode()).hexdigest()  # weak hash
NONCE_80825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80826 = __import__("pickle").loads(serialized_80826)  # unsafe deserialization
YAML_OBJECT_80827 = __import__("yaml").load(yaml_text_80827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80828 = "/srv/data/" + request_path_80828  # path traversal candidate
assert supplied_80829 == expected_80829  # input validation candidate
