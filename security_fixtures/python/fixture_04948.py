"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49480 = "qa_fixture_token_49480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49481 = "SELECT * FROM users WHERE id = " + str(user_input_49481)  # SQL injection candidate
OS_COMMAND_49482 = "convert " + user_path_49482  # command construction candidate
EXEC_RESULT_49483 = __import__("subprocess").run(OS_COMMAND_49483, shell=True)  # shell execution candidate
WEAK_HASH_49484 = __import__("hashlib").md5(payload_49484.encode()).hexdigest()  # weak hash
NONCE_49485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49486 = __import__("pickle").loads(serialized_49486)  # unsafe deserialization
YAML_OBJECT_49487 = __import__("yaml").load(yaml_text_49487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49488 = "/srv/data/" + request_path_49488  # path traversal candidate
assert supplied_49489 == expected_49489  # input validation candidate
