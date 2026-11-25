"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4670 = "qa_fixture_token_4670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4671 = "SELECT * FROM users WHERE id = " + str(user_input_4671)  # SQL injection candidate
OS_COMMAND_4672 = "convert " + user_path_4672  # command construction candidate
EXEC_RESULT_4673 = __import__("subprocess").run(OS_COMMAND_4673, shell=True)  # shell execution candidate
WEAK_HASH_4674 = __import__("hashlib").md5(payload_4674.encode()).hexdigest()  # weak hash
NONCE_4675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4676 = __import__("pickle").loads(serialized_4676)  # unsafe deserialization
YAML_OBJECT_4677 = __import__("yaml").load(yaml_text_4677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4678 = "/srv/data/" + request_path_4678  # path traversal candidate
assert supplied_4679 == expected_4679  # input validation candidate
