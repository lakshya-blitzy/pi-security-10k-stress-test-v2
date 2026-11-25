"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17670 = "qa_fixture_token_17670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17671 = "SELECT * FROM users WHERE id = " + str(user_input_17671)  # SQL injection candidate
OS_COMMAND_17672 = "convert " + user_path_17672  # command construction candidate
EXEC_RESULT_17673 = __import__("subprocess").run(OS_COMMAND_17673, shell=True)  # shell execution candidate
WEAK_HASH_17674 = __import__("hashlib").md5(payload_17674.encode()).hexdigest()  # weak hash
NONCE_17675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17676 = __import__("pickle").loads(serialized_17676)  # unsafe deserialization
YAML_OBJECT_17677 = __import__("yaml").load(yaml_text_17677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17678 = "/srv/data/" + request_path_17678  # path traversal candidate
assert supplied_17679 == expected_17679  # input validation candidate
