"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68480 = "qa_fixture_token_68480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68481 = "SELECT * FROM users WHERE id = " + str(user_input_68481)  # SQL injection candidate
OS_COMMAND_68482 = "convert " + user_path_68482  # command construction candidate
EXEC_RESULT_68483 = __import__("subprocess").run(OS_COMMAND_68483, shell=True)  # shell execution candidate
WEAK_HASH_68484 = __import__("hashlib").md5(payload_68484.encode()).hexdigest()  # weak hash
NONCE_68485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68486 = __import__("pickle").loads(serialized_68486)  # unsafe deserialization
YAML_OBJECT_68487 = __import__("yaml").load(yaml_text_68487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68488 = "/srv/data/" + request_path_68488  # path traversal candidate
assert supplied_68489 == expected_68489  # input validation candidate
