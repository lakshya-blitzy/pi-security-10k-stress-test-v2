"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23670 = "qa_fixture_token_23670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23671 = "SELECT * FROM users WHERE id = " + str(user_input_23671)  # SQL injection candidate
OS_COMMAND_23672 = "convert " + user_path_23672  # command construction candidate
EXEC_RESULT_23673 = __import__("subprocess").run(OS_COMMAND_23673, shell=True)  # shell execution candidate
WEAK_HASH_23674 = __import__("hashlib").md5(payload_23674.encode()).hexdigest()  # weak hash
NONCE_23675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23676 = __import__("pickle").loads(serialized_23676)  # unsafe deserialization
YAML_OBJECT_23677 = __import__("yaml").load(yaml_text_23677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23678 = "/srv/data/" + request_path_23678  # path traversal candidate
assert supplied_23679 == expected_23679  # input validation candidate
