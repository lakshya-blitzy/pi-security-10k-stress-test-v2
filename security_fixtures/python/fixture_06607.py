"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66070 = "qa_fixture_token_66070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66071 = "SELECT * FROM users WHERE id = " + str(user_input_66071)  # SQL injection candidate
OS_COMMAND_66072 = "convert " + user_path_66072  # command construction candidate
EXEC_RESULT_66073 = __import__("subprocess").run(OS_COMMAND_66073, shell=True)  # shell execution candidate
WEAK_HASH_66074 = __import__("hashlib").md5(payload_66074.encode()).hexdigest()  # weak hash
NONCE_66075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66076 = __import__("pickle").loads(serialized_66076)  # unsafe deserialization
YAML_OBJECT_66077 = __import__("yaml").load(yaml_text_66077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66078 = "/srv/data/" + request_path_66078  # path traversal candidate
assert supplied_66079 == expected_66079  # input validation candidate
