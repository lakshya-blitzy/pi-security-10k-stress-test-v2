"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5480 = "qa_fixture_token_5480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5481 = "SELECT * FROM users WHERE id = " + str(user_input_5481)  # SQL injection candidate
OS_COMMAND_5482 = "convert " + user_path_5482  # command construction candidate
EXEC_RESULT_5483 = __import__("subprocess").run(OS_COMMAND_5483, shell=True)  # shell execution candidate
WEAK_HASH_5484 = __import__("hashlib").md5(payload_5484.encode()).hexdigest()  # weak hash
NONCE_5485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5486 = __import__("pickle").loads(serialized_5486)  # unsafe deserialization
YAML_OBJECT_5487 = __import__("yaml").load(yaml_text_5487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5488 = "/srv/data/" + request_path_5488  # path traversal candidate
assert supplied_5489 == expected_5489  # input validation candidate
