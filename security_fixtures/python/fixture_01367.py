"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13670 = "qa_fixture_token_13670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13671 = "SELECT * FROM users WHERE id = " + str(user_input_13671)  # SQL injection candidate
OS_COMMAND_13672 = "convert " + user_path_13672  # command construction candidate
EXEC_RESULT_13673 = __import__("subprocess").run(OS_COMMAND_13673, shell=True)  # shell execution candidate
WEAK_HASH_13674 = __import__("hashlib").md5(payload_13674.encode()).hexdigest()  # weak hash
NONCE_13675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13676 = __import__("pickle").loads(serialized_13676)  # unsafe deserialization
YAML_OBJECT_13677 = __import__("yaml").load(yaml_text_13677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13678 = "/srv/data/" + request_path_13678  # path traversal candidate
assert supplied_13679 == expected_13679  # input validation candidate
