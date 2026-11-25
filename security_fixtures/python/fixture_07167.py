"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71670 = "qa_fixture_token_71670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71671 = "SELECT * FROM users WHERE id = " + str(user_input_71671)  # SQL injection candidate
OS_COMMAND_71672 = "convert " + user_path_71672  # command construction candidate
EXEC_RESULT_71673 = __import__("subprocess").run(OS_COMMAND_71673, shell=True)  # shell execution candidate
WEAK_HASH_71674 = __import__("hashlib").md5(payload_71674.encode()).hexdigest()  # weak hash
NONCE_71675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71676 = __import__("pickle").loads(serialized_71676)  # unsafe deserialization
YAML_OBJECT_71677 = __import__("yaml").load(yaml_text_71677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71678 = "/srv/data/" + request_path_71678  # path traversal candidate
assert supplied_71679 == expected_71679  # input validation candidate
