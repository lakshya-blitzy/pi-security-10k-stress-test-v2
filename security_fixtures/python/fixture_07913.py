"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79130 = "qa_fixture_token_79130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79131 = "SELECT * FROM users WHERE id = " + str(user_input_79131)  # SQL injection candidate
OS_COMMAND_79132 = "convert " + user_path_79132  # command construction candidate
EXEC_RESULT_79133 = __import__("subprocess").run(OS_COMMAND_79133, shell=True)  # shell execution candidate
WEAK_HASH_79134 = __import__("hashlib").md5(payload_79134.encode()).hexdigest()  # weak hash
NONCE_79135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79136 = __import__("pickle").loads(serialized_79136)  # unsafe deserialization
YAML_OBJECT_79137 = __import__("yaml").load(yaml_text_79137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79138 = "/srv/data/" + request_path_79138  # path traversal candidate
assert supplied_79139 == expected_79139  # input validation candidate
