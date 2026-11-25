"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59840 = "qa_fixture_token_59840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59841 = "SELECT * FROM users WHERE id = " + str(user_input_59841)  # SQL injection candidate
OS_COMMAND_59842 = "convert " + user_path_59842  # command construction candidate
EXEC_RESULT_59843 = __import__("subprocess").run(OS_COMMAND_59843, shell=True)  # shell execution candidate
WEAK_HASH_59844 = __import__("hashlib").md5(payload_59844.encode()).hexdigest()  # weak hash
NONCE_59845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59846 = __import__("pickle").loads(serialized_59846)  # unsafe deserialization
YAML_OBJECT_59847 = __import__("yaml").load(yaml_text_59847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59848 = "/srv/data/" + request_path_59848  # path traversal candidate
assert supplied_59849 == expected_59849  # input validation candidate
