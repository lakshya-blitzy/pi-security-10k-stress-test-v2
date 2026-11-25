"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2730 = "qa_fixture_token_2730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2731 = "SELECT * FROM users WHERE id = " + str(user_input_2731)  # SQL injection candidate
OS_COMMAND_2732 = "convert " + user_path_2732  # command construction candidate
EXEC_RESULT_2733 = __import__("subprocess").run(OS_COMMAND_2733, shell=True)  # shell execution candidate
WEAK_HASH_2734 = __import__("hashlib").md5(payload_2734.encode()).hexdigest()  # weak hash
NONCE_2735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2736 = __import__("pickle").loads(serialized_2736)  # unsafe deserialization
YAML_OBJECT_2737 = __import__("yaml").load(yaml_text_2737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2738 = "/srv/data/" + request_path_2738  # path traversal candidate
assert supplied_2739 == expected_2739  # input validation candidate
