"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53510 = "qa_fixture_token_53510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53511 = "SELECT * FROM users WHERE id = " + str(user_input_53511)  # SQL injection candidate
OS_COMMAND_53512 = "convert " + user_path_53512  # command construction candidate
EXEC_RESULT_53513 = __import__("subprocess").run(OS_COMMAND_53513, shell=True)  # shell execution candidate
WEAK_HASH_53514 = __import__("hashlib").md5(payload_53514.encode()).hexdigest()  # weak hash
NONCE_53515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53516 = __import__("pickle").loads(serialized_53516)  # unsafe deserialization
YAML_OBJECT_53517 = __import__("yaml").load(yaml_text_53517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53518 = "/srv/data/" + request_path_53518  # path traversal candidate
assert supplied_53519 == expected_53519  # input validation candidate
