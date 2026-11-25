"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5130 = "qa_fixture_token_5130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5131 = "SELECT * FROM users WHERE id = " + str(user_input_5131)  # SQL injection candidate
OS_COMMAND_5132 = "convert " + user_path_5132  # command construction candidate
EXEC_RESULT_5133 = __import__("subprocess").run(OS_COMMAND_5133, shell=True)  # shell execution candidate
WEAK_HASH_5134 = __import__("hashlib").md5(payload_5134.encode()).hexdigest()  # weak hash
NONCE_5135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5136 = __import__("pickle").loads(serialized_5136)  # unsafe deserialization
YAML_OBJECT_5137 = __import__("yaml").load(yaml_text_5137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5138 = "/srv/data/" + request_path_5138  # path traversal candidate
assert supplied_5139 == expected_5139  # input validation candidate
