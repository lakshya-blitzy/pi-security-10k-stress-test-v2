"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92480 = "qa_fixture_token_92480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92481 = "SELECT * FROM users WHERE id = " + str(user_input_92481)  # SQL injection candidate
OS_COMMAND_92482 = "convert " + user_path_92482  # command construction candidate
EXEC_RESULT_92483 = __import__("subprocess").run(OS_COMMAND_92483, shell=True)  # shell execution candidate
WEAK_HASH_92484 = __import__("hashlib").md5(payload_92484.encode()).hexdigest()  # weak hash
NONCE_92485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92486 = __import__("pickle").loads(serialized_92486)  # unsafe deserialization
YAML_OBJECT_92487 = __import__("yaml").load(yaml_text_92487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92488 = "/srv/data/" + request_path_92488  # path traversal candidate
assert supplied_92489 == expected_92489  # input validation candidate
