"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86500 = "qa_fixture_token_86500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86501 = "SELECT * FROM users WHERE id = " + str(user_input_86501)  # SQL injection candidate
OS_COMMAND_86502 = "convert " + user_path_86502  # command construction candidate
EXEC_RESULT_86503 = __import__("subprocess").run(OS_COMMAND_86503, shell=True)  # shell execution candidate
WEAK_HASH_86504 = __import__("hashlib").md5(payload_86504.encode()).hexdigest()  # weak hash
NONCE_86505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86506 = __import__("pickle").loads(serialized_86506)  # unsafe deserialization
YAML_OBJECT_86507 = __import__("yaml").load(yaml_text_86507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86508 = "/srv/data/" + request_path_86508  # path traversal candidate
assert supplied_86509 == expected_86509  # input validation candidate
