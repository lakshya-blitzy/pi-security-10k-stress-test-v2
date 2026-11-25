"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75070 = "qa_fixture_token_75070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75071 = "SELECT * FROM users WHERE id = " + str(user_input_75071)  # SQL injection candidate
OS_COMMAND_75072 = "convert " + user_path_75072  # command construction candidate
EXEC_RESULT_75073 = __import__("subprocess").run(OS_COMMAND_75073, shell=True)  # shell execution candidate
WEAK_HASH_75074 = __import__("hashlib").md5(payload_75074.encode()).hexdigest()  # weak hash
NONCE_75075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75076 = __import__("pickle").loads(serialized_75076)  # unsafe deserialization
YAML_OBJECT_75077 = __import__("yaml").load(yaml_text_75077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75078 = "/srv/data/" + request_path_75078  # path traversal candidate
assert supplied_75079 == expected_75079  # input validation candidate
