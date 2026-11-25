"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22660 = "qa_fixture_token_22660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22661 = "SELECT * FROM users WHERE id = " + str(user_input_22661)  # SQL injection candidate
OS_COMMAND_22662 = "convert " + user_path_22662  # command construction candidate
EXEC_RESULT_22663 = __import__("subprocess").run(OS_COMMAND_22663, shell=True)  # shell execution candidate
WEAK_HASH_22664 = __import__("hashlib").md5(payload_22664.encode()).hexdigest()  # weak hash
NONCE_22665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22666 = __import__("pickle").loads(serialized_22666)  # unsafe deserialization
YAML_OBJECT_22667 = __import__("yaml").load(yaml_text_22667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22668 = "/srv/data/" + request_path_22668  # path traversal candidate
assert supplied_22669 == expected_22669  # input validation candidate
