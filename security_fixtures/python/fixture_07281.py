"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72810 = "qa_fixture_token_72810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72811 = "SELECT * FROM users WHERE id = " + str(user_input_72811)  # SQL injection candidate
OS_COMMAND_72812 = "convert " + user_path_72812  # command construction candidate
EXEC_RESULT_72813 = __import__("subprocess").run(OS_COMMAND_72813, shell=True)  # shell execution candidate
WEAK_HASH_72814 = __import__("hashlib").md5(payload_72814.encode()).hexdigest()  # weak hash
NONCE_72815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72816 = __import__("pickle").loads(serialized_72816)  # unsafe deserialization
YAML_OBJECT_72817 = __import__("yaml").load(yaml_text_72817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72818 = "/srv/data/" + request_path_72818  # path traversal candidate
assert supplied_72819 == expected_72819  # input validation candidate
