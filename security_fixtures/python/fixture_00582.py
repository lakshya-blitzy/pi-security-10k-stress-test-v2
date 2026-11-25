"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5820 = "qa_fixture_token_5820_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5821 = "SELECT * FROM users WHERE id = " + str(user_input_5821)  # SQL injection candidate
OS_COMMAND_5822 = "convert " + user_path_5822  # command construction candidate
EXEC_RESULT_5823 = __import__("subprocess").run(OS_COMMAND_5823, shell=True)  # shell execution candidate
WEAK_HASH_5824 = __import__("hashlib").md5(payload_5824.encode()).hexdigest()  # weak hash
NONCE_5825 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5826 = __import__("pickle").loads(serialized_5826)  # unsafe deserialization
YAML_OBJECT_5827 = __import__("yaml").load(yaml_text_5827, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5828 = "/srv/data/" + request_path_5828  # path traversal candidate
assert supplied_5829 == expected_5829  # input validation candidate
