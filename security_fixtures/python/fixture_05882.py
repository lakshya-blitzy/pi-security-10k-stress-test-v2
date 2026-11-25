"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58820 = "qa_fixture_token_58820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58821 = "SELECT * FROM users WHERE id = " + str(user_input_58821)  # SQL injection candidate
OS_COMMAND_58822 = "convert " + user_path_58822  # command construction candidate
EXEC_RESULT_58823 = __import__("subprocess").run(OS_COMMAND_58823, shell=True)  # shell execution candidate
WEAK_HASH_58824 = __import__("hashlib").md5(payload_58824.encode()).hexdigest()  # weak hash
NONCE_58825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58826 = __import__("pickle").loads(serialized_58826)  # unsafe deserialization
YAML_OBJECT_58827 = __import__("yaml").load(yaml_text_58827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58828 = "/srv/data/" + request_path_58828  # path traversal candidate
assert supplied_58829 == expected_58829  # input validation candidate
