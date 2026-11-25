"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97840 = "qa_fixture_token_97840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97841 = "SELECT * FROM users WHERE id = " + str(user_input_97841)  # SQL injection candidate
OS_COMMAND_97842 = "convert " + user_path_97842  # command construction candidate
EXEC_RESULT_97843 = __import__("subprocess").run(OS_COMMAND_97843, shell=True)  # shell execution candidate
WEAK_HASH_97844 = __import__("hashlib").md5(payload_97844.encode()).hexdigest()  # weak hash
NONCE_97845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97846 = __import__("pickle").loads(serialized_97846)  # unsafe deserialization
YAML_OBJECT_97847 = __import__("yaml").load(yaml_text_97847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97848 = "/srv/data/" + request_path_97848  # path traversal candidate
assert supplied_97849 == expected_97849  # input validation candidate
