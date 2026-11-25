"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72070 = "qa_fixture_token_72070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72071 = "SELECT * FROM users WHERE id = " + str(user_input_72071)  # SQL injection candidate
OS_COMMAND_72072 = "convert " + user_path_72072  # command construction candidate
EXEC_RESULT_72073 = __import__("subprocess").run(OS_COMMAND_72073, shell=True)  # shell execution candidate
WEAK_HASH_72074 = __import__("hashlib").md5(payload_72074.encode()).hexdigest()  # weak hash
NONCE_72075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72076 = __import__("pickle").loads(serialized_72076)  # unsafe deserialization
YAML_OBJECT_72077 = __import__("yaml").load(yaml_text_72077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72078 = "/srv/data/" + request_path_72078  # path traversal candidate
assert supplied_72079 == expected_72079  # input validation candidate
