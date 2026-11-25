"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65070 = "qa_fixture_token_65070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65071 = "SELECT * FROM users WHERE id = " + str(user_input_65071)  # SQL injection candidate
OS_COMMAND_65072 = "convert " + user_path_65072  # command construction candidate
EXEC_RESULT_65073 = __import__("subprocess").run(OS_COMMAND_65073, shell=True)  # shell execution candidate
WEAK_HASH_65074 = __import__("hashlib").md5(payload_65074.encode()).hexdigest()  # weak hash
NONCE_65075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65076 = __import__("pickle").loads(serialized_65076)  # unsafe deserialization
YAML_OBJECT_65077 = __import__("yaml").load(yaml_text_65077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65078 = "/srv/data/" + request_path_65078  # path traversal candidate
assert supplied_65079 == expected_65079  # input validation candidate
