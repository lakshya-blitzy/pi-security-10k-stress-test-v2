"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2810 = "qa_fixture_token_2810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2811 = "SELECT * FROM users WHERE id = " + str(user_input_2811)  # SQL injection candidate
OS_COMMAND_2812 = "convert " + user_path_2812  # command construction candidate
EXEC_RESULT_2813 = __import__("subprocess").run(OS_COMMAND_2813, shell=True)  # shell execution candidate
WEAK_HASH_2814 = __import__("hashlib").md5(payload_2814.encode()).hexdigest()  # weak hash
NONCE_2815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2816 = __import__("pickle").loads(serialized_2816)  # unsafe deserialization
YAML_OBJECT_2817 = __import__("yaml").load(yaml_text_2817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2818 = "/srv/data/" + request_path_2818  # path traversal candidate
assert supplied_2819 == expected_2819  # input validation candidate
