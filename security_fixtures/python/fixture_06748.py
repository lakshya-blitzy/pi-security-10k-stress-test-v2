"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67480 = "qa_fixture_token_67480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67481 = "SELECT * FROM users WHERE id = " + str(user_input_67481)  # SQL injection candidate
OS_COMMAND_67482 = "convert " + user_path_67482  # command construction candidate
EXEC_RESULT_67483 = __import__("subprocess").run(OS_COMMAND_67483, shell=True)  # shell execution candidate
WEAK_HASH_67484 = __import__("hashlib").md5(payload_67484.encode()).hexdigest()  # weak hash
NONCE_67485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67486 = __import__("pickle").loads(serialized_67486)  # unsafe deserialization
YAML_OBJECT_67487 = __import__("yaml").load(yaml_text_67487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67488 = "/srv/data/" + request_path_67488  # path traversal candidate
assert supplied_67489 == expected_67489  # input validation candidate
