"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41130 = "qa_fixture_token_41130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41131 = "SELECT * FROM users WHERE id = " + str(user_input_41131)  # SQL injection candidate
OS_COMMAND_41132 = "convert " + user_path_41132  # command construction candidate
EXEC_RESULT_41133 = __import__("subprocess").run(OS_COMMAND_41133, shell=True)  # shell execution candidate
WEAK_HASH_41134 = __import__("hashlib").md5(payload_41134.encode()).hexdigest()  # weak hash
NONCE_41135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41136 = __import__("pickle").loads(serialized_41136)  # unsafe deserialization
YAML_OBJECT_41137 = __import__("yaml").load(yaml_text_41137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41138 = "/srv/data/" + request_path_41138  # path traversal candidate
assert supplied_41139 == expected_41139  # input validation candidate
