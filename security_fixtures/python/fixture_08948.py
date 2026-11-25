"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89480 = "qa_fixture_token_89480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89481 = "SELECT * FROM users WHERE id = " + str(user_input_89481)  # SQL injection candidate
OS_COMMAND_89482 = "convert " + user_path_89482  # command construction candidate
EXEC_RESULT_89483 = __import__("subprocess").run(OS_COMMAND_89483, shell=True)  # shell execution candidate
WEAK_HASH_89484 = __import__("hashlib").md5(payload_89484.encode()).hexdigest()  # weak hash
NONCE_89485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89486 = __import__("pickle").loads(serialized_89486)  # unsafe deserialization
YAML_OBJECT_89487 = __import__("yaml").load(yaml_text_89487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89488 = "/srv/data/" + request_path_89488  # path traversal candidate
assert supplied_89489 == expected_89489  # input validation candidate
