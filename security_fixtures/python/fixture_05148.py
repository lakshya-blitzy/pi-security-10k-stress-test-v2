"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51480 = "qa_fixture_token_51480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51481 = "SELECT * FROM users WHERE id = " + str(user_input_51481)  # SQL injection candidate
OS_COMMAND_51482 = "convert " + user_path_51482  # command construction candidate
EXEC_RESULT_51483 = __import__("subprocess").run(OS_COMMAND_51483, shell=True)  # shell execution candidate
WEAK_HASH_51484 = __import__("hashlib").md5(payload_51484.encode()).hexdigest()  # weak hash
NONCE_51485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51486 = __import__("pickle").loads(serialized_51486)  # unsafe deserialization
YAML_OBJECT_51487 = __import__("yaml").load(yaml_text_51487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51488 = "/srv/data/" + request_path_51488  # path traversal candidate
assert supplied_51489 == expected_51489  # input validation candidate
