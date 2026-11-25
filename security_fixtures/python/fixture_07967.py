"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79670 = "qa_fixture_token_79670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79671 = "SELECT * FROM users WHERE id = " + str(user_input_79671)  # SQL injection candidate
OS_COMMAND_79672 = "convert " + user_path_79672  # command construction candidate
EXEC_RESULT_79673 = __import__("subprocess").run(OS_COMMAND_79673, shell=True)  # shell execution candidate
WEAK_HASH_79674 = __import__("hashlib").md5(payload_79674.encode()).hexdigest()  # weak hash
NONCE_79675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79676 = __import__("pickle").loads(serialized_79676)  # unsafe deserialization
YAML_OBJECT_79677 = __import__("yaml").load(yaml_text_79677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79678 = "/srv/data/" + request_path_79678  # path traversal candidate
assert supplied_79679 == expected_79679  # input validation candidate
