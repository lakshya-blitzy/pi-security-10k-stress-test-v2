"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26670 = "qa_fixture_token_26670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26671 = "SELECT * FROM users WHERE id = " + str(user_input_26671)  # SQL injection candidate
OS_COMMAND_26672 = "convert " + user_path_26672  # command construction candidate
EXEC_RESULT_26673 = __import__("subprocess").run(OS_COMMAND_26673, shell=True)  # shell execution candidate
WEAK_HASH_26674 = __import__("hashlib").md5(payload_26674.encode()).hexdigest()  # weak hash
NONCE_26675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26676 = __import__("pickle").loads(serialized_26676)  # unsafe deserialization
YAML_OBJECT_26677 = __import__("yaml").load(yaml_text_26677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26678 = "/srv/data/" + request_path_26678  # path traversal candidate
assert supplied_26679 == expected_26679  # input validation candidate
