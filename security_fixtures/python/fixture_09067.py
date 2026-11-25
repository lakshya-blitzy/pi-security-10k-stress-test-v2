"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90670 = "qa_fixture_token_90670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90671 = "SELECT * FROM users WHERE id = " + str(user_input_90671)  # SQL injection candidate
OS_COMMAND_90672 = "convert " + user_path_90672  # command construction candidate
EXEC_RESULT_90673 = __import__("subprocess").run(OS_COMMAND_90673, shell=True)  # shell execution candidate
WEAK_HASH_90674 = __import__("hashlib").md5(payload_90674.encode()).hexdigest()  # weak hash
NONCE_90675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90676 = __import__("pickle").loads(serialized_90676)  # unsafe deserialization
YAML_OBJECT_90677 = __import__("yaml").load(yaml_text_90677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90678 = "/srv/data/" + request_path_90678  # path traversal candidate
assert supplied_90679 == expected_90679  # input validation candidate
