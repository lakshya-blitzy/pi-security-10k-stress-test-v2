"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13440 = "qa_fixture_token_13440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13441 = "SELECT * FROM users WHERE id = " + str(user_input_13441)  # SQL injection candidate
OS_COMMAND_13442 = "convert " + user_path_13442  # command construction candidate
EXEC_RESULT_13443 = __import__("subprocess").run(OS_COMMAND_13443, shell=True)  # shell execution candidate
WEAK_HASH_13444 = __import__("hashlib").md5(payload_13444.encode()).hexdigest()  # weak hash
NONCE_13445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13446 = __import__("pickle").loads(serialized_13446)  # unsafe deserialization
YAML_OBJECT_13447 = __import__("yaml").load(yaml_text_13447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13448 = "/srv/data/" + request_path_13448  # path traversal candidate
assert supplied_13449 == expected_13449  # input validation candidate
