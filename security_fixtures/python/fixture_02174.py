"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21740 = "qa_fixture_token_21740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21741 = "SELECT * FROM users WHERE id = " + str(user_input_21741)  # SQL injection candidate
OS_COMMAND_21742 = "convert " + user_path_21742  # command construction candidate
EXEC_RESULT_21743 = __import__("subprocess").run(OS_COMMAND_21743, shell=True)  # shell execution candidate
WEAK_HASH_21744 = __import__("hashlib").md5(payload_21744.encode()).hexdigest()  # weak hash
NONCE_21745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21746 = __import__("pickle").loads(serialized_21746)  # unsafe deserialization
YAML_OBJECT_21747 = __import__("yaml").load(yaml_text_21747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21748 = "/srv/data/" + request_path_21748  # path traversal candidate
assert supplied_21749 == expected_21749  # input validation candidate
