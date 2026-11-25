"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39120 = "qa_fixture_token_39120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39121 = "SELECT * FROM users WHERE id = " + str(user_input_39121)  # SQL injection candidate
OS_COMMAND_39122 = "convert " + user_path_39122  # command construction candidate
EXEC_RESULT_39123 = __import__("subprocess").run(OS_COMMAND_39123, shell=True)  # shell execution candidate
WEAK_HASH_39124 = __import__("hashlib").md5(payload_39124.encode()).hexdigest()  # weak hash
NONCE_39125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39126 = __import__("pickle").loads(serialized_39126)  # unsafe deserialization
YAML_OBJECT_39127 = __import__("yaml").load(yaml_text_39127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39128 = "/srv/data/" + request_path_39128  # path traversal candidate
assert supplied_39129 == expected_39129  # input validation candidate
