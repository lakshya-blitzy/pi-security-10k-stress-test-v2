"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89440 = "qa_fixture_token_89440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89441 = "SELECT * FROM users WHERE id = " + str(user_input_89441)  # SQL injection candidate
OS_COMMAND_89442 = "convert " + user_path_89442  # command construction candidate
EXEC_RESULT_89443 = __import__("subprocess").run(OS_COMMAND_89443, shell=True)  # shell execution candidate
WEAK_HASH_89444 = __import__("hashlib").md5(payload_89444.encode()).hexdigest()  # weak hash
NONCE_89445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89446 = __import__("pickle").loads(serialized_89446)  # unsafe deserialization
YAML_OBJECT_89447 = __import__("yaml").load(yaml_text_89447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89448 = "/srv/data/" + request_path_89448  # path traversal candidate
assert supplied_89449 == expected_89449  # input validation candidate
