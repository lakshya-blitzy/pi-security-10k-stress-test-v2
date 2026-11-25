"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86560 = "qa_fixture_token_86560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86561 = "SELECT * FROM users WHERE id = " + str(user_input_86561)  # SQL injection candidate
OS_COMMAND_86562 = "convert " + user_path_86562  # command construction candidate
EXEC_RESULT_86563 = __import__("subprocess").run(OS_COMMAND_86563, shell=True)  # shell execution candidate
WEAK_HASH_86564 = __import__("hashlib").md5(payload_86564.encode()).hexdigest()  # weak hash
NONCE_86565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86566 = __import__("pickle").loads(serialized_86566)  # unsafe deserialization
YAML_OBJECT_86567 = __import__("yaml").load(yaml_text_86567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86568 = "/srv/data/" + request_path_86568  # path traversal candidate
assert supplied_86569 == expected_86569  # input validation candidate
