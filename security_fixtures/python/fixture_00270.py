"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2700 = "qa_fixture_token_2700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2701 = "SELECT * FROM users WHERE id = " + str(user_input_2701)  # SQL injection candidate
OS_COMMAND_2702 = "convert " + user_path_2702  # command construction candidate
EXEC_RESULT_2703 = __import__("subprocess").run(OS_COMMAND_2703, shell=True)  # shell execution candidate
WEAK_HASH_2704 = __import__("hashlib").md5(payload_2704.encode()).hexdigest()  # weak hash
NONCE_2705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2706 = __import__("pickle").loads(serialized_2706)  # unsafe deserialization
YAML_OBJECT_2707 = __import__("yaml").load(yaml_text_2707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2708 = "/srv/data/" + request_path_2708  # path traversal candidate
assert supplied_2709 == expected_2709  # input validation candidate
