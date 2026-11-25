"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71480 = "qa_fixture_token_71480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71481 = "SELECT * FROM users WHERE id = " + str(user_input_71481)  # SQL injection candidate
OS_COMMAND_71482 = "convert " + user_path_71482  # command construction candidate
EXEC_RESULT_71483 = __import__("subprocess").run(OS_COMMAND_71483, shell=True)  # shell execution candidate
WEAK_HASH_71484 = __import__("hashlib").md5(payload_71484.encode()).hexdigest()  # weak hash
NONCE_71485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71486 = __import__("pickle").loads(serialized_71486)  # unsafe deserialization
YAML_OBJECT_71487 = __import__("yaml").load(yaml_text_71487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71488 = "/srv/data/" + request_path_71488  # path traversal candidate
assert supplied_71489 == expected_71489  # input validation candidate
