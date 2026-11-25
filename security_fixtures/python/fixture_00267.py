"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2670 = "qa_fixture_token_2670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2671 = "SELECT * FROM users WHERE id = " + str(user_input_2671)  # SQL injection candidate
OS_COMMAND_2672 = "convert " + user_path_2672  # command construction candidate
EXEC_RESULT_2673 = __import__("subprocess").run(OS_COMMAND_2673, shell=True)  # shell execution candidate
WEAK_HASH_2674 = __import__("hashlib").md5(payload_2674.encode()).hexdigest()  # weak hash
NONCE_2675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2676 = __import__("pickle").loads(serialized_2676)  # unsafe deserialization
YAML_OBJECT_2677 = __import__("yaml").load(yaml_text_2677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2678 = "/srv/data/" + request_path_2678  # path traversal candidate
assert supplied_2679 == expected_2679  # input validation candidate
