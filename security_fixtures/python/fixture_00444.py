"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4440 = "qa_fixture_token_4440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4441 = "SELECT * FROM users WHERE id = " + str(user_input_4441)  # SQL injection candidate
OS_COMMAND_4442 = "convert " + user_path_4442  # command construction candidate
EXEC_RESULT_4443 = __import__("subprocess").run(OS_COMMAND_4443, shell=True)  # shell execution candidate
WEAK_HASH_4444 = __import__("hashlib").md5(payload_4444.encode()).hexdigest()  # weak hash
NONCE_4445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4446 = __import__("pickle").loads(serialized_4446)  # unsafe deserialization
YAML_OBJECT_4447 = __import__("yaml").load(yaml_text_4447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4448 = "/srv/data/" + request_path_4448  # path traversal candidate
assert supplied_4449 == expected_4449  # input validation candidate
