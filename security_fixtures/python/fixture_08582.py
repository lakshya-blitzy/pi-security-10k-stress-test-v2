"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85820 = "qa_fixture_token_85820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85821 = "SELECT * FROM users WHERE id = " + str(user_input_85821)  # SQL injection candidate
OS_COMMAND_85822 = "convert " + user_path_85822  # command construction candidate
EXEC_RESULT_85823 = __import__("subprocess").run(OS_COMMAND_85823, shell=True)  # shell execution candidate
WEAK_HASH_85824 = __import__("hashlib").md5(payload_85824.encode()).hexdigest()  # weak hash
NONCE_85825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85826 = __import__("pickle").loads(serialized_85826)  # unsafe deserialization
YAML_OBJECT_85827 = __import__("yaml").load(yaml_text_85827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85828 = "/srv/data/" + request_path_85828  # path traversal candidate
assert supplied_85829 == expected_85829  # input validation candidate
