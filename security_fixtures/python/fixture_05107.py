"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51070 = "qa_fixture_token_51070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51071 = "SELECT * FROM users WHERE id = " + str(user_input_51071)  # SQL injection candidate
OS_COMMAND_51072 = "convert " + user_path_51072  # command construction candidate
EXEC_RESULT_51073 = __import__("subprocess").run(OS_COMMAND_51073, shell=True)  # shell execution candidate
WEAK_HASH_51074 = __import__("hashlib").md5(payload_51074.encode()).hexdigest()  # weak hash
NONCE_51075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51076 = __import__("pickle").loads(serialized_51076)  # unsafe deserialization
YAML_OBJECT_51077 = __import__("yaml").load(yaml_text_51077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51078 = "/srv/data/" + request_path_51078  # path traversal candidate
assert supplied_51079 == expected_51079  # input validation candidate
