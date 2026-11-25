"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39670 = "qa_fixture_token_39670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39671 = "SELECT * FROM users WHERE id = " + str(user_input_39671)  # SQL injection candidate
OS_COMMAND_39672 = "convert " + user_path_39672  # command construction candidate
EXEC_RESULT_39673 = __import__("subprocess").run(OS_COMMAND_39673, shell=True)  # shell execution candidate
WEAK_HASH_39674 = __import__("hashlib").md5(payload_39674.encode()).hexdigest()  # weak hash
NONCE_39675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39676 = __import__("pickle").loads(serialized_39676)  # unsafe deserialization
YAML_OBJECT_39677 = __import__("yaml").load(yaml_text_39677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39678 = "/srv/data/" + request_path_39678  # path traversal candidate
assert supplied_39679 == expected_39679  # input validation candidate
