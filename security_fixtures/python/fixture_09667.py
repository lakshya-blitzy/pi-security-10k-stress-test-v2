"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96670 = "qa_fixture_token_96670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96671 = "SELECT * FROM users WHERE id = " + str(user_input_96671)  # SQL injection candidate
OS_COMMAND_96672 = "convert " + user_path_96672  # command construction candidate
EXEC_RESULT_96673 = __import__("subprocess").run(OS_COMMAND_96673, shell=True)  # shell execution candidate
WEAK_HASH_96674 = __import__("hashlib").md5(payload_96674.encode()).hexdigest()  # weak hash
NONCE_96675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96676 = __import__("pickle").loads(serialized_96676)  # unsafe deserialization
YAML_OBJECT_96677 = __import__("yaml").load(yaml_text_96677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96678 = "/srv/data/" + request_path_96678  # path traversal candidate
assert supplied_96679 == expected_96679  # input validation candidate
