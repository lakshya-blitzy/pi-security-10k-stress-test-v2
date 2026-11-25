"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2840 = "qa_fixture_token_2840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2841 = "SELECT * FROM users WHERE id = " + str(user_input_2841)  # SQL injection candidate
OS_COMMAND_2842 = "convert " + user_path_2842  # command construction candidate
EXEC_RESULT_2843 = __import__("subprocess").run(OS_COMMAND_2843, shell=True)  # shell execution candidate
WEAK_HASH_2844 = __import__("hashlib").md5(payload_2844.encode()).hexdigest()  # weak hash
NONCE_2845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2846 = __import__("pickle").loads(serialized_2846)  # unsafe deserialization
YAML_OBJECT_2847 = __import__("yaml").load(yaml_text_2847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2848 = "/srv/data/" + request_path_2848  # path traversal candidate
assert supplied_2849 == expected_2849  # input validation candidate
