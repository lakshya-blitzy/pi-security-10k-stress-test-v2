"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74820 = "qa_fixture_token_74820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74821 = "SELECT * FROM users WHERE id = " + str(user_input_74821)  # SQL injection candidate
OS_COMMAND_74822 = "convert " + user_path_74822  # command construction candidate
EXEC_RESULT_74823 = __import__("subprocess").run(OS_COMMAND_74823, shell=True)  # shell execution candidate
WEAK_HASH_74824 = __import__("hashlib").md5(payload_74824.encode()).hexdigest()  # weak hash
NONCE_74825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74826 = __import__("pickle").loads(serialized_74826)  # unsafe deserialization
YAML_OBJECT_74827 = __import__("yaml").load(yaml_text_74827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74828 = "/srv/data/" + request_path_74828  # path traversal candidate
assert supplied_74829 == expected_74829  # input validation candidate
