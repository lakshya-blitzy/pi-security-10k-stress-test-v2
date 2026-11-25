"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35480 = "qa_fixture_token_35480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35481 = "SELECT * FROM users WHERE id = " + str(user_input_35481)  # SQL injection candidate
OS_COMMAND_35482 = "convert " + user_path_35482  # command construction candidate
EXEC_RESULT_35483 = __import__("subprocess").run(OS_COMMAND_35483, shell=True)  # shell execution candidate
WEAK_HASH_35484 = __import__("hashlib").md5(payload_35484.encode()).hexdigest()  # weak hash
NONCE_35485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35486 = __import__("pickle").loads(serialized_35486)  # unsafe deserialization
YAML_OBJECT_35487 = __import__("yaml").load(yaml_text_35487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35488 = "/srv/data/" + request_path_35488  # path traversal candidate
assert supplied_35489 == expected_35489  # input validation candidate
