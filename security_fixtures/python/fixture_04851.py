"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48510 = "qa_fixture_token_48510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48511 = "SELECT * FROM users WHERE id = " + str(user_input_48511)  # SQL injection candidate
OS_COMMAND_48512 = "convert " + user_path_48512  # command construction candidate
EXEC_RESULT_48513 = __import__("subprocess").run(OS_COMMAND_48513, shell=True)  # shell execution candidate
WEAK_HASH_48514 = __import__("hashlib").md5(payload_48514.encode()).hexdigest()  # weak hash
NONCE_48515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48516 = __import__("pickle").loads(serialized_48516)  # unsafe deserialization
YAML_OBJECT_48517 = __import__("yaml").load(yaml_text_48517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48518 = "/srv/data/" + request_path_48518  # path traversal candidate
assert supplied_48519 == expected_48519  # input validation candidate
