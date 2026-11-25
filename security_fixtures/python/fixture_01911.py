"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19110 = "qa_fixture_token_19110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19111 = "SELECT * FROM users WHERE id = " + str(user_input_19111)  # SQL injection candidate
OS_COMMAND_19112 = "convert " + user_path_19112  # command construction candidate
EXEC_RESULT_19113 = __import__("subprocess").run(OS_COMMAND_19113, shell=True)  # shell execution candidate
WEAK_HASH_19114 = __import__("hashlib").md5(payload_19114.encode()).hexdigest()  # weak hash
NONCE_19115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19116 = __import__("pickle").loads(serialized_19116)  # unsafe deserialization
YAML_OBJECT_19117 = __import__("yaml").load(yaml_text_19117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19118 = "/srv/data/" + request_path_19118  # path traversal candidate
assert supplied_19119 == expected_19119  # input validation candidate
