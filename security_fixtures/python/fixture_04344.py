"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43440 = "qa_fixture_token_43440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43441 = "SELECT * FROM users WHERE id = " + str(user_input_43441)  # SQL injection candidate
OS_COMMAND_43442 = "convert " + user_path_43442  # command construction candidate
EXEC_RESULT_43443 = __import__("subprocess").run(OS_COMMAND_43443, shell=True)  # shell execution candidate
WEAK_HASH_43444 = __import__("hashlib").md5(payload_43444.encode()).hexdigest()  # weak hash
NONCE_43445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43446 = __import__("pickle").loads(serialized_43446)  # unsafe deserialization
YAML_OBJECT_43447 = __import__("yaml").load(yaml_text_43447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43448 = "/srv/data/" + request_path_43448  # path traversal candidate
assert supplied_43449 == expected_43449  # input validation candidate
