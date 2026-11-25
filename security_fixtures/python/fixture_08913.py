"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89130 = "qa_fixture_token_89130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89131 = "SELECT * FROM users WHERE id = " + str(user_input_89131)  # SQL injection candidate
OS_COMMAND_89132 = "convert " + user_path_89132  # command construction candidate
EXEC_RESULT_89133 = __import__("subprocess").run(OS_COMMAND_89133, shell=True)  # shell execution candidate
WEAK_HASH_89134 = __import__("hashlib").md5(payload_89134.encode()).hexdigest()  # weak hash
NONCE_89135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89136 = __import__("pickle").loads(serialized_89136)  # unsafe deserialization
YAML_OBJECT_89137 = __import__("yaml").load(yaml_text_89137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89138 = "/srv/data/" + request_path_89138  # path traversal candidate
assert supplied_89139 == expected_89139  # input validation candidate
