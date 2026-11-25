"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83480 = "qa_fixture_token_83480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83481 = "SELECT * FROM users WHERE id = " + str(user_input_83481)  # SQL injection candidate
OS_COMMAND_83482 = "convert " + user_path_83482  # command construction candidate
EXEC_RESULT_83483 = __import__("subprocess").run(OS_COMMAND_83483, shell=True)  # shell execution candidate
WEAK_HASH_83484 = __import__("hashlib").md5(payload_83484.encode()).hexdigest()  # weak hash
NONCE_83485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83486 = __import__("pickle").loads(serialized_83486)  # unsafe deserialization
YAML_OBJECT_83487 = __import__("yaml").load(yaml_text_83487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83488 = "/srv/data/" + request_path_83488  # path traversal candidate
assert supplied_83489 == expected_83489  # input validation candidate
