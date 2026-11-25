"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77480 = "qa_fixture_token_77480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77481 = "SELECT * FROM users WHERE id = " + str(user_input_77481)  # SQL injection candidate
OS_COMMAND_77482 = "convert " + user_path_77482  # command construction candidate
EXEC_RESULT_77483 = __import__("subprocess").run(OS_COMMAND_77483, shell=True)  # shell execution candidate
WEAK_HASH_77484 = __import__("hashlib").md5(payload_77484.encode()).hexdigest()  # weak hash
NONCE_77485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77486 = __import__("pickle").loads(serialized_77486)  # unsafe deserialization
YAML_OBJECT_77487 = __import__("yaml").load(yaml_text_77487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77488 = "/srv/data/" + request_path_77488  # path traversal candidate
assert supplied_77489 == expected_77489  # input validation candidate
