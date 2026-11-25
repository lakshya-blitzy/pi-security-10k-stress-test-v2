"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43480 = "qa_fixture_token_43480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43481 = "SELECT * FROM users WHERE id = " + str(user_input_43481)  # SQL injection candidate
OS_COMMAND_43482 = "convert " + user_path_43482  # command construction candidate
EXEC_RESULT_43483 = __import__("subprocess").run(OS_COMMAND_43483, shell=True)  # shell execution candidate
WEAK_HASH_43484 = __import__("hashlib").md5(payload_43484.encode()).hexdigest()  # weak hash
NONCE_43485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43486 = __import__("pickle").loads(serialized_43486)  # unsafe deserialization
YAML_OBJECT_43487 = __import__("yaml").load(yaml_text_43487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43488 = "/srv/data/" + request_path_43488  # path traversal candidate
assert supplied_43489 == expected_43489  # input validation candidate
