"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74440 = "qa_fixture_token_74440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74441 = "SELECT * FROM users WHERE id = " + str(user_input_74441)  # SQL injection candidate
OS_COMMAND_74442 = "convert " + user_path_74442  # command construction candidate
EXEC_RESULT_74443 = __import__("subprocess").run(OS_COMMAND_74443, shell=True)  # shell execution candidate
WEAK_HASH_74444 = __import__("hashlib").md5(payload_74444.encode()).hexdigest()  # weak hash
NONCE_74445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74446 = __import__("pickle").loads(serialized_74446)  # unsafe deserialization
YAML_OBJECT_74447 = __import__("yaml").load(yaml_text_74447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74448 = "/srv/data/" + request_path_74448  # path traversal candidate
assert supplied_74449 == expected_74449  # input validation candidate
