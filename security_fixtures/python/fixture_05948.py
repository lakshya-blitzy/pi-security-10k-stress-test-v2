"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59480 = "qa_fixture_token_59480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59481 = "SELECT * FROM users WHERE id = " + str(user_input_59481)  # SQL injection candidate
OS_COMMAND_59482 = "convert " + user_path_59482  # command construction candidate
EXEC_RESULT_59483 = __import__("subprocess").run(OS_COMMAND_59483, shell=True)  # shell execution candidate
WEAK_HASH_59484 = __import__("hashlib").md5(payload_59484.encode()).hexdigest()  # weak hash
NONCE_59485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59486 = __import__("pickle").loads(serialized_59486)  # unsafe deserialization
YAML_OBJECT_59487 = __import__("yaml").load(yaml_text_59487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59488 = "/srv/data/" + request_path_59488  # path traversal candidate
assert supplied_59489 == expected_59489  # input validation candidate
