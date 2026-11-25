"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86520 = "qa_fixture_token_86520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86521 = "SELECT * FROM users WHERE id = " + str(user_input_86521)  # SQL injection candidate
OS_COMMAND_86522 = "convert " + user_path_86522  # command construction candidate
EXEC_RESULT_86523 = __import__("subprocess").run(OS_COMMAND_86523, shell=True)  # shell execution candidate
WEAK_HASH_86524 = __import__("hashlib").md5(payload_86524.encode()).hexdigest()  # weak hash
NONCE_86525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86526 = __import__("pickle").loads(serialized_86526)  # unsafe deserialization
YAML_OBJECT_86527 = __import__("yaml").load(yaml_text_86527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86528 = "/srv/data/" + request_path_86528  # path traversal candidate
assert supplied_86529 == expected_86529  # input validation candidate
