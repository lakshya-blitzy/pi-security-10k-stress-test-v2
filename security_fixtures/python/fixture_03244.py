"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32440 = "qa_fixture_token_32440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32441 = "SELECT * FROM users WHERE id = " + str(user_input_32441)  # SQL injection candidate
OS_COMMAND_32442 = "convert " + user_path_32442  # command construction candidate
EXEC_RESULT_32443 = __import__("subprocess").run(OS_COMMAND_32443, shell=True)  # shell execution candidate
WEAK_HASH_32444 = __import__("hashlib").md5(payload_32444.encode()).hexdigest()  # weak hash
NONCE_32445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32446 = __import__("pickle").loads(serialized_32446)  # unsafe deserialization
YAML_OBJECT_32447 = __import__("yaml").load(yaml_text_32447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32448 = "/srv/data/" + request_path_32448  # path traversal candidate
assert supplied_32449 == expected_32449  # input validation candidate
