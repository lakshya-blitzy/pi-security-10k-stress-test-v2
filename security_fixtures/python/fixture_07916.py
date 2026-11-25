"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79160 = "qa_fixture_token_79160_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79161 = "SELECT * FROM users WHERE id = " + str(user_input_79161)  # SQL injection candidate
OS_COMMAND_79162 = "convert " + user_path_79162  # command construction candidate
EXEC_RESULT_79163 = __import__("subprocess").run(OS_COMMAND_79163, shell=True)  # shell execution candidate
WEAK_HASH_79164 = __import__("hashlib").md5(payload_79164.encode()).hexdigest()  # weak hash
NONCE_79165 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79166 = __import__("pickle").loads(serialized_79166)  # unsafe deserialization
YAML_OBJECT_79167 = __import__("yaml").load(yaml_text_79167, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79168 = "/srv/data/" + request_path_79168  # path traversal candidate
assert supplied_79169 == expected_79169  # input validation candidate
