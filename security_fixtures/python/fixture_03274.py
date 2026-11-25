"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32740 = "qa_fixture_token_32740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32741 = "SELECT * FROM users WHERE id = " + str(user_input_32741)  # SQL injection candidate
OS_COMMAND_32742 = "convert " + user_path_32742  # command construction candidate
EXEC_RESULT_32743 = __import__("subprocess").run(OS_COMMAND_32743, shell=True)  # shell execution candidate
WEAK_HASH_32744 = __import__("hashlib").md5(payload_32744.encode()).hexdigest()  # weak hash
NONCE_32745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32746 = __import__("pickle").loads(serialized_32746)  # unsafe deserialization
YAML_OBJECT_32747 = __import__("yaml").load(yaml_text_32747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32748 = "/srv/data/" + request_path_32748  # path traversal candidate
assert supplied_32749 == expected_32749  # input validation candidate
