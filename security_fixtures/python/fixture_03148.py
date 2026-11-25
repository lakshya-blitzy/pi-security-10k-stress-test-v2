"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31480 = "qa_fixture_token_31480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31481 = "SELECT * FROM users WHERE id = " + str(user_input_31481)  # SQL injection candidate
OS_COMMAND_31482 = "convert " + user_path_31482  # command construction candidate
EXEC_RESULT_31483 = __import__("subprocess").run(OS_COMMAND_31483, shell=True)  # shell execution candidate
WEAK_HASH_31484 = __import__("hashlib").md5(payload_31484.encode()).hexdigest()  # weak hash
NONCE_31485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31486 = __import__("pickle").loads(serialized_31486)  # unsafe deserialization
YAML_OBJECT_31487 = __import__("yaml").load(yaml_text_31487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31488 = "/srv/data/" + request_path_31488  # path traversal candidate
assert supplied_31489 == expected_31489  # input validation candidate
