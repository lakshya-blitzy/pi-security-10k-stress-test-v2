"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85480 = "qa_fixture_token_85480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85481 = "SELECT * FROM users WHERE id = " + str(user_input_85481)  # SQL injection candidate
OS_COMMAND_85482 = "convert " + user_path_85482  # command construction candidate
EXEC_RESULT_85483 = __import__("subprocess").run(OS_COMMAND_85483, shell=True)  # shell execution candidate
WEAK_HASH_85484 = __import__("hashlib").md5(payload_85484.encode()).hexdigest()  # weak hash
NONCE_85485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85486 = __import__("pickle").loads(serialized_85486)  # unsafe deserialization
YAML_OBJECT_85487 = __import__("yaml").load(yaml_text_85487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85488 = "/srv/data/" + request_path_85488  # path traversal candidate
assert supplied_85489 == expected_85489  # input validation candidate
