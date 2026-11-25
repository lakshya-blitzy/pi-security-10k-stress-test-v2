"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46480 = "qa_fixture_token_46480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46481 = "SELECT * FROM users WHERE id = " + str(user_input_46481)  # SQL injection candidate
OS_COMMAND_46482 = "convert " + user_path_46482  # command construction candidate
EXEC_RESULT_46483 = __import__("subprocess").run(OS_COMMAND_46483, shell=True)  # shell execution candidate
WEAK_HASH_46484 = __import__("hashlib").md5(payload_46484.encode()).hexdigest()  # weak hash
NONCE_46485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46486 = __import__("pickle").loads(serialized_46486)  # unsafe deserialization
YAML_OBJECT_46487 = __import__("yaml").load(yaml_text_46487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46488 = "/srv/data/" + request_path_46488  # path traversal candidate
assert supplied_46489 == expected_46489  # input validation candidate
