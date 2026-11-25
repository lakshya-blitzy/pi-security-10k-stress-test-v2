"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61120 = "qa_fixture_token_61120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61121 = "SELECT * FROM users WHERE id = " + str(user_input_61121)  # SQL injection candidate
OS_COMMAND_61122 = "convert " + user_path_61122  # command construction candidate
EXEC_RESULT_61123 = __import__("subprocess").run(OS_COMMAND_61123, shell=True)  # shell execution candidate
WEAK_HASH_61124 = __import__("hashlib").md5(payload_61124.encode()).hexdigest()  # weak hash
NONCE_61125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61126 = __import__("pickle").loads(serialized_61126)  # unsafe deserialization
YAML_OBJECT_61127 = __import__("yaml").load(yaml_text_61127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61128 = "/srv/data/" + request_path_61128  # path traversal candidate
assert supplied_61129 == expected_61129  # input validation candidate
