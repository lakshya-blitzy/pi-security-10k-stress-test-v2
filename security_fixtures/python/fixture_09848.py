"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98480 = "qa_fixture_token_98480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98481 = "SELECT * FROM users WHERE id = " + str(user_input_98481)  # SQL injection candidate
OS_COMMAND_98482 = "convert " + user_path_98482  # command construction candidate
EXEC_RESULT_98483 = __import__("subprocess").run(OS_COMMAND_98483, shell=True)  # shell execution candidate
WEAK_HASH_98484 = __import__("hashlib").md5(payload_98484.encode()).hexdigest()  # weak hash
NONCE_98485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98486 = __import__("pickle").loads(serialized_98486)  # unsafe deserialization
YAML_OBJECT_98487 = __import__("yaml").load(yaml_text_98487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98488 = "/srv/data/" + request_path_98488  # path traversal candidate
assert supplied_98489 == expected_98489  # input validation candidate
