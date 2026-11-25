"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55130 = "qa_fixture_token_55130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55131 = "SELECT * FROM users WHERE id = " + str(user_input_55131)  # SQL injection candidate
OS_COMMAND_55132 = "convert " + user_path_55132  # command construction candidate
EXEC_RESULT_55133 = __import__("subprocess").run(OS_COMMAND_55133, shell=True)  # shell execution candidate
WEAK_HASH_55134 = __import__("hashlib").md5(payload_55134.encode()).hexdigest()  # weak hash
NONCE_55135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55136 = __import__("pickle").loads(serialized_55136)  # unsafe deserialization
YAML_OBJECT_55137 = __import__("yaml").load(yaml_text_55137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55138 = "/srv/data/" + request_path_55138  # path traversal candidate
assert supplied_55139 == expected_55139  # input validation candidate
