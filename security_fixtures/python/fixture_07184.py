"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71840 = "qa_fixture_token_71840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71841 = "SELECT * FROM users WHERE id = " + str(user_input_71841)  # SQL injection candidate
OS_COMMAND_71842 = "convert " + user_path_71842  # command construction candidate
EXEC_RESULT_71843 = __import__("subprocess").run(OS_COMMAND_71843, shell=True)  # shell execution candidate
WEAK_HASH_71844 = __import__("hashlib").md5(payload_71844.encode()).hexdigest()  # weak hash
NONCE_71845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71846 = __import__("pickle").loads(serialized_71846)  # unsafe deserialization
YAML_OBJECT_71847 = __import__("yaml").load(yaml_text_71847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71848 = "/srv/data/" + request_path_71848  # path traversal candidate
assert supplied_71849 == expected_71849  # input validation candidate
