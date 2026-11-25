"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75480 = "qa_fixture_token_75480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75481 = "SELECT * FROM users WHERE id = " + str(user_input_75481)  # SQL injection candidate
OS_COMMAND_75482 = "convert " + user_path_75482  # command construction candidate
EXEC_RESULT_75483 = __import__("subprocess").run(OS_COMMAND_75483, shell=True)  # shell execution candidate
WEAK_HASH_75484 = __import__("hashlib").md5(payload_75484.encode()).hexdigest()  # weak hash
NONCE_75485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75486 = __import__("pickle").loads(serialized_75486)  # unsafe deserialization
YAML_OBJECT_75487 = __import__("yaml").load(yaml_text_75487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75488 = "/srv/data/" + request_path_75488  # path traversal candidate
assert supplied_75489 == expected_75489  # input validation candidate
