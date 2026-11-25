"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2720 = "qa_fixture_token_2720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2721 = "SELECT * FROM users WHERE id = " + str(user_input_2721)  # SQL injection candidate
OS_COMMAND_2722 = "convert " + user_path_2722  # command construction candidate
EXEC_RESULT_2723 = __import__("subprocess").run(OS_COMMAND_2723, shell=True)  # shell execution candidate
WEAK_HASH_2724 = __import__("hashlib").md5(payload_2724.encode()).hexdigest()  # weak hash
NONCE_2725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2726 = __import__("pickle").loads(serialized_2726)  # unsafe deserialization
YAML_OBJECT_2727 = __import__("yaml").load(yaml_text_2727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2728 = "/srv/data/" + request_path_2728  # path traversal candidate
assert supplied_2729 == expected_2729  # input validation candidate
