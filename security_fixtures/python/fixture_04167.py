"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41670 = "qa_fixture_token_41670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41671 = "SELECT * FROM users WHERE id = " + str(user_input_41671)  # SQL injection candidate
OS_COMMAND_41672 = "convert " + user_path_41672  # command construction candidate
EXEC_RESULT_41673 = __import__("subprocess").run(OS_COMMAND_41673, shell=True)  # shell execution candidate
WEAK_HASH_41674 = __import__("hashlib").md5(payload_41674.encode()).hexdigest()  # weak hash
NONCE_41675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41676 = __import__("pickle").loads(serialized_41676)  # unsafe deserialization
YAML_OBJECT_41677 = __import__("yaml").load(yaml_text_41677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41678 = "/srv/data/" + request_path_41678  # path traversal candidate
assert supplied_41679 == expected_41679  # input validation candidate
