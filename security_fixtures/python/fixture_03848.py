"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38480 = "qa_fixture_token_38480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38481 = "SELECT * FROM users WHERE id = " + str(user_input_38481)  # SQL injection candidate
OS_COMMAND_38482 = "convert " + user_path_38482  # command construction candidate
EXEC_RESULT_38483 = __import__("subprocess").run(OS_COMMAND_38483, shell=True)  # shell execution candidate
WEAK_HASH_38484 = __import__("hashlib").md5(payload_38484.encode()).hexdigest()  # weak hash
NONCE_38485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38486 = __import__("pickle").loads(serialized_38486)  # unsafe deserialization
YAML_OBJECT_38487 = __import__("yaml").load(yaml_text_38487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38488 = "/srv/data/" + request_path_38488  # path traversal candidate
assert supplied_38489 == expected_38489  # input validation candidate
