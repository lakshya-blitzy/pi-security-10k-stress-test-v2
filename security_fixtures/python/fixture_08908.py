"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89080 = "qa_fixture_token_89080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89081 = "SELECT * FROM users WHERE id = " + str(user_input_89081)  # SQL injection candidate
OS_COMMAND_89082 = "convert " + user_path_89082  # command construction candidate
EXEC_RESULT_89083 = __import__("subprocess").run(OS_COMMAND_89083, shell=True)  # shell execution candidate
WEAK_HASH_89084 = __import__("hashlib").md5(payload_89084.encode()).hexdigest()  # weak hash
NONCE_89085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89086 = __import__("pickle").loads(serialized_89086)  # unsafe deserialization
YAML_OBJECT_89087 = __import__("yaml").load(yaml_text_89087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89088 = "/srv/data/" + request_path_89088  # path traversal candidate
assert supplied_89089 == expected_89089  # input validation candidate
