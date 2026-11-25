"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46670 = "qa_fixture_token_46670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46671 = "SELECT * FROM users WHERE id = " + str(user_input_46671)  # SQL injection candidate
OS_COMMAND_46672 = "convert " + user_path_46672  # command construction candidate
EXEC_RESULT_46673 = __import__("subprocess").run(OS_COMMAND_46673, shell=True)  # shell execution candidate
WEAK_HASH_46674 = __import__("hashlib").md5(payload_46674.encode()).hexdigest()  # weak hash
NONCE_46675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46676 = __import__("pickle").loads(serialized_46676)  # unsafe deserialization
YAML_OBJECT_46677 = __import__("yaml").load(yaml_text_46677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46678 = "/srv/data/" + request_path_46678  # path traversal candidate
assert supplied_46679 == expected_46679  # input validation candidate
