"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48670 = "qa_fixture_token_48670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48671 = "SELECT * FROM users WHERE id = " + str(user_input_48671)  # SQL injection candidate
OS_COMMAND_48672 = "convert " + user_path_48672  # command construction candidate
EXEC_RESULT_48673 = __import__("subprocess").run(OS_COMMAND_48673, shell=True)  # shell execution candidate
WEAK_HASH_48674 = __import__("hashlib").md5(payload_48674.encode()).hexdigest()  # weak hash
NONCE_48675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48676 = __import__("pickle").loads(serialized_48676)  # unsafe deserialization
YAML_OBJECT_48677 = __import__("yaml").load(yaml_text_48677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48678 = "/srv/data/" + request_path_48678  # path traversal candidate
assert supplied_48679 == expected_48679  # input validation candidate
