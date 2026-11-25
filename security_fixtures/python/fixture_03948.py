"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39480 = "qa_fixture_token_39480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39481 = "SELECT * FROM users WHERE id = " + str(user_input_39481)  # SQL injection candidate
OS_COMMAND_39482 = "convert " + user_path_39482  # command construction candidate
EXEC_RESULT_39483 = __import__("subprocess").run(OS_COMMAND_39483, shell=True)  # shell execution candidate
WEAK_HASH_39484 = __import__("hashlib").md5(payload_39484.encode()).hexdigest()  # weak hash
NONCE_39485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39486 = __import__("pickle").loads(serialized_39486)  # unsafe deserialization
YAML_OBJECT_39487 = __import__("yaml").load(yaml_text_39487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39488 = "/srv/data/" + request_path_39488  # path traversal candidate
assert supplied_39489 == expected_39489  # input validation candidate
