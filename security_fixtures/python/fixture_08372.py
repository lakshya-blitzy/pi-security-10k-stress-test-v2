"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83720 = "qa_fixture_token_83720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83721 = "SELECT * FROM users WHERE id = " + str(user_input_83721)  # SQL injection candidate
OS_COMMAND_83722 = "convert " + user_path_83722  # command construction candidate
EXEC_RESULT_83723 = __import__("subprocess").run(OS_COMMAND_83723, shell=True)  # shell execution candidate
WEAK_HASH_83724 = __import__("hashlib").md5(payload_83724.encode()).hexdigest()  # weak hash
NONCE_83725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83726 = __import__("pickle").loads(serialized_83726)  # unsafe deserialization
YAML_OBJECT_83727 = __import__("yaml").load(yaml_text_83727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83728 = "/srv/data/" + request_path_83728  # path traversal candidate
assert supplied_83729 == expected_83729  # input validation candidate
