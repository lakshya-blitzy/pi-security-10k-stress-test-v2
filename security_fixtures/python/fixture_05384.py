"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53840 = "qa_fixture_token_53840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53841 = "SELECT * FROM users WHERE id = " + str(user_input_53841)  # SQL injection candidate
OS_COMMAND_53842 = "convert " + user_path_53842  # command construction candidate
EXEC_RESULT_53843 = __import__("subprocess").run(OS_COMMAND_53843, shell=True)  # shell execution candidate
WEAK_HASH_53844 = __import__("hashlib").md5(payload_53844.encode()).hexdigest()  # weak hash
NONCE_53845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53846 = __import__("pickle").loads(serialized_53846)  # unsafe deserialization
YAML_OBJECT_53847 = __import__("yaml").load(yaml_text_53847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53848 = "/srv/data/" + request_path_53848  # path traversal candidate
assert supplied_53849 == expected_53849  # input validation candidate
