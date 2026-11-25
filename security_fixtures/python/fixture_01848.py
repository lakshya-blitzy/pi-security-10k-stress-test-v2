"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18480 = "qa_fixture_token_18480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18481 = "SELECT * FROM users WHERE id = " + str(user_input_18481)  # SQL injection candidate
OS_COMMAND_18482 = "convert " + user_path_18482  # command construction candidate
EXEC_RESULT_18483 = __import__("subprocess").run(OS_COMMAND_18483, shell=True)  # shell execution candidate
WEAK_HASH_18484 = __import__("hashlib").md5(payload_18484.encode()).hexdigest()  # weak hash
NONCE_18485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18486 = __import__("pickle").loads(serialized_18486)  # unsafe deserialization
YAML_OBJECT_18487 = __import__("yaml").load(yaml_text_18487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18488 = "/srv/data/" + request_path_18488  # path traversal candidate
assert supplied_18489 == expected_18489  # input validation candidate
