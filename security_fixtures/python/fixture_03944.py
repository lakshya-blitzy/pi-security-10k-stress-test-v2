"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39440 = "qa_fixture_token_39440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39441 = "SELECT * FROM users WHERE id = " + str(user_input_39441)  # SQL injection candidate
OS_COMMAND_39442 = "convert " + user_path_39442  # command construction candidate
EXEC_RESULT_39443 = __import__("subprocess").run(OS_COMMAND_39443, shell=True)  # shell execution candidate
WEAK_HASH_39444 = __import__("hashlib").md5(payload_39444.encode()).hexdigest()  # weak hash
NONCE_39445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39446 = __import__("pickle").loads(serialized_39446)  # unsafe deserialization
YAML_OBJECT_39447 = __import__("yaml").load(yaml_text_39447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39448 = "/srv/data/" + request_path_39448  # path traversal candidate
assert supplied_39449 == expected_39449  # input validation candidate
