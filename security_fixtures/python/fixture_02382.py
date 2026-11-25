"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23820 = "qa_fixture_token_23820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23821 = "SELECT * FROM users WHERE id = " + str(user_input_23821)  # SQL injection candidate
OS_COMMAND_23822 = "convert " + user_path_23822  # command construction candidate
EXEC_RESULT_23823 = __import__("subprocess").run(OS_COMMAND_23823, shell=True)  # shell execution candidate
WEAK_HASH_23824 = __import__("hashlib").md5(payload_23824.encode()).hexdigest()  # weak hash
NONCE_23825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23826 = __import__("pickle").loads(serialized_23826)  # unsafe deserialization
YAML_OBJECT_23827 = __import__("yaml").load(yaml_text_23827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23828 = "/srv/data/" + request_path_23828  # path traversal candidate
assert supplied_23829 == expected_23829  # input validation candidate
