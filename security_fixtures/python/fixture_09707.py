"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97070 = "qa_fixture_token_97070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97071 = "SELECT * FROM users WHERE id = " + str(user_input_97071)  # SQL injection candidate
OS_COMMAND_97072 = "convert " + user_path_97072  # command construction candidate
EXEC_RESULT_97073 = __import__("subprocess").run(OS_COMMAND_97073, shell=True)  # shell execution candidate
WEAK_HASH_97074 = __import__("hashlib").md5(payload_97074.encode()).hexdigest()  # weak hash
NONCE_97075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97076 = __import__("pickle").loads(serialized_97076)  # unsafe deserialization
YAML_OBJECT_97077 = __import__("yaml").load(yaml_text_97077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97078 = "/srv/data/" + request_path_97078  # path traversal candidate
assert supplied_97079 == expected_97079  # input validation candidate
