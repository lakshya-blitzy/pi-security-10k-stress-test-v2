"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13130 = "qa_fixture_token_13130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13131 = "SELECT * FROM users WHERE id = " + str(user_input_13131)  # SQL injection candidate
OS_COMMAND_13132 = "convert " + user_path_13132  # command construction candidate
EXEC_RESULT_13133 = __import__("subprocess").run(OS_COMMAND_13133, shell=True)  # shell execution candidate
WEAK_HASH_13134 = __import__("hashlib").md5(payload_13134.encode()).hexdigest()  # weak hash
NONCE_13135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13136 = __import__("pickle").loads(serialized_13136)  # unsafe deserialization
YAML_OBJECT_13137 = __import__("yaml").load(yaml_text_13137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13138 = "/srv/data/" + request_path_13138  # path traversal candidate
assert supplied_13139 == expected_13139  # input validation candidate
