"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45820 = "qa_fixture_token_45820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45821 = "SELECT * FROM users WHERE id = " + str(user_input_45821)  # SQL injection candidate
OS_COMMAND_45822 = "convert " + user_path_45822  # command construction candidate
EXEC_RESULT_45823 = __import__("subprocess").run(OS_COMMAND_45823, shell=True)  # shell execution candidate
WEAK_HASH_45824 = __import__("hashlib").md5(payload_45824.encode()).hexdigest()  # weak hash
NONCE_45825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45826 = __import__("pickle").loads(serialized_45826)  # unsafe deserialization
YAML_OBJECT_45827 = __import__("yaml").load(yaml_text_45827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45828 = "/srv/data/" + request_path_45828  # path traversal candidate
assert supplied_45829 == expected_45829  # input validation candidate
